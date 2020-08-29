# -*- coding: utf-8 -#-
#
# Auteur        : Cédric Kreis
# Programme     : ROT13
# Fonctions     : Converti les Majuscules en miniscules et chiffre en ROT13
# Créé le       : 12.11.2019
# Modifié le    :
# Version       : 1.3
# Python        : 2.7.16+
#
#-------------------------------------------------------------------------------

textecomplet = ""

#entree du texte
texte = raw_input("Insérer une lettre ou une phrase :\n")


min = texte.lower()


#boucle d’affichage des caracteres du texte
for i in range (0,len(min)):
    #print min[i]
    x = ord(min[i])

    if 97<=ord(min[i])<=122 :
        y = chr(((((x - 97) + 13) % 26) + 97))
        #print y
        textecomplet += y
    else :
        None

    #Inverse le texte
    #textecomplet = min[i] + textecomplet
    #print(min[i])

print textecomplet

#fermeture du programme
raw_input("Fin du programme")
