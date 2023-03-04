
import numpy as np

arr = np.arange(10, 100).reshape(9, 10)
print(arr)

#Tout d'abord, nous avons importé le module NumPy avec l'instruction import numpy as np. Cela nous permet d'utiliser les fonctions et les tableaux de NumPy dans notre code.

#Ensuite, nous avons créé un tableau en utilisant la fonction np.arange(10, 100). Cela génère une séquence de nombres de 10 à 99 (inclus), que nous avons stockée dans la variable arr.

#Enfin, nous avons utilisé la méthode reshape() de NumPy pour changer la forme de arr en une matrice de 9 lignes et 10 colonnes. Nous avons passé ces dimensions à reshape() sous forme de tuple (9, 10). Nous avons ensuite imprimé cette matrice à la console en utilisant la fonction print().

#J'espère que cela vous aide à comprendre le code !


#Solution II:

import numpy as np

arr = np.arange(10, 100).reshape(9, 10)
print(arr)


#Solution III:

import numpy as np

arr = np.arange(10, 100).reshape(9, -1)
print(arr)