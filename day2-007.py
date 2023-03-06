#Create any two-dimensional NumPy array of the shape (2,6) and int32 type and assign it to variable named arr.

import numpy as np

arr = np.array([[4, 5, 67, 8, 2, 4], [4, 2, 5, 7, 2, 5]], dtype='int32')

#Le code crée un array numpy à deux dimensions appelé arr qui contient deux lignes et six colonnes.
# Les valeurs de l'array sont des nombres entiers spécifiés entre crochets et séparés par des virgules.
# Le type de données pour les éléments de l'array est spécifié à l'aide de l'argument dtype qui est égal à 'int32'.
#La spécification dtype='int32' indique que chaque élément de l'array doit être stocké comme un entier signé sur 32 bits.
# Cela peut être utile lorsque la précision est importante et que les valeurs de l'array sont relativement grandes ou peuvent être négatives.
# Notez que le type de données par défaut pour les éléments de l'array numpy est 'float64'.