"""Module implémentant un exemple simpliste de machine à états."""
from typing import Callable, Dict


class SimpleStateMachine:
    """Représente une machine à états simple destinées à implémenter un
    parcours composé de declencheurs reliant 2 états."""

    def __init__(self, start_state: Callable) -> None:
        """Initialise une nouvelle machine à états."""
        self._next_state: Callable = start_state

    def start(self) -> None:
        """Démarre la machine à états."""
        args: Dict = {}
        while self._next_state:
            self._next_state, args = self._next_state(**args)
