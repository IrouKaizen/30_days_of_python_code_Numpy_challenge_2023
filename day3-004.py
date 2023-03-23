#Ce code crée un tableau NumPy "arr" à trois dimensions contenant deux matrices de dimensions (3,6). Chaque matrice contient des nombres entiers.

#Ensuite, la fonction "np.ones_like" de NumPy est utilisée pour créer un tableau NumPy "result" de la même forme et de la même taille que "arr", où chaque élément est initialisé à 1.

#Enfin, le tableau NumPy "result" est imprimé sur la console. Le résultat affiché sera une matrice de dimensions (2,3,6) contenant uniquement des 1 dans chaque élément.

import numpy as np

arr = np.array(
    [
        [[3, 2, 4, 0, 1, 3], [5, 0, 4, 4, 4, 1], [3, 2, 4, 1, 1, 4]],
        [[5, 5, 4, 5, 1, 3], [2, 2, 5, 2, 4, 0], [5, 1, 3, 4, 2, 3]],
    ]
)

result = np.ones_like(arr)
print(result)