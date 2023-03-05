import numpy as np

arr = np.zeros(shape=(6, 6), dtype='int')
arr[::2, ::2] = 2
arr[1::2, ::2] = 4

print(arr)

#Le code crée un tableau de numpy de dimension 6x6 rempli de zéros, avec le type de données entier.

#La première instruction arr[::2, ::2] = 2 affecte la valeur 2 à tous les éléments du tableau qui sont situés aux indices pairs, à la fois pour les rangées et les colonnes. Cela se fait en utilisant la notation ::2 pour les deux indices, ce qui signifie qu'on prend tous les éléments avec un pas de 2, à partir de l'indice 0.

#La deuxième instruction arr[1::2, ::2] = 4 affecte la valeur 4 à tous les éléments du tableau qui sont situés aux indices impairs pour les rangées et pairs pour les colonnes. Cela se fait en utilisant la notation 1::2 pour l'indice de rangée, ce qui signifie qu'on prend tous les éléments avec un pas de 2, à partir de l'indice 1. Pour les colonnes, on utilise la même notation que précédemment (::2). Cela a pour effet de créer des bandes alternées de valeurs 2 et 4 sur les rangées paires et impaires respectivement.

#Enfin, le tableau modifié est affiché à l'aide de la fonction print().