# import des fichiers
import fileFunction.variableMap as VarM
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

    # if mapBinaire[y][x] == " " or mapBinaire[y][x] == "." :
    if mapBinaire[y][x] in VarM.slotMoove:
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
                if str(map1[compteur1][compteur2]) in VarM.ItemCouleur:
                    color = VarM.couleurItem[str(map1[compteur1][compteur2])]
                    ligne = f"{ligne}{color}"
                else:
                    ligne = f"{ligne}{map1[compteur1][compteur2]}"
            compteur2 = compteur2 + 1
        compteur1 = compteur1 + 1
        # j'imprime les lignes une a une
        print(ligne)
    print()
    print()

# fonction qui permet de dormir
def sleepHour(nbHeure, statSommeil, statSoif, statFaim):
    statSommeil = statSommeil + nbHeure * 6

    if statSommeil > int(VarC.maxSommeil):
        statSommeil = VarC.maxSommeil
    statFaim = statFaim - nbHeure * 1
    statSoif = statSoif - nbHeure * 2
    return statSommeil, statFaim, statSoif

# ajouter les item dans la carte
def addItemPointOnMap(map1, items):
    for index in items:
        positionItemsIndex = 2
        while positionItemsIndex < (len(index) - 2):
            index[positionItemsIndex] = int(index[positionItemsIndex])
            index[positionItemsIndex+1] = int(index[positionItemsIndex+1])
            map1[index[positionItemsIndex + 1]][index[positionItemsIndex]] = "."
            positionItemsIndex += 2
    return map1

# fonction fin de tour qui imprime la carte et les stats
def endTurn():
    clear()
    FMap.printMap(VarC.positionJoueurY, VarC.positionJoueurX, VarM.mapInATab)
    print(f"Votre action précedentes était de : {VarC.prevMoove}")
    FBag.intoMyBag(VarC.sac, VarC.limitSac)
    print(f"{VarC.nomJoueur} voici vos stat, faim = {VarC.statFaim}, soif = {VarC.statSoif}, sommeil = {VarC.statSommeil}")