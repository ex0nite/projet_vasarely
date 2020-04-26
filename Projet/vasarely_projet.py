# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Boris Pitticco"
__version__ = "1.0"
__credits__ = ["Sébastien Hoarau", "Thierry Massart"]
__maintainer__ = "Boris Pitticco"
__email__ = "pitticco.boris@protonmail.com"

import math
import turtle as turt
import random
import time
import uuid

"""
Projet Vasarely
Auteur : ex0nite
Date : 26.04.2020

Le but du programme est de réaliser une oeuvre à la Victor Vasarely. 

Entrées : paramètres saisis par l'utilisateur. 
Sortie : caneva 

Programme réalisé dans le cadre du Mooc "Apprendre à coder avec Python"
"""

title = "  ..........................................................................\n" + \
        "  ..........................................................................\n" + \
        "  ..██████╗.██████╗..██████╗......██╗███████╗████████╗......................\n" + \
        "  ..██╔══██╗██╔══██╗██╔═══██╗.....██║██╔════╝╚══██╔══╝......................\n" + \
        "  ..██████╔╝██████╔╝██║...██║.....██║█████╗.....██║.........................\n" + \
        "  ..██╔═══╝.██╔══██╗██║...██║██...██║██╔══╝.....██║.........................\n" + \
        "  ..██║.....██║..██║╚██████╔╝╚█████╔╝███████╗...██║.........................\n" + \
        "  ..╚═╝.....╚═╝..╚═╝.╚═════╝..╚════╝.╚══════╝...╚═╝.........................\n" + \
        "  ..........................................................................\n" + \
        "  ..██╗...██╗.█████╗.███████╗.█████╗.██████╗.███████╗██╗..██╗...██╗.........\n" + \
        "  ..██║...██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██║..╚██╗.██╔╝.........\n" + \
        "  ..██║...██║███████║███████╗███████║██████╔╝█████╗..██║...╚████╔╝..........\n" + \
        "  ..╚██╗.██╔╝██╔══██║╚════██║██╔══██║██╔══██╗██╔══╝..██║....╚██╔╝...........\n" + \
        "  ...╚████╔╝.██║..██║███████║██║..██║██║..██║███████╗███████╗██║............\n" + \
        "  ....╚═══╝..╚═╝..╚═╝╚══════╝╚═╝..╚═╝╚═╝..╚═╝╚══════╝╚══════╝╚═╝............\n" + \
        "  ..........................................................................\n"

projet = "  ....Projet Vasarely.......................................................\n" + \
         "  ....Auteur : ex0nite......................................................\n" + \
         "  ....Date : 26.04.2020.....................................................\n" + \
         "  ..........................................................................\n" + \
         "  ....Le but du programme est de réaliser une oeuvre à la Victor Vasarely...\n" + \
         "  ..........................................................................\n" + \
         "  ....Entrées : paramètres saisis par l'utilisateur.........................\n" + \
         "  ....Sortie : caneva.......................................................\n" + \
         "  ..........................................................................\n" + \
         "  ....Programme réalisé dans le cadre du Mooc : ............................\n" + \
         "  ........\"Apprendre à coder avec Python\"...................................\n" + \
         "  ..........................................................................\n"

txt_turt = "  ..........................................................................\n" + \
           "  ............La démo va démarrer dans quelques instants !..................\n" + \
           "  ..........................................................................\n"


def banner_generated():
    print(title, end='')
    print(projet)


def return_banner():
    return title


def return_proj():
    return projet


def return_text():
    return txt_turt

def pavage(ig, sd, lg, col, centre, rayon):
    """
    :param ig: coin bas gauche du pavage
    :type ig: tuple
    :param sd: coin haut droit du pavage
    :type sd: tuple
    :param lg: longueur d'un hexagone
    :type lg: int
    :param col: couleurs
    :type col: tuple
    :param centre: coord. du centre de la déformation
    :type centre: tuple
    :param rayon: rayon de la zone de déformation
    :type rayon: int

    :return: 1 pour continuer main() (sauvegarde)
    """
    # numérotation des lignes
    lig = 1
    # variable de position de turt
    pos_t = [turt.xcor(), turt.ycor()]
    # tant qu'on est pas arrivé en haut
    while pos_t[1] <= sd[1]:
        # tant qu'on est pas arrivé au bord
        while pos_t[0] <= sd[0]:
            # on envoie un hexagone, gars
            hexagone(pos_t, lg, col, centre, rayon)
            pos_t[0] = pos_t[0] + lg * 3
        # incrémentation de lig
        lig += 1
        # on monte d'une ligne
        pos_t[1] = pos_t[1] + lg * math.cos(30 * math.pi / 180)
        # positionnement en ligne paire
        if lig % 2 == 0:
            pos_t[0] = ig[0] + 1.5 * longueur
        # positionnement en ligne impaire
        else:
            pos_t[0] = ig[0]
    return 1


