# Prérequis
```
sudo apt-get update
sudo apt-get install -y tesseract-ocr tesseract-ocr-fra poppler-utils
```
# Execution
```
Exécuter plusieurs modules depuis le runner principal
python src/main.py --modules admission
python src/main.py --modules pharmacie
python src/main.py --modules admission pharmacie
python src/main.py --all
```
# Variables
```
OPENAI_API_KEY=ta_cle_api
OPENAI_MODEL=gpt-4o-mini
```
