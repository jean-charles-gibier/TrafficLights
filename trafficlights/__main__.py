"""Module de lancement de l'application."""

# remove dot for inline debugging
from .app import Application


def main() -> None:
    """Point d'entrée principal de l'application."""
    application = Application()
    application.start()


if __name__ == "__main__":
    main()
