# coding: utf-8
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
    for i in VarC.bag:
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
            while choixAction > (len(VarC.bag) - 1) or choixAction < 0:
                choixAction = input(f"entre 0 et {(len(VarC.bag)) - 1}: ")
            # appel de la fonction use an item
            consumItem = FBag.useAnItem(VarC.bag[choixAction], VarC.thirst, VarC.hunger, VarC.sleep)
            # si la valeur delete est true on suprime
            if consumItem[0]:
                del VarC.bag[choixAction]
            # je reajuste ls stat
            VarC.thirst = consumItem[3]
            VarC.hunger = consumItem[4]
            VarC.sleep = consumItem[2]
            VarC.prevMoove = consumItem[1]
    # si le choix du joueur est de deposer un objet
    else:
        # je verifie que je peux deposer a la lplace ouce situe le joueur
        testMap = VarM.mapInATab[VarC.positionPlayerY][VarC.positionPlayerX]
        if testMap == ".":
            VarC.prevMoove = "Vous avez tenter de deposer un objet mais la place était deja prise"
        else:
            choixAction = input("Quel objet voulez vous deposer ? (par ID, rien pour sortir) ")
            # comme la fonction prec
            if choixAction != "rien":
                choixAction = int(choixAction)
                while choixAction > (len(VarC.bag) - 1) or choixAction < 0:
                    choixAction = input(f"entre 0 et {(len(VarC.bag)) - 1}: ")
                if choixAction < 4 or VarC.bag[choixAction] == "clef d'or" or VarC.bag[choixAction] == "clef d'argent" or VarC.bag[choixAction] == "clef de bronze":
                    VarC.prevMoove = "Cet objet ne peux pas etre deposer, il est trop important"
                else:
                    listToItem = [VarC.bag[choixAction], 0, VarC.positionPlayerX, VarC.positionPlayerY]
                    VarC.itemSlot.append(listToItem)
                    del VarC.bag[int(choixAction)]
                    VarM.mapInATab[VarC.positionPlayerY][VarC.positionPlayerX] = "."
                    print("Vous avez bien deposer votre objet")
                    VarC.prevMoove = "Depot d'un objet"

# fonction pour la commande dormir
def dormir():
    # flemme d'expliquer, il n'y a rien de sorcier la
    nbHeure = int(input("Combien d'heure voulez vous dormir ? "))
    goSleep = FMap.sleepHour(nbHeure, VarC.sleep, VarC.thirst, VarC.hunger)
    VarC.sleep = goSleep[0]
    VarC.hunger = goSleep[1]
    VarC.thirst = goSleep[2]
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
        VarC.namePlayer = FPrint.debutDuJeux()
        # je m'assure que le joueur ai lu les regle
        question = str(input("Est ce que vous êtes pret ? "))
        while question not in VarC.answerStart:
            question = str(input("Prenez votre temps et dite moi quand vous serez prêt ! "))

        print()

        # je cree de maniere aleatoire les diferent point de spawn des items
        VarC.itemSlot = FBag.createItemSlot(VarC.itemSlot)
        clear()
        # j'ajoute les items sur la map
        VarM.mapInATab = FMap.addItemPointOnMap(VarM.mapInATab, VarC.itemSlot)
    elif menuChoix == 2:
        # je verifie qu'il existe une sauvegarde valable
        if Fsave.checkIsSaved():
            Fsave.loadVarSaved()
            Fsave.loadVarMap()
            VarM.mapInATab = FMap.addItemPointOnMap(VarM.mapInATab, VarC.itemSlot)
        else:
            clear()
            print("Vous n'avez pas de sauvegarde valide a charger")
            input("Appuyer sur Entrer pour continuer")
            menu()
    elif menuChoix == 3:
        clear()
        Fsave.loadScore()
        input("Appuyer sur Entrer pour continuer")
        menu()
    elif menuChoix == 4:
        clear()
        Fsave.loadHistoric()
        input("Appuyer sur Entrer pour continuer")
        menu()

# fonction pour la commande bouger
def bouger():
    # je demande la directino et je m'ssure qu'elle soit valide
    direction = input("Vers ou souhaitez vous bouger ? ")
        
    while direction not in VarC.directionPossible:
        direction = input("Choisissez parmis z, s, q, d, regle ou touche ! ")

    # je verifie que le joueur peux s'y deplacer
    check = FMap.checkDeplacement(VarC.positionPlayerY, VarC.positionPlayerX, direction, VarM.mapInATab)
    
    while check == "ko":
        direction = input("Vous ne pouvez pas vous deplacer par la, choisissez une autre destination ! ")
        check = FMap.checkDeplacement(VarC.positionPlayerY, VarC.positionPlayerX, direction, VarM.mapInATab)
    # si le joueur gagne
    if check == "win":
        FPrint.gameWin(nomJoueur)
    # une fois que la direction est valide je le deplace
    else:
        if direction == "z":
            VarC.positionPlayerY = VarC.positionPlayerY - 1
            VarC.avatar = "▲"
        elif direction == "s":
            VarC.positionPlayerY = VarC.positionPlayerY + 1
            VarC.avatar = "▼"
        elif direction == "q":
            VarC.positionPlayerX = VarC.positionPlayerX - 1
            VarC.avatar = "◄"
        elif direction == "d":
            VarC.positionPlayerX = VarC.positionPlayerX + 1
            VarC.avatar = "►"
    
    # J'ajuste les var pour le deplacement
    VarC.sleep = VarC.sleep - 3
    VarC.thirst = VarC.thirst - 2
    VarC.hunger = VarC.hunger - 2
    VarC.prevMoove = "marcher"

    clear()
    # je check si le joueur a almrcher sur un objet
    itemPlaceCheck = FMap.checkItemPosition(VarC.positionPlayerX, VarC.positionPlayerY, VarC.itemSlot)
    if itemPlaceCheck != None:
        if itemPlaceCheck == "bouteille d'eau":
            FPrint.printBouteille()
        elif itemPlaceCheck == "ananas":
            FPrint.printAnanas()
        elif itemPlaceCheck == "kit de cookie":
            FPrint.printCookie()
        elif itemPlaceCheck == "noix de coco":
            FPrint.printCoconut()
        itemAction = input(f"en marchant vous tombé sur un {itemPlaceCheck} que veux tu en faire, (ramasser, ou rien) ? ")
        while itemAction not in VarC.itemActionPossible:
            itemAction = input(f"ramasser ou rien ")
        if itemAction == "ramasser":
            if len(VarC.bag) < 10:
                VarC.bag.append(itemPlaceCheck)
                VarM.mapInATab[VarC.positionPlayerY][VarC.positionPlayerX] = " "
            else:
                print("votre sac est plein, vous ne pouvez pas rammasser un autre objet")

# je m'assure que mes vars Int en soit bien
def formatVar():
    VarC.hunger = int(VarC.hunger)
    VarC.thirst = int(VarC.thirst)
    VarC.sleep = int(VarC.sleep)
    VarC.positionPlayerX = int(VarC.positionPlayerX)
    VarC.positionPlayerY = int(VarC.positionPlayerY)
    VarC.limitBag = int(VarC.limitBag)
    VarC.playerTurn = int(VarC.playerTurn)
    VarC.playerAction = int(VarC.playerAction)
    VarC.maxThirst = int(VarC.maxThirst)
    VarC.maxHunger = int(VarC.maxHunger)
    VarC.maxSleep = int(VarC.maxSleep)