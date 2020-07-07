import fileFunction.debutDuJeux as fileDebutDuJeux
import fileFunction.printRegle as filePrintRegle
import fileFunction.printTouche as filePrintTouche
# import fileFunction.gameOver as fileGameOver
# import fileFunction.gameWin as fileGameWin
import fileFunction.variableMap as variableMap
import fileFunction.FunctionAboutBag as FBag
import fileFunction.FunctionAboutMap as FMap
import fileFunction.FunctionPrint as FPrint
import fileFunction.variableClassic as VarC
import os




# Call all the function
nomJoueur = fileDebutDuJeux.debutDuJeux()
reponse = ["oui", "yes", "si"]
question = str(input("Est ce que vous êtes pret ? "))
while question not in reponse:
    question = str(input("Prenez votre temps et dite moi quand vous serez prêt ! "))

print()
clear = lambda: os.system('cls')
VarC.itemSlot = FBag.createItemSlot(VarC.itemSlot)
clear()
variableMap.mapInATab = FMap.addItemPointOnMap(variableMap.mapInATab, VarC.itemSlot)
FMap.printMap(VarC.positionJoueurY, VarC.positionJoueurX, variableMap.mapInATab)

print()
while VarC.statutParti == "ok":
    action = input("Que souhaitez vous faire ? ")
    
    while action not in VarC.actionPossible:
        action = input(f"Vous pouvez {VarC.actionPossible}")
    
    if action == "regle":
        filePrintRegle.printRegle()
    
    elif action == "touche":
        filePrintTouche.printTouche()
    
    elif action == "bouger":
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

    elif action == "dormir":
        nbHeure = int(input("Combien d'heure voulez vous dormir ? "))
        goSleep = FMap.sleepHour(nbHeure, VarC.statSommeil, VarC.statSoif, VarC.statFaim)
        VarC.statSommeil = goSleep[0]
        VarC.statFaim = goSleep[1]
        VarC.statSoif = goSleep[2]
        VarC.prevMoove = "dormir"
    
    elif action == "inventaire":
        clear()
        FPrint.printBag()
        print()
        print(f"Vous disposer actuellement dans votre sac de :")
        compteur = 0
        result = ""
        for i in VarC.sac:
            result = f"{result} {compteur}: {i}\n"
            compteur +=1
        print(result)
        choixAction = input("Quel objet voulez vous utiliser ? (par ID)")

    if VarC.statFaim <= 0 or VarC.statSoif <= 0 or VarC.statSommeil <= 0:
        VarC.statutParti = "ko"

    print(f"Votre action précedentes était de : {VarC.prevMoove}")
    FMap.printMap(VarC.positionJoueurY, VarC.positionJoueurX, variableMap.mapInATab)
    FBag.intoMyBag(VarC.sac, VarC.limitSac)
    print(f"{nomJoueur} voici vos stat, faim = {VarC.statFaim}, soif = {VarC.statSoif}, sommeil = {VarC.statSommeil}")

if VarC.statutParti == "ko":
    FPrint.gameOver()

