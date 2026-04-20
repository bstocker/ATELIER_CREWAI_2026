from __future__ import annotations

from pathlib import Path

from src.loaders.multiformat_loader import load_directory


MODULE_NAME = "admission"

BASE_DIR = Path(__file__).resolve().parent.parent
MODULE_DIR = BASE_DIR / "modules" / MODULE_NAME

FORMAL_DIR = MODULE_DIR / "data" / "formal"
REAL_DIR = MODULE_DIR / "data" / "real"
OUTPUT_DIR = MODULE_DIR / "outputs"

FORMAL_OUTPUT_FILE = OUTPUT_DIR / "analyse_formelle.md"
REAL_OUTPUT_FILE = OUTPUT_DIR / "analyse_reelle.md"


def ensure_output_dir() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def build_formal_analysis_input() -> str:
    """
    Charge les sources formelles du module admission.
    OCR désactivé par défaut sur le formel.
    """
    return load_directory(
        directory=FORMAL_DIR,
        enable_ocr=False,
        ocr_lang="fra",
    )


def build_real_analysis_input() -> str:
    """
    Charge les sources réelles du module admission.
    OCR activé pour gérer les PDF scannés présents dans real.
    """
    return load_directory(
        directory=REAL_DIR,
        enable_ocr=True,
        ocr_lang="fra",
    )


def write_output(file_path: Path, title: str, content: str) -> None:
    file_path.write_text(
        f"# {title}\n\n{content if content.strip() else '[AUCUN CONTENU CHARGÉ]'}\n",
        encoding="utf-8",
    )


def main() -> None:
    ensure_output_dir()

    formal_content = build_formal_analysis_input()
    real_content = build_real_analysis_input()

    write_output(
        FORMAL_OUTPUT_FILE,
        "Analyse formelle - Admission",
        formal_content,
    )

    write_output(
        REAL_OUTPUT_FILE,
        "Analyse réelle - Admission",
        real_content,
    )

    print("Chargement terminé.")
    print(f"Analyse formelle : {FORMAL_OUTPUT_FILE}")
    print(f"Analyse réelle   : {REAL_OUTPUT_FILE}")


if __name__ == "__main__":
    main()
