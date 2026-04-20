from __future__ import annotations

from pathlib import Path
from typing import Optional

import pytesseract
from pdf2image import convert_from_path
from PIL import Image


def _ocr_image(image: Image.Image, lang: str = "fra") -> str:
    """
    OCR simple sur une image PIL.
    """
    return pytesseract.image_to_string(image, lang=lang)


def extract_text_with_simple_ocr(
    file_path: str | Path,
    lang: str = "fra",
    dpi: int = 300,
    first_page: Optional[int] = None,
    last_page: Optional[int] = None,
) -> str:
    """
    Réalise un OCR simple sur un fichier PDF image/scanné.

    Args:
        file_path: Chemin du PDF
        lang: Langue Tesseract (ex: 'fra', 'eng', 'fra+eng')
        dpi: Résolution de conversion PDF -> image
        first_page: Première page à traiter (1-based)
        last_page: Dernière page à traiter (1-based)

    Returns:
        Texte OCR concaténé
    """
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Fichier introuvable : {file_path}")

    images = convert_from_path(
        str(file_path),
        dpi=dpi,
        first_page=first_page,
        last_page=last_page,
    )

    pages_text = []

    for idx, image in enumerate(images, start=1):
        try:
            text = _ocr_image(image, lang=lang)
            pages_text.append(f"\n--- PAGE {idx} ---\n{text.strip()}\n")
        except Exception as exc:
            pages_text.append(f"\n--- PAGE {idx} ---\n[ERREUR OCR : {exc}]\n")

    return "\n".join(pages_text).strip()
