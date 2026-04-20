from pathlib import Path
import csv
import xml.etree.ElementTree as ET
from pypdf import PdfReader
from docx import Document
from openpyxl import load_workbook
from pptx import Presentation

TEXT_EXTENSIONS = {".md", ".txt", ".csv", ".xml"}
SUPPORTED_EXTENSIONS = {
    ".pdf", ".xlsx", ".xls", ".docx", ".png", ".jpg", ".jpeg", ".webp",
    ".xml", ".csv", ".md", ".txt", ".pptx", ".wav", ".mp3", ".m4a"
}

def _read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")

def _read_pdf(path: Path) -> str:
    reader = PdfReader(str(path))
    parts = []
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        parts.append(f"\n--- PDF page {i}: {path.name} ---\n{text}")
    return "\n".join(parts)

def _read_docx(path: Path) -> str:
    doc = Document(str(path))
    return "\n".join(p.text for p in doc.paragraphs if p.text.strip())

def _read_xlsx(path: Path) -> str:
    wb = load_workbook(str(path), data_only=True)
    chunks = []
    for ws in wb.worksheets:
        chunks.append(f"\n--- Sheet: {ws.title} ({path.name}) ---")
        for row in ws.iter_rows(values_only=True):
            vals = ["" if v is None else str(v) for v in row]
            if any(v.strip() for v in vals):
                chunks.append(" | ".join(vals))
    return "\n".join(chunks)

def _read_csv(path: Path) -> str:
    rows = []
    with path.open("r", encoding="utf-8", errors="ignore", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(" | ".join(row))
    return "\n".join(rows)

def _read_xml(path: Path) -> str:
    tree = ET.parse(str(path))
    root = tree.getroot()
    chunks = [f"XML root: {root.tag}"]
    for elem in root.iter():
        text = (elem.text or "").strip()
        if text:
            chunks.append(f"{elem.tag}: {text}")
    return "\n".join(chunks)

def _read_pptx(path: Path) -> str:
    prs = Presentation(str(path))
    chunks = []
    for i, slide in enumerate(prs.slides, start=1):
        chunks.append(f"\n--- Slide {i}: {path.name} ---")
        for shape in slide.shapes:
            if hasattr(shape, "text") and shape.text.strip():
                chunks.append(shape.text.strip())
    return "\n".join(chunks)

def _read_image_placeholder(path: Path) -> str:
    return f"[IMAGE PLACEHOLDER] Fichier image détecté: {path.name}. Ajouter un OCR ou un modèle vision pour extraction détaillée."

def _read_audio_placeholder(path: Path) -> str:
    return f"[AUDIO PLACEHOLDER] Fichier audio détecté: {path.name}. Brancher un moteur de transcription pour extraire le contenu."

def load_file(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in {".md", ".txt"}:
        return _read_text_file(path)
    if ext == ".pdf":
        return _read_pdf(path)
    if ext == ".docx":
        return _read_docx(path)
    if ext in {".xlsx", ".xls"}:
        return _read_xlsx(path)
    if ext == ".csv":
        return _read_csv(path)
    if ext == ".xml":
        return _read_xml(path)
    if ext == ".pptx":
        return _read_pptx(path)
    if ext in {".png", ".jpg", ".jpeg", ".webp"}:
        return _read_image_placeholder(path)
    if ext in {".wav", ".mp3", ".m4a"}:
        return _read_audio_placeholder(path)
    return f"[UNSUPPORTED] {path.name}"

def load_directory_contents(directory: Path) -> str:
    if not directory.exists():
        return ""
    chunks = []
    files = sorted([p for p in directory.rglob("*") if p.is_file()])
    for path in files:
        chunks.append(f"\n====================\nSOURCE: {path.name}\nTYPE: {path.suffix.lower()}\n====================")
        try:
            chunks.append(load_file(path))
        except Exception as e:
            chunks.append(f"[ERROR] Impossible de lire {path.name}: {e}")
    return "\n".join(chunks)
