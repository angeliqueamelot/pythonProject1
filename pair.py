# Exercice 1 Kata 1
from random import *

def pair(y):
    if y % 2 == 0:
        #print("VRAI")
        # garde la valeur en memoire
        return "VRAI"
    else:
        #print("FAUX") # juste pour vérifier si j'ai le bon output
        return "FAUX"

# pour lancer la fonction
pair(2)
z = []
z.append(pair(2))
print(z)

# pour l'ensemble sur une liste

def aleatoire():
    y = []
    for i in range(20):
        y.append(randint(0, 20))
    return y

print(aleatoire())

# essayer de boucler sur la liste pair en appelant 2 fonctions, en définissant une liste

aleatoire()
    for