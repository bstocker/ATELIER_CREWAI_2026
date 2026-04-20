# POC CrewAI CHIC — Architecture modulaire multiformat

Ce projet propose une architecture modulaire par domaine métier, avec support **multiformat**
pour les entrées `formal` et `real`.

## Formats pris en charge

- PDF
- Excel (`.xlsx`, `.xls`)
- Word (`.docx`)
- images (`.png`, `.jpg`, `.jpeg`, `.webp`)
- exports XML / CSV
- Markdown (`.md`)
- texte (`.txt`)
- PowerPoint (`.pptx`)
- audio (`.wav`, `.mp3`, `.m4a`) — **placeholder à brancher avec un moteur de transcription**

## Principe

Chaque module possède ses propres répertoires :

- `data/formal/`
- `data/real/`
- `outputs/`

Les entrées sont chargées automatiquement par un loader multiformat qui concatène le contenu textuel
extrait de tous les fichiers présents dans `formal` ou `real`.

## Modules fournis

- `admission`
- `pharmacie`

## Lancement

### Exécuter un module
```bash
python src/main_admission.py
python src/main_pharmacie.py
```

### Exécuter plusieurs modules depuis le runner principal
```bash
python src/main.py --modules admission
python src/main.py --modules pharmacie
python src/main.py --modules admission pharmacie
python src/main.py --all
```

## Configuration

Créer un fichier `.env` à partir de `.env.example` et renseigner :

```text
OPENAI_API_KEY=ta_cle_api
OPENAI_MODEL=gpt-4o-mini
```

## Dépendances documentaires

Le projet inclut les bibliothèques de base pour extraire :
- PDF
- Word
- Excel
- PowerPoint
- CSV / XML / TXT / MD

Pour les **images** et le **son**, le loader est préparé mais nécessite un moteur complémentaire :
- OCR pour les images si tu veux extraire le texte d’un scan
- transcription audio pour les fichiers son

## Structure

```text
poc-crewai-chic-multiformat/
├── config/
├── modules/
│   ├── admission/
│   │   ├── data/
│   │   │   ├── formal/
│   │   │   └── real/
│   │   └── outputs/
│   └── pharmacie/
│       ├── data/
│       │   ├── formal/
│       │   └── real/
│       └── outputs/
├── src/
│   ├── main.py
│   ├── main_admission.py
│   ├── main_pharmacie.py
│   ├── runner.py
│   └── loaders/
└── .env.example
```
