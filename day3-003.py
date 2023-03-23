#Ce code utilise la fonction "tile" de NumPy pour créer une matrice de dimensions (5,10) en répétant horizontalement le tableau unidimensionnel créé à l'aide de la fonction "arange" de NumPy.

#La fonction "arange" crée un tableau unidimensionnel de valeurs allant de 0 à 9 (10 valeurs au total), tandis que la fonction "tile" répète ce tableau 5 fois horizontalement (lignes) et 1 fois verticalement (colonnes), ce qui signifie que chaque ligne de la matrice aura les mêmes valeurs.

#Le résultat imprimé sur la console sera une matrice de dimensions (5,10), où chaque ligne sera identique et contiendra les nombres de 0 à 9.

import numpy as np

arr = np.tile(np.arange(10), (5, 1))

print(arr)