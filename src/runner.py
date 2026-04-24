import os
from pathlib import Path

import yaml
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

from loaders import load_directory_contents


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


load_dotenv()


def load_yaml(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Fichier YAML introuvable : {path}")

    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if data is None:
        raise ValueError(f"Fichier YAML vide ou invalide : {path}")

    return data


def build_llm() -> LLM:
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY introuvable. Renseigne-le dans .env ou les secrets.")

    return LLM(
        model=model,
        api_key=api_key,
    )


def save_output(path: Path, content) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("" if content is None else str(content), encoding="utf-8")


def make_agent(cfg: dict, key: str, llm: LLM) -> Agent:
    if key not in cfg:
        raise KeyError(f"Agent '{key}' introuvable dans le fichier YAML.")

    return Agent(
        role=cfg[key]["role"],
        goal=cfg[key]["goal"],
        backstory=cfg[key]["backstory"],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )


def make_task(
    tasks_cfg: dict,
    task_key: str,
    agent: Agent,
    additional_description: str = "",
    context: list | None = None,
) -> Task:
    if task_key not in tasks_cfg:
        raise KeyError(f"Tâche '{task_key}' introuvable dans le fichier YAML.")

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

    agents_cfg = load_yaml(cfg["agents_file"])
    tasks_cfg = load_yaml(cfg["tasks_file"])
    llm = build_llm()

    formal_input = load_directory_contents(cfg["formal_dir"])
    real_input = load_directory_contents(cfg["real_dir"])

    output_dir = cfg["output_dir"]
    output_dir.mkdir(parents=True, exist_ok=True)

    formal_agent = make_agent(agents_cfg, cfg["formal_agent_key"], llm)
    real_agent = make_agent(agents_cfg, cfg["real_agent_key"], llm)
    alignment_agent = make_agent(agents_cfg, cfg["alignment_agent_key"], llm)

    formal_task = make_task(
        tasks_cfg=tasks_cfg,
        task_key=cfg["formal_task_key"],
        agent=formal_agent,
        additional_description="Documents source :\n" + formal_input,
    )

    real_task = make_task(
        tasks_cfg=tasks_cfg,
        task_key=cfg["real_task_key"],
        agent=real_agent,
        additional_description="Documents source :\n" + real_input,
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

    result = crew.kickoff()

    save_output(output_dir / "analyse_formelle.md", getattr(formal_task, "output", ""))
    save_output(output_dir / "analyse_reelle.md", getattr(real_task, "output", ""))
    save_output(output_dir / "rapport_realignement.md", getattr(alignment_task, "output", result))

    print(f"\n=== Exécution {module_name} terminée ===")
    print(f"Fichiers générés dans : {output_dir}")

    return result


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
                f"Aucun rapport de réalignement trouvé pour ce module."
            )

    return "\n".join(reports)


def run_transversal_consolidation():
    cfg = TRANSVERSAL_CONFIG

    agents_cfg = load_yaml(cfg["agents_file"])
    tasks_cfg = load_yaml(cfg["tasks_file"])
    llm = build_llm()

    output_dir = cfg["output_dir"]
    output_dir.mkdir(parents=True, exist_ok=True)

    consolidated_input = collect_alignment_reports()

    if not consolidated_input.strip():
        raise ValueError("Aucun rapport de réalignement disponible pour la consolidation transverse.")

    transversal_agent = make_agent(agents_cfg, cfg["agent_key"], llm)

    transversal_task = make_task(
        tasks_cfg=tasks_cfg,
        task_key=cfg["task_key"],
        agent=transversal_agent,
        additional_description="Notes de réalignement des modules :\n" + consolidated_input,
    )

    crew = Crew(
        agents=[transversal_agent],
        tasks=[transversal_task],
        process=Process.sequential,
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
