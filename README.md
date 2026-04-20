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

# Le répertoire formal du module concerné doit contenir :
* procédures
* modes opératoires
* organigrammes
* règles de gestion
* cartographies processus
* politiques qualité
* référentiels

# Le répertoire real représente le terrain :
* scans
* formulaires remplis
* mails
* extractions Excel
* incidents
* notes utilisateurs
* comptes rendus
* photos
* traces opérationnelles

# le cadre cognitif de l’agent (fichier agents_xxxxx.yaml) définit :
* rôle
* objectif
* posture
* angle d’analyse
* niveau d’exigence
* vocabulaire métier
* limites

# Le prompt agent doit définir :
- qui parle ?
- avec quelle expertise ?
- dans quel objectif ?
- avec quel niveau d’exigence ?

# Les prompts dans tasks.yaml définissent les commandes opérationnelle.
Une bonne task précise :
* ce qu’il faut produire ;
* la structure attendue ;
* le niveau de détail ;
* les critères ;
* les exclusions ;
* le format de sortie.
