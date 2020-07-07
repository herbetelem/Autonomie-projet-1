import fileFunction.debutDuJeux as fileDebutDuJeux
import fileFunction.printRegle as filePrintRegle
import fileFunction.printTouche as filePrintTouche
import fileFunction.variableMap as variableMap
import fileFunction.FunctionAboutBag as FBag
import fileFunction.FunctionAboutMap as FMap
import fileFunction.FunctionMain as FMain
import fileFunction.FunctionPrint as FPrint
import fileFunction.variableClassic as VarC
import os
clear = lambda: os.system('cls')



# Call all the function
VarC.nomJoueur = fileDebutDuJeux.debutDuJeux()
reponse = ["oui", "yes", "si"]
question = str(input("Est ce que vous êtes pret ? "))
while question not in reponse:
    question = str(input("Prenez votre temps et dite moi quand vous serez prêt ! "))

print()

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
        FMain.bouger()

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
        choixAction = input("Avec quel objet ? (par ID, rien pour sortir) ")
        if choixAction == "rien":
            FMap.endTurn()
            continue
        while not choixAction.isdigit() or int(choixAction) > (len(VarC.sac) - 1) or int(choixAction) < 0:
            choixAction = input(f"entre 0 et {(len(VarC.sac)) - 1}: ")
        consumItem = FBag.useAnItem(VarC.sac[int(choixAction)], VarC.statSoif, VarC.statFaim, VarC.statSommeil)
        if consumItem[0]:
            del VarC.sac[int(choixAction)]
        VarC.statSoif = consumItem[3]
        VarC.statFaim = consumItem[4]
        VarC.statSommeil = consumItem[2]
        VarC.prevMoove = consumItem[1]

    if VarC.statFaim <= 0 or VarC.statSoif <= 0 or VarC.statSommeil <= 0:
        VarC.statutParti = "ko"

    FMap.endTurn()

if VarC.statutParti == "ko":
    FPrint.gameOver()

