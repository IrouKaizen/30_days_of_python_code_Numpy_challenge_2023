#Ce code Python utilise le module NumPy pour créer un tableau de valeurs à partir d'une liste de listes, puis convertit la liste en un objet NumPy Array en utilisant la fonction np.asarray(). Enfin, il affiche le tableau NumPy créé à l'aide de la fonction print().

#Plus précisément, ce code crée une liste rates qui contient deux sous-listes, chacune contenant six nombres décimaux. Ensuite, le code utilise la fonction np.asarray() pour créer un objet NumPy Array arr à partir de cette liste de listes.

#Enfin, le code affiche le contenu de arr en utilisant la fonction print(). Le résultat est un tableau NumPy avec deux lignes et six colonnes, où chaque élément est un nombre décimal.

import numpy as np

rates = [
    [1.97, 1.04, 1.35, 2.17, 2.29, 4.38],
    [1.34, 2.04, 1.37, 2.09, 1.29, 3.38],
]

arr = np.asarray(rates)
print(arr)