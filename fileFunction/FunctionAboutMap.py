# import des fichiers
import fileFunction.variableMap as variableMap
import fileFunction.FunctionAboutBag as FBag
import fileFunction.FunctionAboutMap as FMap
import fileFunction.FunctionPrint as FPrint
import fileFunction.variableClassic as VarC
import fileFunction.FunctionGame as FGame
import os
clear = lambda: os.system('cls')

# fonction pour verifier que le deplacement est possible
def checkDeplacement(y, x, deplacement, mapBinaire):
    # je modifie la position par rapport au deplacement
    if deplacement == "z":
        y = y - 1
    elif deplacement == "s":
        y = y + 1
    elif deplacement == "q":
        x = x - 1
    elif deplacement == "d":
        x = x + 1
    # je recupere la position du joueur et je verifie que c'est un 1 et pas un 0
    var = mapBinaire[y][x]

    if mapBinaire[y][x] == "1":
        return "ok"
    else:
        return "ko"

# fonction qui vas verifier si le joueur est sur un item
def checkItemPosition(playerX, playerY, listItems):

    result = None
    for index in listItems:
        pointer = 2
        while pointer < len(index):
            if index[pointer] == playerX and index[pointer + 1] == playerY:
                result = index[0]
            pointer += 2
    return result

# fonction pour imprimer la map
def printMap (y, x, map1):
    # compteur1 represente l'axe Y
    compteur1 = 0
    print()
    while compteur1 < len(map1):
    # compteur1 represente l'axe X
        compteur2 = 0
        # je reinitialise ma var ligne qui represente la ligne en cours d'impression
        ligne = ""
        while compteur2 < len(map1[0]):
            # si le caractere actuel est a la coordoné de l'avatar alor je print l'avatar
            if compteur1 == y and compteur2 == x:
                ligne = str(ligne) + VarC.avatar
            else:
                # je verifie et si oui j'ajoute la couleur
                if str(map1[compteur1][compteur2]) == "*":
                    ligne = f"{ligne}\033[33m{map1[compteur1][compteur2]}\033[0m"
                elif str(map1[compteur1][compteur2]) == "~":
                    ligne = f"{ligne}\033[36m{map1[compteur1][compteur2]}\033[0m"
                elif str(map1[compteur1][compteur2]) == "█":
                    ligne = f"{ligne}\033[31m{map1[compteur1][compteur2]}\033[0m"
                elif str(map1[compteur1][compteur2]) == "M":
                    ligne = f"{ligne}\033[35m{map1[compteur1][compteur2]}\033[0m"
                elif str(map1[compteur1][compteur2]) == "♣":
                    ligne = f"{ligne}\033[32m{map1[compteur1][compteur2]}\033[0m"
                else:
                    ligne = str(ligne) + str(map1[compteur1][compteur2])
            compteur2 = compteur2 + 1
        compteur1 = compteur1 + 1
        # j'imprime les lignes une a une
        print(ligne)
    print()
    print()

# fonction qui permet de dormier
def sleepHour(nbHeure, statSommeil, statSoif, statFaim):
    statSommeil = statSommeil + nbHeure * 6
    if statSommeil > 100:
        statSommeil = 100
    statFaim = statFaim - nbHeure * 1
    statSoif = statSoif - nbHeure * 2
    return statSommeil, statFaim, statSoif

# ajouter les item dans la carte
def addItemPointOnMap(map1, items):
    for index in items:
        positionItemsIndex = 2
        while positionItemsIndex < (len(index) - 2):
            if index[positionItemsIndex + 1] > 0 and index[positionItemsIndex] > 0:
                map1[index[positionItemsIndex + 1]][index[positionItemsIndex]] = "."
            else:
                map1[index[abs(positionItemsIndex) + 1]][index[abs(positionItemsIndex)]] = " "
            positionItemsIndex += 2
    return map1

# fonction fin de tour qui imprime la carte et les stats
def endTurn():
    clear()
    FMap.printMap(VarC.positionJoueurY, VarC.positionJoueurX, variableMap.mapInATab)
    print(f"Votre action précedentes était de : {VarC.prevMoove}")
    FBag.intoMyBag(VarC.sac, VarC.limitSac)
    print(f"{VarC.nomJoueur} voici vos stat, faim = {VarC.statFaim}, soif = {VarC.statSoif}, sommeil = {VarC.statSommeil}")