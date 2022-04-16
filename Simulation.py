# coding=utf-8

import os
import itertools

#Cette fonction déplace l'oiseau num_oiseau et met à jour sa position dans la liste
def lance_graine (num_oiseau, liste_oiseau) :
    liste_oiseau[num_oiseau]=liste_oiseau[num_oiseau-1]+liste_oiseau[num_oiseau+1]-liste_oiseau[num_oiseau]
    return liste_oiseau

#Cette fonction lance une graine à un oiseau de la liste
def parcours_liste (l_o,l_oiseaux,l_solutions) :
    boucle = 1
    while boucle  == 1 :
        l_oiseaux = lance_graine(l_o,l_oiseaux)
        if l_oiseaux[1:-1] not in l_solutions :
            print "Ajout de "+str(l_oiseaux[1:-1])+" à la liste des solutions..."
            l_solutions.append(l_oiseaux[1:-1])
        else :
            print "La solution "+str(l_oiseaux[1:-1])+" existe déjà !"
            boucle = 0
    return l_solutions

#On efface l'écran pour plus de clarté
os.system('clear')

quit()

#Saisie des valeurs initiales
nb_oiseaux = input("Combien d'oiseaux ? : ")
max_fils = input("Combien de fils ? (-n..0..n) n=")

#On place les oiseaux sur les fils
#La premiere valeur est =0 par définition
oiseaux = [0]
for oiseau in range(nb_oiseaux) :
    fil_oiseau = input("Position de l'oiseau "+str(oiseau+1)+" : ")
    oiseaux.append(fil_oiseau)
#La derniere valeur est =0 par définition
oiseaux.append(0)

#Affichage de debug
#print("Positions U des oiseaux : " + str(oiseaux) + " (Par convention, U0 et U" + str(nb_oiseaux+1) + " sont nuls)")
print("Position des oiseaux : " + str(oiseaux[1:-1]))

#On initialise la liste des solutions possible avec les positions initiales
solutions = []
solutions.append(oiseaux[1:-1])
for hirondelle in range(nb_oiseaux) :
    parcours_liste(hirondelle+1,oiseaux,solutions)
print
print
print solutions
