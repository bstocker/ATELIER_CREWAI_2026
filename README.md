# POC CrewAI — Admission & Facturation SIH

Ce POC compare le **processus formel** du circuit admission-facturation avec les **pratiques réelles observées** afin d'identifier les désalignements socio-techniques et de proposer des actions de réalignement.

## Objectif

Produire automatiquement trois livrables :
- `outputs/analyse_formelle.md`
- `outputs/analyse_reelle.md`
- `outputs/rapport_realignement.md`

## Agents

1. **Analyste du processus formel**
2. **Analyste des pratiques réelles**
3. **Analyste de réalignement socio-technique**

## Lancement local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# renseigner OPENAI_API_KEY dans .env
python src/main.py
```

## Lancement dans GitHub Codespaces

Le projet contient un `.devcontainer/devcontainer.json`.
Une fois le Codespace démarré :

```bash
pip install -r requirements.txt
cp .env.example .env
# renseigner OPENAI_API_KEY dans .env ou dans les secrets Codespaces
python src/main.py
```
