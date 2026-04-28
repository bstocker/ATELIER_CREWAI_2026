import os
from pathlib import Path

import yaml
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

from loaders import load_directory_contents
from tools import make_formal_tool, make_real_tool, make_reports_tool


BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "config"


MODULE_CONFIG = {
    "admission": {
        "module_dir": BASE_DIR / "modules" / "admission",
        "formal_dir": BASE_DIR / "modules" / "admission" / "data" / "formal",
        "real_dir": BASE_DIR / "modules" / "admission" / "data" / "real",
        "output_dir": BASE_DIR / "modules" / "admission" / "outputs",
        "agents_file": CONFIG_DIR / "agents_admission.yaml",
        "tasks_file": CONFIG_DIR / "tasks_admission.yaml",
        "formal_agent_key": "formal_analyst",
        "real_agent_key": "real_analyst",
        "alignment_agent_key": "alignment_analyst",
        "formal_task_key": "formal_task",
        "real_task_key": "real_task",
        "alignment_task_key": "alignment_task",
    },
    "pharmacie": {
        "module_dir": BASE_DIR / "modules" / "pharmacie",
        "formal_dir": BASE_DIR / "modules" / "pharmacie" / "data" / "formal",
        "real_dir": BASE_DIR / "modules" / "pharmacie" / "data" / "real",
        "output_dir": BASE_DIR / "modules" / "pharmacie" / "outputs",
        "agents_file": CONFIG_DIR / "agents_pharmacie.yaml",
        "tasks_file": CONFIG_DIR / "tasks_pharmacie.yaml",
        "formal_agent_key": "formal_pharmacy_analyst",
        "real_agent_key": "real_pharmacy_analyst",
        "alignment_agent_key": "alignment_pharmacy_analyst",
        "formal_task_key": "formal_pharmacy_task",
        "real_task_key": "real_pharmacy_task",
        "alignment_task_key": "alignment_pharmacy_task",
    },
    "bloc": {
        "module_dir": BASE_DIR / "modules" / "bloc",
        "formal_dir": BASE_DIR / "modules" / "bloc" / "data" / "formal",
        "real_dir": BASE_DIR / "modules" / "bloc" / "data" / "real",
        "output_dir": BASE_DIR / "modules" / "bloc" / "outputs",
        "agents_file": CONFIG_DIR / "agents_bloc.yaml",
        "tasks_file": CONFIG_DIR / "tasks_bloc.yaml",
        "formal_agent_key": "formal_analyst",
        "real_agent_key": "real_analyst",
        "alignment_agent_key": "alignment_analyst",
        "formal_task_key": "formal_task",
        "real_task_key": "real_task",
        "alignment_task_key": "alignment_task",
    },
}


TRANSVERSAL_CONFIG = {
    "output_dir": BASE_DIR / "transversal" / "outputs",
    "agents_file": CONFIG_DIR / "agents_transversal_capacitating_consolidator.yaml",
    "tasks_file": CONFIG_DIR / "tasks_transversal_capacitating_consolidator.yaml",
    "agent_key": "transversal_capacitating_consolidator",
    "task_key": "transversal_consolidation_task",
}

# Sections obligatoires dans un rapport de réalignement valide
ALIGNMENT_REQUIRED_SECTIONS = ["désalignement", "quick win", "action structurante"]
ALIGNMENT_MAX_RETRIES = 2


load_dotenv()


