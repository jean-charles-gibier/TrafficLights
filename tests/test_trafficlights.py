import unittest
from trafficlights.trafficlight import Trafficlight


class MyTestTrafficlights(unittest.TestCase):
    def test_simple_instance(self):
        # Test "Créer un nouveau feu dans un état spécifié"
        traffic = Trafficlight("UK", current="rouge")
        # Test "Connaître l'état du feu"
        self.assertEqual(traffic.get_current(), "rouge")
        # ajout des états & transitions UK
        traffic.add("next", "rouge", "rouge_et_jaune")
        traffic.add("next", "rouge_et_jaune", "vert")
        traffic.add("next", "vert", "jaune")
        traffic.add("next", "jaune", "rouge")

        # Test "Passer le feu au prochain état de la séquence"
        traffic.next()
        # on doit passer de rouge à "rouge_et_jaune"
        self.assertEqual(traffic.get_current(), "rouge_et_jaune")

        # prochaine séquence (cas nominal passant)
        traffic.set_current("vert")
        self.assertEqual(traffic.get_current(), "vert")

        # forcer la prochaine séquence (cas d'erreur)
        traffic.set_current("rouge")
        # la valeur est restée la même
        self.assertEqual(traffic.get_current(), "vert")


if __name__ == "__main__":
    unittest.main()
