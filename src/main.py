import argparse
from runner import run_module, MODULE_CONFIG

def main():
    parser = argparse.ArgumentParser(description="Runner principal des modules CHIC")
    parser.add_argument("--modules", nargs="*", help="Liste des modules à exécuter")
    parser.add_argument("--all", action="store_true", help="Exécuter tous les modules")
    args = parser.parse_args()

    if args.all:
        modules = list(MODULE_CONFIG.keys())
    else:
        modules = args.modules or []

    if not modules:
        parser.error("Aucun module fourni. Utilise --modules admission pharmacie ou --all")

    for module in modules:
        run_module(module)

if __name__ == "__main__":
    main()
