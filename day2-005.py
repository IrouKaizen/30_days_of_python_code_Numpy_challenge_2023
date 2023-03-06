import numpy as np

arr = np.tri(6)
print(arr)

#La fonction np.tri() crée une matrice triangulaire inférieure avec des uns sur la diagonale principale et des zéros au-dessus.
# Par défaut, la fonction crée une matrice carrée avec une taille donnée en entrée (ici 6).

#Notez que np.tri() peut également prendre un deuxième argument optionnel k qui spécifie l'indice de la diagonale pour laquelle les valeurs sont égales à 1.
#Par exemple, k=1 produirait une matrice triangulaire supérieure avec des uns sur la diagonale et au-dessus.