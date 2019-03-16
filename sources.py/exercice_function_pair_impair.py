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
nombre_encode = input("Encodez un nombre :")
parite = estPair(nombre_encode)
if parite == True:
    print(nombre_encode,"est pair !")
else:
    print(nombre_encode,"est impair !")

