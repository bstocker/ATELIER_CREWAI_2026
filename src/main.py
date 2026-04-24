import argparse
from runner import run_module, run_transversal_consolidation, MODULE_CONFIG

def main():
    parser = argparse.ArgumentParser(description="Runner principal des modules CHIC")
    parser.add_argument("--modules", nargs="*", help="Liste des modules à exécuter")
    parser.add_argument("--all", action="store_true", help="Exécuter tous les modules")
    parser.add_argument(
        "--transversal",
        action="store_true",
        help="Lancer la consolidation transverse après les analyses modules"
    )
    args = parser.parse_args()

    if args.all:
        modules = list(MODULE_CONFIG.keys())
    else:
        modules = args.modules or []

    if not modules and not args.transversal:
        parser.error("Aucun module fourni. Utilise --modules admission pharmacie, --all ou --transversal")

    for module in modules:
        run_module(module)

    if args.transversal:
        run_transversal_consolidation()

if __name__ == "__main__":
    main()
