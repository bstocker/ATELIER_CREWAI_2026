import os
from pathlib import Path
from dotenv import load_dotenv
import yaml
from crewai import Agent, Task, Crew, Process, LLM

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "config"
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"

load_dotenv()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def build_llm() -> LLM:
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY introuvable. Renseigne-le dans .env ou les secrets.")
    return LLM(model=model, api_key=api_key)


def build_agents(llm, agents_cfg):
    formal_agent = Agent(
        role=agents_cfg["formal_analyst"]["role"],
        goal=agents_cfg["formal_analyst"]["goal"],
        backstory=agents_cfg["formal_analyst"]["backstory"],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    real_agent = Agent(
        role=agents_cfg["real_analyst"]["role"],
        goal=agents_cfg["real_analyst"]["goal"],
        backstory=agents_cfg["real_analyst"]["backstory"],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    alignment_agent = Agent(
        role=agents_cfg["alignment_analyst"]["role"],
        goal=agents_cfg["alignment_analyst"]["goal"],
        backstory=agents_cfg["alignment_analyst"]["backstory"],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    return formal_agent, real_agent, alignment_agent


def save_output(path: Path, content) -> None:
    if content is None:
        text = ""
    else:
        text = str(content)
    path.write_text(text, encoding="utf-8")


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    formal_input = read_text(DATA_DIR / "formal" / "admission_facturation_formel.md")
    real_input = read_text(DATA_DIR / "real" / "admission_facturation_reel.md")

    agents_cfg = load_yaml(CONFIG_DIR / "agents.yaml")
    tasks_cfg = load_yaml(CONFIG_DIR / "tasks.yaml")
    llm = build_llm()

    formal_agent, real_agent, alignment_agent = build_agents(llm, agents_cfg)

    formal_task = Task(
        description=tasks_cfg["formal_task"]["description"] + "\n\nDocument source :\n" + formal_input,
        expected_output=tasks_cfg["formal_task"]["expected_output"],
        agent=formal_agent,
    )

    real_task = Task(
        description=tasks_cfg["real_task"]["description"] + "\n\nDocument source :\n" + real_input,
        expected_output=tasks_cfg["real_task"]["expected_output"],
        agent=real_agent,
    )

    alignment_task = Task(
        description=tasks_cfg["alignment_task"]["description"],
        expected_output=tasks_cfg["alignment_task"]["expected_output"],
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

    # Sauvegarde explicite des sorties
    save_output(OUTPUT_DIR / "analyse_formelle.md", getattr(formal_task, "output", ""))
    save_output(OUTPUT_DIR / "analyse_reelle.md", getattr(real_task, "output", ""))
    save_output(OUTPUT_DIR / "rapport_realignement.md", getattr(alignment_task, "output", result))

    print("\n=== Exécution terminée ===")
    print(result)
    print(f"\nFichiers générés dans : {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