def load_yaml(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Fichier YAML introuvable : {path}")

    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if data is None:
        raise ValueError(f"Fichier YAML vide ou invalide : {path}")

    return data


def build_llm(profile: str = "mini") -> LLM:
    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY introuvable. Renseigne-le dans .env ou secrets.")

    if profile == "strong":
        model = os.getenv("CLAUDE_MODEL_STRONG", "claude-sonnet-4-6")
    else:
        model = os.getenv("CLAUDE_MODEL_MINI", "claude-haiku-4-5")

    print(f"[LLM] Profil={profile} | Modèle={model}")

    return LLM(
        model=f"anthropic/{model}",
        api_key=api_key,
        max_tokens=32000,
    )


def save_output(path: Path, content) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if content is None:
        text = ""
    elif hasattr(content, "raw"):
        text = content.raw or ""
    else:
        text = str(content)
    path.write_text(text, encoding="utf-8")


def _get_output_text(task_output) -> str:
    if task_output is None:
        return ""
    if hasattr(task_output, "raw"):
        return task_output.raw or ""
    return str(task_output)


def _check_alignment_quality(text: str) -> list[str]:
    return [s for s in ALIGNMENT_REQUIRED_SECTIONS if s.lower() not in text.lower()]


def _make_file_listing(directory: Path) -> str:
    files = sorted(f.name for f in directory.rglob("*") if f.is_file())
    if not files:
        return "Aucun fichier disponible."
    return "\n".join(f"  - {f}" for f in files)


def make_agent(
    cfg: dict,
    key: str,
    llm: LLM,
    tools: list | None = None,
    allow_delegation: bool = False,
) -> Agent:
    if key not in cfg:
        raise KeyError(f"Agent '{key}' introuvable dans le YAML.")

    return Agent(
        role=cfg[key]["role"],
        goal=cfg[key]["goal"],
        backstory=cfg[key]["backstory"],
        llm=llm,
        tools=tools or [],
        verbose=True,
        allow_delegation=allow_delegation,
    )


def make_task(
    tasks_cfg: dict,
    task_key: str,
    agent: Agent,
    additional_description: str = "",
    context: list | None = None,
) -> Task:
    if task_key not in tasks_cfg:
        raise KeyError(f"Tâche '{task_key}' introuvable dans le YAML.")

    description = tasks_cfg[task_key]["description"]

    if additional_description:
        description += "\n\n" + additional_description

    return Task(
        description=description,
        expected_output=tasks_cfg[task_key]["expected_output"],
        agent=agent,
        context=context or [],
    )


def run_module(module_name: str):
    if module_name not in MODULE_CONFIG:
        raise ValueError(f"Module inconnu : {module_name}")

    cfg = MODULE_CONFIG[module_name]

    print(f"\n===== Lancement module : {module_name.upper()} =====")

    agents_cfg = load_yaml(cfg["agents_file"])
    tasks_cfg = load_yaml(cfg["tasks_file"])

    formal_llm = build_llm("mini")
    real_llm = build_llm("mini")
    alignment_llm = build_llm("strong")

    output_dir = cfg["output_dir"]
    output_dir.mkdir(parents=True, exist_ok=True)

    # Outils par agent (priorité 1 + 3)
    formal_tool = make_formal_tool(cfg["formal_dir"])
    real_tool = make_real_tool(cfg["real_dir"])

    formal_agent = make_agent(
        agents_cfg, cfg["formal_agent_key"], formal_llm,
        tools=[formal_tool],
    )
    real_agent = make_agent(
        agents_cfg, cfg["real_agent_key"], real_llm,
        tools=[real_tool],
    )
    # Délégation activée pour l'agent de réalignement (priorité 3)
    alignment_agent = make_agent(
        agents_cfg, cfg["alignment_agent_key"], alignment_llm,
        tools=[formal_tool, real_tool],
        allow_delegation=True,
    )

    formal_task = make_task(
        tasks_cfg=tasks_cfg,
        task_key=cfg["formal_task_key"],
        agent=formal_agent,
        additional_description=(
            "Documents formels disponibles via l'outil 'Accès documents formels' :\n"
            + _make_file_listing(cfg["formal_dir"])
            + "\n\nUtilise l'outil pour lire les documents et effectuer ton analyse."
        ),
    )

    real_task = make_task(
        tasks_cfg=tasks_cfg,
        task_key=cfg["real_task_key"],
        agent=real_agent,
        additional_description=(
            "Documents réels disponibles via l'outil 'Accès documents réels' :\n"
            + _make_file_listing(cfg["real_dir"])
            + "\n\nUtilise l'outil pour lire les documents et effectuer ton analyse."
        ),
    )

    alignment_task = make_task(
        tasks_cfg=tasks_cfg,
        task_key=cfg["alignment_task_key"],
        agent=alignment_agent,
        context=[formal_task, real_task],
    )

    crew = Crew(
        agents=[formal_agent, real_agent, alignment_agent],
        tasks=[formal_task, real_task, alignment_task],
        process=Process.sequential,
        verbose=True,
    )

    crew.kickoff()

    # Quality Gate (priorité 4) — relance alignment si sections manquantes
    alignment_output_text = _get_output_text(getattr(alignment_task, "output", None))
    missing = _check_alignment_quality(alignment_output_text)

    for attempt in range(ALIGNMENT_MAX_RETRIES):
        if not missing:
            break

        print(f"\n[QUALITY GATE] Tentative {attempt + 1}/{ALIGNMENT_MAX_RETRIES} — sections manquantes : {missing}")

        formal_raw = _get_output_text(getattr(formal_task, "output", None))
        real_raw = _get_output_text(getattr(real_task, "output", None))

        retry_task = make_task(
            tasks_cfg=tasks_cfg,
            task_key=cfg["alignment_task_key"],
            agent=alignment_agent,
            additional_description=(
                f"[RELANCE QUALITÉ — tentative {attempt + 2}]\n"
                f"Ta réponse précédente est incomplète. Sections obligatoires manquantes : "
                f"{', '.join(missing)}.\n"
                f"Couvre IMPÉRATIVEMENT ces sections dans ta réponse.\n\n"
                f"=== ANALYSE FORMELLE ===\n{formal_raw}\n\n"
                f"=== ANALYSE RÉELLE ===\n{real_raw}"
            ),
        )

        retry_crew = Crew(
            agents=[alignment_agent],
            tasks=[retry_task],
            process=Process.sequential,
            verbose=True,
        )
        retry_crew.kickoff()

        alignment_task = retry_task
        alignment_output_text = _get_output_text(getattr(retry_task, "output", None))
        missing = _check_alignment_quality(alignment_output_text)

    if missing:
        print(f"\n[QUALITY GATE] Max retries atteint. Sections toujours manquantes : {missing}")

    save_output(output_dir / "analyse_formelle.md", getattr(formal_task, "output", ""))
    save_output(output_dir / "analyse_reelle.md", getattr(real_task, "output", ""))
    save_output(
        output_dir / "rapport_realignement.md",
        getattr(alignment_task, "output", ""),
    )

    print(f"\n=== Exécution {module_name} terminée ===")
    print(f"Fichiers générés dans : {output_dir}")

    return getattr(alignment_task, "output", "")


def collect_alignment_reports() -> str:
    reports = []

    for module_name, cfg in MODULE_CONFIG.items():
        report_path = cfg["output_dir"] / "rapport_realignement.md"

        if report_path.exists():
            content = report_path.read_text(encoding="utf-8")
            reports.append(
                f"\n\n====================\n"
                f"MODULE : {module_name.upper()}\n"
                f"SOURCE : {report_path}\n"
                f"====================\n\n"
                f"{content}"
            )
        else:
            reports.append(
                f"\n\n====================\n"
                f"MODULE : {module_name.upper()}\n"
                f"RAPPORT ABSENT\n"
                f"====================\n\n"
                f"Aucun rapport disponible."
            )

    return "\n".join(reports)


def run_transversal_consolidation():
    print("\n===== Lancement consolidation transverse =====")

    cfg = TRANSVERSAL_CONFIG

    agents_cfg = load_yaml(cfg["agents_file"])
    tasks_cfg = load_yaml(cfg["tasks_file"])

    transversal_llm = build_llm("strong")
    manager_llm = build_llm("strong")

    output_dir = cfg["output_dir"]
    output_dir.mkdir(parents=True, exist_ok=True)

    consolidated_input = collect_alignment_reports()

    if not consolidated_input.strip():
        raise ValueError("Aucun rapport disponible pour consolidation.")

    # Outil pour re-lire des rapports spécifiques à la demande (priorité 1 + 2)
    reports_tool = make_reports_tool(BASE_DIR / "modules")

    transversal_agent = make_agent(
        agents_cfg,
        cfg["agent_key"],
        transversal_llm,
        tools=[reports_tool],
        allow_delegation=True,
    )

    transversal_task = make_task(
        tasks_cfg=tasks_cfg,
        task_key=cfg["task_key"],
        agent=transversal_agent,
        additional_description=(
            "Notes de réalignement des modules :\n"
            + consolidated_input
            + "\n\nUtilise l'outil 'Accès rapports de réalignement' pour relire "
            "un rapport spécifique si tu as besoin d'un approfondissement ciblé."
        ),
    )

    # Processus hiérarchique : manager orchestre la consolidation (priorité 2)
    crew = Crew(
        agents=[transversal_agent],
        tasks=[transversal_task],
        process=Process.hierarchical,
        manager_llm=manager_llm,
        verbose=True,
    )

    result = crew.kickoff()

    save_output(
        output_dir / "rapport_consolidation_transverse.md",
        getattr(transversal_task, "output", result),
    )

    print("\n=== Consolidation transverse terminée ===")
    print(f"Fichier généré dans : {output_dir}")

    return result
