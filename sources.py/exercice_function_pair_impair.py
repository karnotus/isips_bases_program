#
# Author      : Laurent Deschryver <laurent.deschryver@protonmail.com>
# Date        : 16 mars 2019
# Fichier     : exercice_function_pair_impair.py
# Description : Exemple de script qui utilise une fonction qui détermine si un nombre
#               est pair ou impair.
#

# Fonction qui retourne True si le nombre passé comme paramètre est pair.
# False dans le cas contraire.
#
def estPair(nombre):
    if int(nombre)%2 == 0:
        return True
    else:
        return False

# Code principal
#

# L'utilisateur encode un nombre
nombre_encode = input("Encodez un nombre :")

# Appel de la fonction estPair avec le nombre encodé. Retour de True ou False.
parite = estPair(nombre_encode)

# Si le nombre est pair...
if parite == True:
    print(nombre_encode,"est pair !")

# Sinon...
else:
    print(nombre_encode,"est impair !")

