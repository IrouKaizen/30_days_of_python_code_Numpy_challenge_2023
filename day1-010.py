#À l'aide de NumPy, vous pouvez créer une matrice 2D de forme 10x10 qui a des zéros partout sauf sur la diagonale
# principale. Sur cette diagonale, les éléments sont les nombres entiers de 1 à 9. Pour ce faire,
# vous pouvez utiliser la fonction np.diag() de NumPy pour créer une matrice diagonale, puis vous pouvez utiliser
# la fonction np.zeros() pour créer une matrice remplie de zéros de la même forme et remplacer la diagonale par la
# matrice diagonale. Voici le code qui vous permettra de créer cette matrice :

import numpy as np

# Crée une matrice diagonale avec les nombres entiers de 1 à 9
diag_arr = np.diag(np.arange(1, 10))

# Crée une matrice remplie de zéros de la forme 10x10
zeros_arr = np.zeros((10, 10))

# Remplace la diagonale de la matrice remplie de zéros par la matrice diagonale
zeros_arr[np.arange(10), np.arange(10)] = diag_arr

# Affiche la matrice finale
print(zeros_arr)

#output

#[[0 0 0 0 0 0 0 0 0 0]
 #[0 1 0 0 0 0 0 0 0 0]
 #[0 0 2 0 0 0 0 0 0 0]
 #[0 0 0 3 0 0 0 0 0 0]
 #[0 0 0 0 4 0 0 0 0 0]
 #[0 0 0 0 0 5 0 0 0 0]
 #[0 0 0 0 0 0 6 0 0 0]
 #[0 0 0 0 0 0 0 7 0 0]
 #[0 0 0 0 0 0 0 0 8 0]
 #[0 0 0 0 0 0 0 0 0 9]]




