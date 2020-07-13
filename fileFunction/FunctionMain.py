# add all libs
import fileFunction.variableMap as VarM
import fileFunction.FunctionAboutBag as FBag
import fileFunction.FunctionAboutMap as FMap
import fileFunction.FunctionMain as FMain
import fileFunction.FunctionPrint as FPrint
import fileFunction.FunctionGame as FGame
import fileFunction.variableClassic as VarC
import fileFunction.FunctionSave as Fsave
import os
clear = lambda: os.system('cls')

# fonction pour la commande inventaire
def inventaire():
    clear()
    FPrint.printBag()
    print()
    # def les 2 option
    dropOrUseModel = ["deposer", "utiliser"]
    dropOrUse = input("vous voulez deposer un objet ou en utiliser un ? ")
    # check que les option du joueur sois dans celle qui sont possible
    while dropOrUse not in dropOrUseModel:
        dropOrUse = input(f"seulement {dropOrUseModel}")
    print(f"Vous disposer actuellement dans votre sac de :")
    compteur = 0
    result = ""
    for i in VarC.sac:
        result = f"{result} {compteur}: {i}\n"
        compteur +=1
    print(result)
    # si action est use
    if dropOrUse == "utiliser":
        # je demande quel obket a use
        choixAction = input("Quel objet voulez vous utiliser ? (par ID, rien pour sortir) ")
        # si pas rien, si rien bah tu sort
        if choixAction != "rien":
            # je trasforme le choix en int pour ma suite
            choixAction = int(choixAction)
            # je verifie que l'id de lobjet est valide
            while choixAction > (len(VarC.sac) - 1) or choixAction < 0:
                choixAction = input(f"entre 0 et {(len(VarC.sac)) - 1}: ")
            # appel de la fonction use an item
            consumItem = FBag.useAnItem(VarC.sac[choixAction], VarC.statSoif, VarC.statFaim, VarC.statSommeil)
            # si la valeur delete est true on suprime
            if consumItem[0]:
                del VarC.sac[choixAction]
            # je reajuste ls stat
            VarC.statSoif = consumItem[3]
            VarC.statFaim = consumItem[4]
            VarC.statSommeil = consumItem[2]
            VarC.prevMoove = consumItem[1]
    # si le choix du joueur est de deposer un objet
    else:
        # je verifie que je peux deposer a la lplace ouce situe le joueur
        testMap = VarM.mapInATab[VarC.positionJoueurY][VarC.positionJoueurX]
        if testMap == ".":
            VarC.prevMoove = "Vous avez tenter de deposer un objet mais la place était deja prise"
        else:
            choixAction = input("Quel objet voulez vous deposer ? (par ID, rien pour sortir) ")
            # comme la fonction prec
            if choixAction != "rien":
                choixAction = int(choixAction)
                while choixAction > (len(VarC.sac) - 1) or choixAction < 0:
                    choixAction = input(f"entre 0 et {(len(VarC.sac)) - 1}: ")
                if choixAction < 4 or VarC.sac[choixAction] == "clef d'or" or VarC.sac[choixAction] == "clef d'argent" or VarC.sac[choixAction] == "clef de bronze":
                    VarC.prevMoove = "Cet objet ne peux pas etre deposer, il est trop important"
                else:
                    listToItem = [VarC.sac[choixAction], 0, VarC.positionJoueurX, VarC.positionJoueurY]
                    VarC.itemSlot.append(listToItem)
                    del VarC.sac[int(choixAction)]
                    VarM.mapInATab[VarC.positionJoueurY][VarC.positionJoueurX] = "."
                    print("Vous avez bien deposer votre objet")
                    VarC.prevMoove = "Depot d'un objet"

# fonction pour la commande dormir
def dormir():
    # flemme d'expliquer, il n'y a rien de sorcier la
    nbHeure = int(input("Combien d'heure voulez vous dormir ? "))
    goSleep = FMap.sleepHour(nbHeure, VarC.statSommeil, VarC.statSoif, VarC.statFaim)
    VarC.statSommeil = goSleep[0]
    VarC.statFaim = goSleep[1]
    VarC.statSoif = goSleep[2]
    VarC.prevMoove = "dormir"

# fonction qui gere le menu
def menu():
    clear()
    FPrint.menuTitle()
    menuChoix = int(input("Choisissez votre option ici : "))
    if menuChoix == 1:
        # je recupere les variable dans mon fichier txt
        Fsave.loadVarClassic()
        Fsave.loadVarMap()
    elif menuChoix == 2:
        pass
    elif menuChoix == 3:
        clear()
        Fsave.loadScore()
        input("Appuyer sur Enter pour continuer")
        menu()

# fonction pour la commande bouger
def bouger():
    # je demande la directino et je m'ssure qu'elle soit valide
    direction = input("Vers ou souhaitez vous bouger ? ")
        
    while direction not in VarC.directionPossible:
        direction = input("Choisissez parmis z, s, q, d, regle ou touche ! ")

    # je verifie que le joueur peux s'y deplacer
    check = FMap.checkDeplacement(VarC.positionJoueurY, VarC.positionJoueurX, direction, VarM.mapInATab)
    
    while check == "ko":
        direction = input("Vous ne pouvez pas vous deplacer par la, choisissez une autre destination ! ")
        check = FMap.checkDeplacement(VarC.positionJoueurY, VarC.positionJoueurX, direction, VarM.mapInATab)
    # si le joueur gagne
    if check == "win":
        FPrint.gameWin(nomJoueur)
    # une fois que la direction est valide je le deplace
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
    
    # J'ajuste les var pour le deplacement
    VarC.statSommeil = VarC.statSommeil - 3
    VarC.statSoif = VarC.statSoif - 2
    VarC.statFaim = VarC.statFaim - 2
    VarC.prevMoove = "marcher"

    clear()
    # je check si le joueur a almrcher sur un objet
    itemPlaceCheck = FMap.checkItemPosition(VarC.positionJoueurX, VarC.positionJoueurY, VarC.itemSlot)
    if itemPlaceCheck != None:
        itemAction = input(f"en marchant vous tombé sur un {itemPlaceCheck} que veux tu en faire, (ramasser, ou rien) ? ")
        while itemAction not in VarC.itemActionPossible:
            itemAction = input(f"ramasser ou rien ")
        if itemAction == "ramasser":
            if len(VarC.sac) < 10:
                VarC.sac.append(itemPlaceCheck)
                VarM.mapInATab[VarC.positionJoueurY][VarC.positionJoueurX] = " "
            else:
                print("votre sac est plein, vous ne pouvez pas rammasser un autre objet")