#  Traffic lights

Version minimaliste de FSM (automate à etats finis) modelisant le fonctionnement d'un feu de circulation.<br>
Note : Dans cette version il n'y a qu'un arc attribué à chaque tuple état / trigger, ce qui limite la modélisation mais suffit pour répondre aux exigences de l'exercice.

## Installation

1. Cloner ce dépôt de code avec `git clone https://github.com/jean-charles-gibier/TrafficLights.git`<br>
ou dezipper les source du livrable dans un répertoire nomé 'trafficlights'
1. Se rendre dans le projet avec `cd trafficlights`

Le projet est developpé sous Python 3.7, il est "stand alone" et ne nécessite pas de module additionnels.<br>
Créer un environement de developpement n'est pas exigé mais reste toujours conseillé.

## Démarrage
Macos et Linux: `python3 -m trafficlights`<br>
Windows: `py -m trafficlights`

## tests
Macos et Linux: `python3 -m pytest`<br>
Windows: `py -m pytest`

(Pour installer pytest : `sudo apt install python3-pytest`)

## exemple d'utilisation
```shell script
jcg@JCG-LNV:/mnt/d/work/trafficlights$ python3 -m trafficlights
Uk      (rouge)

0 - next
1 - quitter
Ou entrez la valeur en toutes lettres.

>>> 0
Uk      (rouge_et_jaune)

0 - next
1 - quitter
Ou entrez la valeur en toutes lettres.

>>> 0
Uk      (vert)

0 - next
1 - quitter
Ou entrez la valeur en toutes lettres.

>>> 0
Uk      (jaune)

0 - next
1 - quitter
Ou entrez la valeur en toutes lettres.

>>> rouge
Uk      (rouge)

0 - next
1 - quitter
Ou entrez la valeur en toutes lettres.

>>> jaune
La couleur jaune ne peut suivre la couleur rouge
Uk      (rouge)

0 - next
1 - quitter
Ou entrez la valeur en toutes lettres.

>>> 1
bye
```
