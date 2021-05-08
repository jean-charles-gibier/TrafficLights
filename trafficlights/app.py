"""Implémentation de l'application elle-même."""

from typing import Any, Dict, Tuple, Callable

# remove dot for inline debugging
from .trafficlight import Trafficlight
from .statemachine import SimpleStateMachine


class Application(SimpleStateMachine):
    """Représente une application implémentant un système de feux de circulation."""

    def __init__(self) -> None:
        super().__init__(self.handle_start)

    def handle_start(self) -> Tuple[Callable, Dict]:
        """ Fonction appelée au démarrage de l'application (injection).
            elle est stockée lors de son instanciation
            elle est lancée par la fonction "start" héritée.
        """
        # Version UK
        return (
            Trafficlight("UK")
            .add("next", "rouge", "rouge_et_jaune")
            .add("next", "rouge_et_jaune", "vert")
            .add("next", "vert", "jaune")
            .add("next", "jaune", "rouge")
            .add("quitter", "*", "quitter")
            .render()
        )

    # Version française
    #     return (
    #         Trafficlight("FR")
    #         .add("next", "rouge", "vert")
    #         .add("next", "vert", "jaune")
    #         .add("next", "jaune", "rouge")
    #         .add("quitter", "*", "quitter")
    #         .render()
