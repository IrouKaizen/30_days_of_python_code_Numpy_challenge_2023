#Expected output:
#[['30' 'Days' 'of' 'Python']
#['Code' '-' 'Numpy' 'Challange']]

import numpy as np

title = '30 Days of Python Code - Numpy Challange'
tokens = title.split(' ')
arr = np.asarray(tokens).reshape(2, -1)

print(arr)

#Ce code divise la chaîne de caractères "title" en une liste de mots individuels
#en utilisant l'espace comme délimiteur à l'aide de la méthode "split" de Python.
#Ensuite, il convertit cette liste en un tableau NumPy à deux dimensions
#en utilisant la fonction "np.asarray" de NumPy et en redimensionnant le tableau
#en deux lignes avec autant de colonnes que nécessaire en utilisant "-1" pour que
#a taille soit automatiquement calculée. Le tableau résultant "arr" a donc une forme
#de (2, n) où "n" est le nombre de mots dans la chaîne de caractères "title".
#Enfin, il imprime le tableau NumPy "arr" sur la console.