def pos_log(c, longueur):
    """
    :param c: coordonnées de base de l'hexagone
    :type c: tuple
    :param longueur: longueur d'un segment d'un losange composant l'hexagone
    :type longueur: int
    :return: liste de tuple
    """
    p1 = (c[0] + longueur, c[1])
    p2 = (c[0] + longueur * math.cos(math.pi / 3), c[1] + longueur * math.sin(math.pi / 3))
    p3 = (c[0] - longueur * math.cos(math.pi / 3), c[1] + longueur * math.sin(math.pi / 3))
    p4 = (c[0] - longueur, c[1])
    p5 = (c[0] - longueur * math.cos(math.pi / 3), c[1] - longueur * math.sin(math.pi / 3))
    p6 = (c[0] + longueur * math.cos(math.pi / 3), c[1] - longueur * math.sin(math.pi / 3))
    p7 = (c[0] + longueur, c[1])
    return [p1, p2, p3, p4, p5, p6, p7]


def hexagone(pt, lg, col, cen, r):
    """
    :param pt: coordonnées de base de l'hexa
    :type pt: tuple
    :param lg: distance entre pt et un sommet de l'hexagone
    :type lg: int
    :param col: tuple, couleurs des hexagones
    :type col: liste de str
    :param cen:  tuple, centre de la sphere de deformation
    :type cen: tuple de int
    :param r: rayon de la sphere de déformation
    :type r: int
    :return: none
    """
    turt.up()
    list = pos_log(pt, longueur)
    turt.speed("fastest")

    c_x = int(cen[0])
    c_y = int(cen[1])
    c_z = int(cen[2])
    # on déforme les coordonées du point de base
    pt_base = deformation((pt[0], pt[1], 0), (c_x, c_y, c_z), r)
    # on se déplace aux coordonées déformées
    #turt.goto(pt_base[0], pt_base[1])

    # un hexa est composé de 3 losanges
    for i in range(3):
        turt.goto(pt_base[0], pt_base[1])
        turt.color(col[i])
        turt.begin_fill()
        # on parcours la liste de points, le décalage est utilisé pour récupérer les bonnes coordonnées
        for pos in list[i * 2:i * 2 + 3]:
            p = deformation((pos[0], pos[1], 0), cen, r)
            turt.goto(p[0], p[1])
        turt.goto(pt_base[0], pt_base[1])
        turt.end_fill()
    turt.down()


def deformation(p, c, rayon):
    """ Calcul des coordonnées d'un point suite à la déformation
        engendrée par la sphère émergeante
        Entrées :
          p : coordonnées (x, y, z) du point du dalage à tracer
             (z = 0) AVANT déformation
          centre : coordonnées (X0, Y0, Z0) du centre de la sphère
          rayon : rayon de la sphère
        Sorties : coordonnées (xprim, yprim, zprim) du point du dallage
             à tracer APRÈS déformation
    """
    x, y, z = p
    xprim, yprim, zprim = x, y, z
    xc, yc, zc = int(c[0]), int(c[1]), int(c[2])

    if rayon ** 2 > zc ** 2:
        zc = zc if zc <= 0 else -zc
        r = math.sqrt((x - xc) ** 2 + (y - yc) ** 2)  # distance horizontale
        # depuis le point à dessiner jusqu'à l'axe de la sphère
        rayon_emerge = math.sqrt(rayon ** 2 - zc ** 2)  # rayon de la partie
        # émergée de la sphère
        rprim = rayon * math.sin(math.acos(-zc / rayon) * r / rayon_emerge)
        if 0 < r <= rayon_emerge:  # calcul de la déformation
            # dans les autres cas
            xprim = xc + (x - xc) * rprim / r  # les nouvelles coordonnées
            # sont proportionnelles aux anciennes
            yprim = yc + (y - yc) * rprim / r
        if r <= rayon_emerge:
            beta = math.asin(rprim / rayon)
            zprim = zc + rayon * math.cos(beta)
            if int(c[2]) > 0:
                zprim = -zprim

    return xprim, yprim, zprim


def random_color(nb):
    """
    :param nb: nombre de couleur à selectionner
    :return: tuple de nb couleurs randomisées
    """
    colors = ["ghost white", "white smoke", "gainsboro", "floral white", "old lace", "antique white",
              "papaya whip", "blanched almond", "bisque", "peach puff", "navajo white", "moccasin", "cornsilk", "ivory",
              "lemon chiffon", "seashell", "honeydew", "mint cream", "azure", "alice blue", "lavender",
              "lavender blush", "misty rose", "white", "black", "dark slate gray", "dim gray", "slate gray",
              "light slate gray", "gray", "light grey", "midnight blue", "navy", "cornflower blue", "dark slate blue",
              "slate blue", "medium slate blue", "light slate blue", "medium blue", "royal blue", "blue", "dodger blue",
              "deep sky blue", "sky blue", "light sky blue", "steel blue", "light steel blue", "light blue",
              "powder blue", "pale turquoise", "dark turquoise", "medium turquoise", "turquoise", "cyan", "light cyan",
              "cadet blue", "medium aquamarine", "aquamarine", "dark green", "dark olive green", "dark sea green",
              "sea green", "medium sea green", "light sea green", "pale green", "spring green", "lawn green", "green",
              "chartreuse", "medium spring green", "green yellow"]
    col = []
    i = 0
    while i < nb:
        c = random.choice(colors)
        if c in col:
            pass
        else:
            col.append(c)  # Choose a random color
            i+=1

    return col


