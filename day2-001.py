import numpy as np

# create the original array
arr = np.ones((4, 4), dtype=np.int32)

# add zeros around the original array
arr_pad = np.pad(arr, pad_width=1, mode='constant', constant_values=0)

# fill the center with the value of 5
arr_pad[1:-1, 1:-1] = 5

# print the resulting array
print(arr_pad)

#La première ligne crée le tableau d'origine avec np.ones((4, 4), dtype=np.int32). Cette ligne crée un tableau 4x4 rempli de 1 avec un type entier.

#Ensuite, nous avons ajouté des zéros autour de la matrice d'origine en utilisant np.pad(). Le premier argument est le tableau d'origine, le deuxième argument est la largeur du tampon que nous voulons ajouter à chaque bordure, et le troisième argument est le mode de remplissage pour les valeurs ajoutées (dans ce cas, nous utilisons le mode 'constant' pour ajouter des zéros). Le quatrième argument spécifie la valeur constante à ajouter, qui est de 0 dans ce cas.

#Après avoir ajouté des zéros autour de la matrice d'origine, nous avons rempli la zone centrale de la matrice avec des 5 en utilisant la ligne arr_pad[1:-1, 1:-1] = 5. Cette ligne accède à toutes les cases de la matrice arr_pad à l'exception des bords et leur assigne la valeur de 5.

#Enfin, nous avons imprimé le tableau résultant avec print(arr_pad) pour afficher le résultat final.





