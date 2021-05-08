"""Module implémentant des classes en relations avec le menu."""

from typing import Callable, Dict, List, Tuple, AnyStr


class Trafficlight:
    """Modélise un feu de circulation présentant un état lumineux donné.
    wrarn : la couleur affectée par défaut n'est pas validée par l'init
     autrement dit on peut initialiser avec une couleur inexistante dans le choix final """

    def __init__(self, name: str = "None", current: str = "rouge") -> None:
        """Initialise une instance de feu.
        Args:
            name: identifiant du feu courant
            current: etat par defaut
        """
        self._name: str = name
        self._current: str = current
        self._triggers: Dict = {}

    def add(self, trigger: AnyStr, source: AnyStr, dest: AnyStr) -> "Trafficlight":
        """Ajoute une transition entre 2  etats.

        Args:
            trigger: action déclenchant la transition,
            source: etat de départ,
            dest: etat d'arivee
        """
        trigger = trigger.lower().strip()
        source = source.lower().strip()
        self._triggers[trigger] = self._triggers.get(trigger, {})
        self._triggers[trigger][source] = dest
        return self

    def next(self, **args):
        """Recupere le prochain etat et appelle le renderer."""
        # vérification du choix de la couleur
        if "color" in args and self._triggers["next"][self._current] != args["color"]:
            print(
                "La couleur {} ne peut suivre la couleur {} ".format(
                    args["color"], self._current
                )
            )
            return getattr(self, "render"), args
        self._current = self._triggers["next"][self._current]
        return getattr(self, "render"), args

    def quitter(self, **args):
        """Quitte le parcours."""
        return None, None

    def __str__(self) -> str:
        """Formate le contenu de l'objet en vue de sa présentation à l'utilisateur."""
        lines: List[str] = [f"{self._name.title()}\t({self._current})\n"]
        for key, value in enumerate(self._triggers.keys()):
            lines.append(f"{key} - {value}")
        lines.append("Ou entrez la valeur en toutes lettres.")
        lines.append("")
        lines.append(">>> ")
        return "\n".join(lines)

    def render(self, **args) -> Tuple[Callable, Dict]:
        """Affiche le choix des triggers à l'utilisateur et attend la réponse de ce dernier.
        """
        entries: Dict = {
            str(key): value for (key, value) in enumerate(self._triggers.keys())
        }
        while True:
            choice = input(self).lower().strip()
            if choice in entries:
                return getattr(self, entries[choice]), {}
            elif choice in self._triggers["next"]:
                return getattr(self, "next"), {"color": choice}
            else:
                print("Erreur de saisie.")

    def get_current(self) -> str:
        """renvoie l'etat courant du feu.
        """
        return self._current

    def set_current(self, value: AnyStr):
        """ affecte l'etat courant du feu.
        """
        self.next(color=value)
