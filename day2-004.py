import numpy as np

A = np.array(
    [
        [4.99, 3.49, 9.99],
        [1.99, 9.99, 14.99],
        [14.99, 2.39, 7.29],
    ]
)

B = np.full_like(A, 9.99)

print(B)

#Ici, np.full_like(A, 9.99) crée un nouvel array de la même forme et du même type que A,
# mais avec toutes les valeurs remplacées par la constante 9.99.