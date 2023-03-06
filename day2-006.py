import numpy as np

arr = np.array(
    [
        [False, True, True, False, True],
        [False, False, True, True, True],
    ]
)

arr = arr.astype('int')
print(arr)

#output
#array([[0, 1, 1, 0, 1],
#       [0, 0, 1, 1, 1]])


#La conversion de l'array de booléens en array d'entiers remplace False par 0 et True par 1.
#Cela peut être utile pour effectuer des opérations arithmétiques sur l'array ou pour afficher
#les données de manière plus claire.