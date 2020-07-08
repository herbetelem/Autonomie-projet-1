import fileFunction.variableMap as variableMap
import fileFunction.FunctionAboutBag as FBag
import fileFunction.FunctionAboutMap as FMap
import fileFunction.FunctionPrint as FPrint
import fileFunction.variableClassic as VarC
import os
clear = lambda: os.system('cls')


def checkDeplacement(y, x, deplacement, mapBinaire):
    if deplacement == "z":
        y = y - 1
    elif deplacement == "s":
        y = y + 1
    elif deplacement == "q":
        x = x - 1
    elif deplacement == "d":
        x = x + 1

    var = mapBinaire[y][x]

    if mapBinaire[y][x] == "1":
        return "ok"
    elif mapBinaire[y][x] == "2":
        return "win"
    else:
        return "ko"


def checkItemPosition(playerX, playerY, listItems):
    result = None
    for index in listItems:
        pointer = 2
        while pointer < len(index):
            if index[pointer] == playerX and index[pointer + 1] == playerY:
                result = index[0]
            pointer += 2
    return result


def printMap (y, x, map1):
    compteur1 = 0
    print()
    while compteur1 < len(map1):
        compteur2 = 0
        ligne = ""
        while compteur2 < len(map1[0]):
            if compteur1 == y and compteur2 == x:
                ligne = str(ligne) + VarC.avatar
            else:
                if str(map1[compteur1][compteur2]) == "*":
                    ligne = f"{ligne}\033[33m{map1[compteur1][compteur2]}\033[37m"
                elif str(map1[compteur1][compteur2]) == "~":
                    ligne = f"{ligne}\033[36m{map1[compteur1][compteur2]}\033[37m"
                elif str(map1[compteur1][compteur2]) == "█":
                    ligne = f"{ligne}\033[31m{map1[compteur1][compteur2]}\033[37m"
                elif str(map1[compteur1][compteur2]) == "M":
                    ligne = f"{ligne}\033[35m{map1[compteur1][compteur2]}\033[37m"
                elif str(map1[compteur1][compteur2]) == "♣":
                    ligne = f"{ligne}\033[32m{map1[compteur1][compteur2]}\033[37m"
                else:
                    ligne = str(ligne) + str(map1[compteur1][compteur2])
            compteur2 = compteur2 + 1
        compteur1 = compteur1 + 1
        print(ligne)
    print()
    print()

def sleepHour(nbHeure, statSommeil, statSoif, statFaim):
    statSommeil = statSommeil + nbHeure * 6
    if statSommeil > 100:
        statSommeil = 100
    statFaim = statFaim - nbHeure * 1
    statSoif = statSoif - nbHeure * 2
    return statSommeil, statFaim, statSoif

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

def endTurn():
    clear()
    FMap.printMap(VarC.positionJoueurY, VarC.positionJoueurX, variableMap.mapInATab)
    print(f"Votre action précedentes était de : {VarC.prevMoove}")
    FBag.intoMyBag(VarC.sac, VarC.limitSac)
    print(f"{VarC.nomJoueur} voici vos stat, faim = {VarC.statFaim}, soif = {VarC.statSoif}, sommeil = {VarC.statSommeil}")