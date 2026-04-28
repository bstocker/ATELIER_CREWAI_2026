from pathlib import Path
from typing import Type

from pydantic import BaseModel, Field
from crewai.tools import BaseTool

from loaders.multiformat_loader import load_file


class DocumentQueryInput(BaseModel):
    query: str = Field(
        ...,
        description=(
            "Passe 'list' pour lister les fichiers disponibles, "
            "ou le nom d'un fichier pour lire son contenu complet."
        ),
    )


class DocumentAccessTool(BaseTool):
    name: str
    description: str
    base_dir: str
    args_schema: Type[BaseModel] = DocumentQueryInput

    def _run(self, query: str) -> str:
        base = Path(self.base_dir)
        q = query.strip()

        if q.lower() == "list":
            files = sorted(str(f.relative_to(base)) for f in base.rglob("*") if f.is_file())
            if not files:
                return "Aucun document disponible."
            return "Documents disponibles :\n" + "\n".join(f"  - {f}" for f in files)

        target = base / q
        if target.exists() and target.is_file():
            return load_file(target)

        matches = [f for f in base.rglob("*") if f.is_file() and q.lower() in f.name.lower()]
        if matches:
            return load_file(matches[0])

        available = sorted(f.name for f in base.rglob("*") if f.is_file())
        return f"Fichier '{q}' introuvable. Disponibles : {', '.join(available)}"


def make_formal_tool(formal_dir: Path) -> DocumentAccessTool:
    return DocumentAccessTool(
        name="Accès documents formels",
        description=(
            "Accède aux documents formels du module. "
            "Passe 'list' pour voir les fichiers disponibles, "
            "ou le nom exact d'un fichier pour lire son contenu."
        ),
        base_dir=str(formal_dir),
    )


def make_real_tool(real_dir: Path) -> DocumentAccessTool:
    return DocumentAccessTool(
        name="Accès documents réels",
        description=(
            "Accède aux documents de pratiques réelles du module. "
            "Passe 'list' pour voir les fichiers disponibles, "
            "ou le nom exact d'un fichier pour lire son contenu."
        ),
        base_dir=str(real_dir),
    )


def make_reports_tool(modules_dir: Path) -> DocumentAccessTool:
    return DocumentAccessTool(
        name="Accès rapports de réalignement",
        description=(
            "Lit les rapports de réalignement des modules (admission, pharmacie, bloc). "
            "Passe 'list' pour voir tous les rapports disponibles dans les outputs, "
            "ou un chemin relatif comme 'admission/outputs/rapport_realignement.md' "
            "pour lire un rapport spécifique."
        ),
        base_dir=str(modules_dir),
    )
