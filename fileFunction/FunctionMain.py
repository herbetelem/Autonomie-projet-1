import fileFunction.variableMap as variableMap
import fileFunction.FunctionAboutBag as FBag
import fileFunction.FunctionAboutMap as FMap
import fileFunction.FunctionMain as FMain
import fileFunction.FunctionPrint as FPrint
import fileFunction.FunctionGame as FGame
import fileFunction.variableClassic as VarC
import os
clear = lambda: os.system('cls')

def inventaire():
    clear()
    FPrint.printBag()
    print()
    dropOrUseModel = ["deposer", "utiliser"]
    dropOrUse = input("vous voulez deposer un objet ou en utiliser un ? ")
    while dropOrUse not in dropOrUseModel:
        dropOrUse = input(f"seulement {dropOrUseModel}")
    print(f"Vous disposer actuellement dans votre sac de :")
    compteur = 0
    result = ""
    for i in VarC.sac:
        result = f"{result} {compteur}: {i}\n"
        compteur +=1
    print(result)
    if dropOrUse == "utiliser":
        choixAction = int(input("Quel objet voulez vous utiliser ? (par ID, rien pour sortir) "))
        if choixAction != "rien":
            while choixAction > (len(VarC.sac) - 1) or choixAction < 0:
                choixAction = input(f"entre 0 et {(len(VarC.sac)) - 1}: ")
            consumItem = FBag.useAnItem(VarC.sac[choixAction], VarC.statSoif, VarC.statFaim, VarC.statSommeil)
            if consumItem[0]:
                del VarC.sac[choixAction]
            VarC.statSoif = consumItem[3]
            VarC.statFaim = consumItem[4]
            VarC.statSommeil = consumItem[2]
            VarC.prevMoove = consumItem[1]
    else:
        testMap = variableMap.mapInATab[VarC.positionJoueurY][VarC.positionJoueurX]
        if testMap == ".":
            VarC.prevMoove = "Vous avez tenter de deposer un objet mais la place était deja prise"
        else:
            choixAction = int(input("Quel objet voulez vous deposer ? (par ID, rien pour sortir) "))
            if choixAction != "rien":
                while choixAction > (len(VarC.sac) - 1) or choixAction < 0:
                    choixAction = input(f"entre 0 et {(len(VarC.sac)) - 1}: ")
                if choixAction < 4 or VarC.sac[choixAction] == "clef d'or" or VarC.sac[choixAction] == "clef d'argent" or VarC.sac[choixAction] == "clef de bronze":
                    VarC.prevMoove = "Cet objet ne peux pas etre deposer, il est trop important"
                else:
                    listToItem = [VarC.sac[choixAction], 0, VarC.positionJoueurX, VarC.positionJoueurY]
                    VarC.itemSlot.append(listToItem)
                    del VarC.sac[int(choixAction)]
                    variableMap.mapInATab[VarC.positionJoueurY][VarC.positionJoueurX] = "."
                    print("Vous avez bien deposer votre objet")
                    VarC.prevMoove = "Depot d'un objet"
    

def dormir():
    nbHeure = int(input("Combien d'heure voulez vous dormir ? "))
    goSleep = FMap.sleepHour(nbHeure, VarC.statSommeil, VarC.statSoif, VarC.statFaim)
    VarC.statSommeil = goSleep[0]
    VarC.statFaim = goSleep[1]
    VarC.statSoif = goSleep[2]
    VarC.prevMoove = "dormir"

def bouger():
    direction = input("Vers ou souhaitez vous bouger ? ")
        
    while direction not in VarC.directionPossible:
        direction = input("Choisissez parmis z, s, q, d, regle ou touche ! ")

    check = FMap.checkDeplacement(VarC.positionJoueurY, VarC.positionJoueurX, direction, variableMap.mapBinInATab)
    
    while check == "ko":
        direction = input("Vous ne pouvez pas vous deplacer par la, choisissez une autre destination ! ")
        check = FMap.checkDeplacement(VarC.positionJoueurY, VarC.positionJoueurX, direction, variableMap.mapBinInATab)

    if check == "win":
        FPrint.gameWin(nomJoueur)
    else:
        if direction == "z":
            VarC.positionJoueurY = VarC.positionJoueurY - 1
            VarC.avatar = "▲"
        elif direction == "s":
            VarC.positionJoueurY = VarC.positionJoueurY + 1
            VarC.avatar = "▼"
        elif direction == "q":
            VarC.positionJoueurX = VarC.positionJoueurX - 1
            VarC.avatar = "◄"
        elif direction == "d":
            VarC.positionJoueurX = VarC.positionJoueurX + 1
            VarC.avatar = "►"
    
    VarC.statSommeil = VarC.statSommeil - 3
    VarC.statSoif = VarC.statSoif - 2
    VarC.statFaim = VarC.statFaim - 2
    VarC.prevMoove = "marcher"

    clear()

    itemPlaceCheck = FMap.checkItemPosition(VarC.positionJoueurX, VarC.positionJoueurY, VarC.itemSlot)
    if itemPlaceCheck != None:
        itemAction = input(f"en marchant vous tombé sur un {itemPlaceCheck} que veux tu en faire, (ramasser, ou rien) ? ")
        while itemAction not in VarC.itemActionPossible:
            itemAction = input(f"ramasser ou rien ")
        if itemAction == "ramasser":
            if len(VarC.sac) < 10:
                VarC.sac.append(itemPlaceCheck)
                variableMap.mapInATab[VarC.positionJoueurY][VarC.positionJoueurX] = " "
            else:
                print("votre sac est plein, vous ne pouvez pas rammasser un autre objet")