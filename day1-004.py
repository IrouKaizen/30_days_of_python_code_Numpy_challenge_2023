#Using NumPy, create a one-dimensional array of all two-digit numbers, assign it to a variable named arr and print this array to the console as shown below.

import numpy as np

arr = np.arange(10, 100)
print(arr)

#Expected output:

#[10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
# 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57
# 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
# 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99]

#Tip: Use the np.arange() function.

#La fonction np.arange() est une fonction de NumPy qui génère un tableau de valeurs de manière séquentielle. La syntaxe de base de la fonction est la suivante :

#"python
#Copy code
#np.arange(start, stop, step)
#start : la valeur de départ de la séquence
#stop : la valeur d'arrêt de la séquence (non incluse)
#step : l'incrément entre chaque valeur de la séquence
#Dans le cas de notre exercice, nous avons simplement utilisé la fonction np.arange(10, 100), car nous voulions créer une séquence de nombres de 10 à 99 avec un incrément par défaut de 1. Cette séquence est stockée dans la variable arr.

#Ensuite, nous avons utilisé la fonction print() pour afficher le tableau arr dans la console.

#J'espère que cela vous aide à comprendre le code !