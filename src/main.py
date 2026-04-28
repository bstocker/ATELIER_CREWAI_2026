import argparse
from runner import (
    run_module,
    run_transversal_consolidation,
    validate_module,
    validate_transversal,
    MODULE_CONFIG,
)


def main():
    parser = argparse.ArgumentParser(description="Runner principal des modules CHIC")
    parser.add_argument("--modules", nargs="*", help="Liste des modules à exécuter")
    parser.add_argument("--all", action="store_true", help="Exécuter tous les modules")
    parser.add_argument(
        "--transversal",
        action="store_true",
        help="Lancer la consolidation transverse après les analyses modules",
    )
    parser.add_argument(
        "--validate",
        nargs="+",
        metavar="MODULE",
        help=(
            "Valide les outputs d'un ou plusieurs modules comme exemples few-shot. "
            "Utilise 'transversal' pour valider le rapport de consolidation. "
            "Ex: --validate admission pharmacie transversal"
        ),
    )
    args = parser.parse_args()

    # Validation des outputs comme exemples few-shot
    if args.validate:
        for target in args.validate:
            if target == "transversal":
                validate_transversal()
            elif target in MODULE_CONFIG:
                validate_module(target)
            else:
                parser.error(f"Module inconnu pour --validate : '{target}'. Choix : {list(MODULE_CONFIG.keys())} + transversal")
        return

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
