import fileFunction.debutDuJeux as fileDebutDuJeux
import fileFunction.printRegle as filePrintRegle
import fileFunction.printTouche as filePrintTouche
import fileFunction.variableMap as variableMap
import fileFunction.FunctionAboutBag as FBag
import fileFunction.FunctionAboutMap as FMap
import fileFunction.FunctionPrint as FPrint
import fileFunction.variableClassic as VarC
import os
clear = lambda: os.system('cls')




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
        elif direction == "s":
            VarC.positionJoueurY = VarC.positionJoueurY + 1
        elif direction == "q":
            VarC.positionJoueurX = VarC.positionJoueurX - 1
        elif direction == "d":
            VarC.positionJoueurX = VarC.positionJoueurX + 1
    
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