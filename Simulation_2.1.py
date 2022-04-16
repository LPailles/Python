# coding=utf-8

import os
import itertools #pour les permutations

#Cette fonction déplace l'oiseau num_oiseau et met à jour sa position dans la liste
def lance_graine (num_oiseau, liste_oiseau) :
    liste_oiseau_retour = []
    for o in liste_oiseau :
        liste_oiseau_retour.append(o)
    print ("\t\t\tOn lance la graine à l'oiseau " + str(num_oiseau) + " depuis la situation " + str(tuple(liste_oiseau_retour[1:-1])))
    #print("\t\t\t\tU" + str(num_oiseau - 1) + "=" + str(liste_oiseau_retour[num_oiseau-1]) + ",U" + str(num_oiseau) + "=" + str(liste_oiseau_retour[num_oiseau]) + ",U" + str(num_oiseau + 1) + "=" + str(liste_oiseau_retour[num_oiseau + 1]))
    #print("\t\t\t\tV" + str(num_oiseau) + "=" + str(liste_oiseau_retour[num_oiseau-1]) + "+" + str(liste_oiseau_retour[num_oiseau+1]) + "-" + str(liste_oiseau_retour[num_oiseau]) + "=" + str(liste_oiseau_retour[num_oiseau-1]+liste_oiseau_retour[num_oiseau+1]-liste_oiseau_retour[num_oiseau]))
    liste_oiseau_retour[num_oiseau]=liste_oiseau_retour[num_oiseau-1]+liste_oiseau_retour[num_oiseau+1]-liste_oiseau_retour[num_oiseau]
    print ("\t\t\t\tOn arrive à la situation " + str(tuple(liste_oiseau_retour[1:-1])))
    #print(liste_oiseau)
    #print(liste_oiseau_retour)
    #input()
    return liste_oiseau_retour



def construit_arbre (positions_depart,l_solutions) :
    arbre_sortie=[]
    for p in positions_depart :
        arbre_sortie.append(p)
    #print("Appel de construit_arbre(" + str(arbre_sortie) + ")")
    for oiseau in range(1,len(arbre_sortie) - 1) :
        #print("\tAppel de lance_graine(" + str(oiseau) + "," + str(arbre_sortie) + ")")
        position_finale=lance_graine(oiseau,arbre_sortie)
        if tuple(position_finale[1:-1]) not in l_solutions :
            print ("Ajout de " + str(position_finale[1:-1]) + " à la liste des solutions...")
            l_solutions.append(tuple(position_finale[1:-1]))
            construit_arbre(position_finale,l_solutions)
        #else:
        #    construit_arbre(position_finale,l_solutions)
    return position_finale

def main() :
    #On efface l'écran pour plus de clarté
    os.system('clear')

    #Saisie des valeurs initiales
    g_nb_oiseaux = input("Combien d'oiseaux ? : ")

    #Pas de max dans ce cas d'étude
    #max_fils = input("Combien de fils ? (-n..0..n) n=")

    #Un seul oiseau sur le fil 1
    #Les autres oiseaux sur le fil 0
    #On va placer le dernier oiseau sur le fil 1
    #Attention les listes commencent à 0 ...
    g_depart_oiseaux = [0]
    for o in range(int(g_nb_oiseaux) - 2) :
        g_depart_oiseaux.append(0)
    g_depart_oiseaux.append(1)
    #g_depart_oiseaux.append(0)
    print(g_depart_oiseaux)
    #On génère toutes les permutations possibles
    g_permutations = list(itertools.permutations(g_depart_oiseaux))

    #Comme plusieurs oiseaux peuvent se trouver sur le fil 0
    #On peut avoir des doublons, on les supprime
    g_permutations_oiseaux = list(dict.fromkeys(g_permutations))
    print()
    print("Situations possibles de départ : " + str(g_permutations_oiseaux))
    print()

    #On initialise l'ensemble des solutions (mélodies) possibles
    solutions = []

    for position_initale in g_permutations_oiseaux :
        #On initialise les position U0 et Un+1 à 0 par convention
        g_oiseaux=[0]
        for p in position_initale :
            g_oiseaux.append(p)
        g_oiseaux.append(0)
        #La situation de départ est une solution possible, on l'ajoute si
        #elle n'a pas déjà été inscrite précedemment
        if tuple(g_oiseaux[1:-1]) not in solutions :
            print ("Ajout de " + str(g_oiseaux[1:-1]) + " à la liste des solutions...")
            solutions.append(tuple(g_oiseaux[1:-1]))
        construit_arbre(g_oiseaux,solutions)


        #o = 1
        #while o <= int(g_nb_oiseaux) :
        #    g_oiseaux_temp = g_oiseaux
        #    print("***Situation de départ : " + str(g_oiseaux_temp[1:-1]))
        #    print("***On nourrit l'oiseau : " + str(o))
        #    g_proposition_solution = parcours_liste (o,g_oiseaux_temp,solutions)
        #    print(g_proposition_solution)
        #    o += 1

        #print("Appel depuis main de construit_arbre(" + str(g_oiseaux) + ")")
        #melodie=construit_arbre(g_oiseaux)
        #print(melodie)
    melodies = list(dict.fromkeys(solutions))
    print("Il y a " + str(len(melodies)) + " solutions :")
    print(melodies)


main()