if __name__ == "__main__":
    # -> https://stackoverflow.com/questions/419163/what-does-if-name-main-do

    # ask permet de passer du mode "debug" (paramètre automatique) au mode "user" (demande des paramètres en console)
    ask = False

    # sauvegarder l'image ?
    save = False

    # PARTIE CONSOLE
    banner_generated()

    if ask:
        # coin inférieur gauche
        print("Coin inférieur gauche\n\t Avec x = y ")
        ig_x = ig_y = int(input("\t x: "))
        ig = (ig_x, ig_y)

        # coin sup droit
        print("Coin supérieur droit\n\t Avec x = y ")
        sd_x = sd_y = int(input("\t x: "))
        sd = (sd_x, sd_y)

        # longueur du segment de pavage
        longueur = int(input("Longueur du pavage : "))

        # couleur (en mode texte)
        input_string = input("Indiquez 3 couleurs en respectant les consignes suivantes :\n"
                             "\t- Les couleurs doivent être en anglais,\n"
                             "\t- Séparées par une virgule,\n"
                             "\t- Pas d'espaces après les virgules,\n"
                             "\t- Faites entrer à la fin :\n"
                             "\t- Exemple : \"black,red,blue\"\n"
                             "\t- Taper \"random\" pour des couleurs aléatoires\n"
                             "\t- Couleurs : ")
        if input_string == "random":
            col = random_color(3)
        else:
            col = input_string.replace(" ", " ").split(",")
        print(col)

        # coordonnées du centre de la sphere de déformation
        input_string = input("Indiquez 3 coordonnées en respectant les consignes suivantes :\n"
                             "\t- Ordre = abs, ordonnées, hauteur\n"
                             "\t- Integer seulement,\n"
                             "\t- Pas d'espaces après les virgules,\n"
                             "\t- Faites entrer à la fin :\n"
                             "\t- Exemple : \"50,-50,-50\"\n"
                             "\t- Valeurs : ")
        ct_def = input_string.replace(" ", " ").split(",")
        print(ct_def)

        # rayon de la sphere de déformation
        r = int(input("rayon de la sphere de déformation :"))

        # demande si sauvegarde de l'image finale ?
        save_input = input("Voulez vous sauvegarder l'image finale ? (o/n):")
        if save_input == 'o':
            save = True
        else:
            save = False

    else:
        ig_x = ig_y = random.randint(-400, -200)
        ig = (ig_x, ig_y)
        sd_x = sd_y = -ig_x
        sd = (sd_x, sd_y)
        longueur = random.randint(10, 50)
        col = random_color(3)
        ct_def = [random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)]
        r = random.randint(100, 300)
        save = True

    # PARTIE TURTLE
    SCREEN_X = 400
    SCREEN_Y = 400

    turt.up()

    # Présentation du projet
    turt.goto(-400, 100)
    turt.write(return_banner(), font=("Courier New", 12, "normal"))
    turt.goto(-400, -120)
    turt.write(return_proj(), font=("Courier New", 12, "normal"))
    turt.goto(-400, -285)
    turt.write(return_text(), font=("Courier New", 12, "normal"))

    # On attends 5 secondes puis on clean puis pavage
    turt.ontimer(lambda: turt.clearscreen(), 800)
    time.sleep(1)

    # Screen
    turt.title("Projet Vasarely")
    turt.screensize(SCREEN_X, SCREEN_Y)
    turt.bgcolor('white')

    # Tortue
    turt.hideturtle()
    turt.speed("fastest")
    turt.up()

    # Console
    print("Paramètres retenus : ")
    print("Coin inférieur gauche : ", ig)
    print("Coin supérieur droit : ", sd)
    print("Longueur : ", longueur)
    print("Couleurs : ", col)
    print("Centre de la sphère : ", ct_def)
    print("Rayon de la sphère : ", r)
    print("Sauvegarde : ", save)

    # Pavage
    turt.goto(ig_x, ig_y)
    pavage(ig, sd, longueur, col, ct_def, r)

    # Sauvegarde
    if save:
        print("Sauvegarde en cours...")
        ts = turt.getscreen()
        filename = "img/Vasarely" + str(uuid.uuid4()) + ".eps"
        ts.getcanvas().postscript(file=filename)
        print("Sauvegarde effectuée !")

    # Une fois terminé, on attends un click pour fermer la fenetre
    turt.exitonclick()