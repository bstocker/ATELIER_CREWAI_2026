import os
from pathlib import Path
from dotenv import load_dotenv
import yaml
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
        "formal_agent_key": "formal_bloc_analyst",
        "real_agent_key": "real_bloc_analyst",
        "alignment_agent_key": "alignment_bloc_analyst",
        "formal_task_key": "formal_bloc_task",
        "real_task_key": "real_bloc_task",
        "alignment_task_key": "alignment_bloc_task",
    },
}

load_dotenv()

def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def build_llm() -> LLM:
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY introuvable. Renseigne-le dans .env ou les secrets.")
    return LLM(model=model, api_key=api_key)

def save_output(path: Path, content) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("" if content is None else str(content), encoding="utf-8")

def make_agent(cfg: dict, key: str, llm: LLM) -> Agent:
    return Agent(
        role=cfg[key]["role"],
        goal=cfg[key]["goal"],
        backstory=cfg[key]["backstory"],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

def run_module(module_name: str):
    if module_name not in MODULE_CONFIG:
        raise ValueError(f"Module inconnu: {module_name}")

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

    formal_task = Task(
        description=tasks_cfg[cfg["formal_task_key"]]["description"] + "\n\nDocuments source :\n" + formal_input,
        expected_output=tasks_cfg[cfg["formal_task_key"]]["expected_output"],
        agent=formal_agent,
    )
    real_task = Task(
        description=tasks_cfg[cfg["real_task_key"]]["description"] + "\n\nDocuments source :\n" + real_input,
        expected_output=tasks_cfg[cfg["real_task_key"]]["expected_output"],
        agent=real_agent,
    )
    alignment_task = Task(
        description=tasks_cfg[cfg["alignment_task_key"]]["description"],
        expected_output=tasks_cfg[cfg["alignment_task_key"]]["expected_output"],
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
