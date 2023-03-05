#The following array is given:



#arr = np.array(
    #[
 #       [4.99, 3.49, 9.99],
 #       [1.99, 9.99, 14.99],
 #       [14.99, 2.39, 7.29],
 #   ]
#)


#Using NumPy, create an array of the same shape and data type as the given array and fill it with zeros. In response, print this array to the console.

import numpy as np

arr = np.array(
    [
        [4.99, 3.49, 9.99],
        [1.99, 9.99, 14.99],
        [14.99, 2.39, 7.29],
    ]
)

zeros_arr = np.zeros_like(arr)

print(zeros_arr)

#Nous importons tout d'abord la bibliothèque NumPy en utilisant la commande import numpy as np.
#Le tableau donné est défini et affecté à arr.
#Pour créer un tableau de même forme et même type que arr, nous utilisons la fonction np.zeros_like(arr) qui retourne un nouveau tableau de même forme et même type que arr, rempli de zéros.
#Finalement, le tableau résultant rempli de zéros est affiché à l'aide de la fonction print().