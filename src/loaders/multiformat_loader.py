from pathlib import Path
import csv
import xml.etree.ElementTree as ET

from pypdf import PdfReader
from docx import Document
from openpyxl import load_workbook
from pptx import Presentation

from PIL import Image
import pytesseract
from pdf2image import convert_from_path


TEXT_EXTENSIONS = {".md", ".txt", ".csv", ".xml"}

SUPPORTED_EXTENSIONS = {
    ".pdf", ".xlsx", ".xls", ".docx", ".png", ".jpg", ".jpeg", ".webp",
    ".xml", ".csv", ".md", ".txt", ".pptx", ".wav", ".mp3", ".m4a"
}


# =====================================================
# OCR HELPERS
# =====================================================

def _is_text_usable(text: str) -> bool:
    if not text:
        return False

    text = text.strip()

    if len(text) < 30:
        return False

    if len(text.split()) < 5:
        return False

    return True


def _ocr_pdf(path: Path, lang="fra") -> str:
    images = convert_from_path(str(path), dpi=300)
    chunks = []

    for i, image in enumerate(images, start=1):
        txt = pytesseract.image_to_string(image, lang=lang)
        chunks.append(f"\n--- OCR PDF page {i}: {path.name} ---\n{txt}")

    return "\n".join(chunks)


def _ocr_image(path: Path, lang="fra") -> str:
    img = Image.open(path)
    txt = pytesseract.image_to_string(img, lang=lang)
    return f"\n--- OCR IMAGE: {path.name} ---\n{txt}"


# =====================================================
# READERS
# =====================================================

def _read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def _read_pdf(path: Path) -> str:
    reader = PdfReader(str(path))

    raw_texts = []
    formatted_parts = []

    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        raw_texts.append(text)
        formatted_parts.append(f"\n--- PDF page {i}: {path.name} ---\n{text}")

    raw_joined = "\n".join(raw_texts).strip()

    # Si le vrai texte extrait du PDF est exploitable, on le garde
    if _is_text_usable(raw_joined):
        return "\n".join(formatted_parts)

    # Sinon on bascule sur OCR
    return _ocr_pdf(path)


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


def _read_image(path: Path) -> str:
    return _ocr_image(path)


def _read_audio_placeholder(path: Path) -> str:
    return f"[AUDIO PLACEHOLDER] {path.name}"


# =====================================================
# DISPATCH
# =====================================================

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
        return _read_image(path)

    if ext in {".wav", ".mp3", ".m4a"}:
        return _read_audio_placeholder(path)

    return f"[UNSUPPORTED] {path.name}"


# =====================================================
# DIRECTORY LOADER
# =====================================================

def load_directory_contents(directory: Path) -> str:
    if not directory.exists():
        return ""

    chunks = []
    files = sorted([p for p in directory.rglob("*") if p.is_file()])

    for path in files:
        chunks.append(
            f"\n====================\n"
            f"SOURCE: {path.name}\n"
            f"TYPE: {path.suffix.lower()}\n"
            f"===================="
        )

        try:
            chunks.append(load_file(path))
        except Exception as e:
            chunks.append(f"[ERROR] Impossible de lire {path.name}: {e}")

    return "\n".join(chunks)
