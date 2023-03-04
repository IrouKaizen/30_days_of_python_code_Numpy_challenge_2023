import numpy as np

arr = np.array(
    [
        ['4', '3', '6', '2', '1'],
        ['7', '2', '1', '2', '6'],
    ],
    dtype='<U1',
)

arr = arr.astype('float16')

print(arr)

#Dans cet exercice, nous avons un tableau NumPy avec des chaînes de caractères comme données. Le tableau est défini comme suit :

#arr = np.array(
#    [
#        ['4', '3', '6', '2', '1'],
#        ['7', '2', '1', '2', '6'],
#    ],
#    dtype='<U1',
#)
#Nous voulons changer le type de données du tableau de <U1 (chaîne de caractères unicode de longueur 1) à float16 (nombre flottant sur 16 bits). Pour cela, nous allons utiliser la méthode astype() de NumPy :
#    arr = arr.astype('float16')
#Maintenant, le tableau arr contient les mêmes données, mais avec un type de données différent. Enfin, pour vérifier que le changement de type a bien eu lieu, nous allons imprimer le tableau :

#print(arr)
#Le résultat attendu est :

#[[4. 3. 6. 2. 1.]
#[7. 2. 1. 2. 6.]]
#Ce tableau a maintenant des nombres flottants au lieu de chaînes de caractères.