import fileFunction.debutDuJeux as fileDebutDuJeux
import fileFunction.printRegle as filePrintRegle
import fileFunction.printTouche as filePrintTouche
import fileFunction.printMap as filePrintMap
import fileFunction.checkDeplacement as fileCheckDeplacement
import fileFunction.gameOver as fileGameOver
import fileFunction.gameWin as fileGameWin
import fileFunction.intoMyBag as intoMyBag
import fileFunction.sleepHour as sleepHour
import fileFunction.createItemSlot as createItemSlot
import fileFunction.checkItemPosition as checkItemPosition
import os




# Call all the function
nomJoueur = fileDebutDuJeux.debutDuJeux()
reponse = ["oui", "yes", "si"]
question = str(input("Est ce que vous êtes pret ? "))
while question not in reponse:
    question = str(input("Prenez votre temps et dite moi quand vous serez prêt ! "))

print()
clear = lambda: os.system('cls')
avatar = 0
statSoif = 100
statFaim = 100
statSommeil = 100
positionJoueurY = 3
positionJoueurX = 10
sac = ["PC portable", "couteau suisse", "carte", ["bouteille", 100]]
limitSac = 10
itemSlot = [["bouteille d'eau pleine", 5], ["pomme", 5], ["noix de coco", 5], ["kit de cookie", 5]]
itemSlot = createItemSlot.createItemSlot(itemSlot)
prevMoove = "commencer"
clear()
filePrintMap.printMap(positionJoueurY, positionJoueurX, itemSlot)
statutParti = "ok"
actionPossible = ["bouger", "dormir", "regle", "touche"]
directionPossible = ["s", "z", "q", "d"]
itemActionPossible = ["ramasser", "rien"]

print()
while statutParti == "ok":
    action = input("Que souhaitez vous faire ? ")
    
    while action not in actionPossible:
        action = input("Vous pouvez bouger ou dormir ! ")
    
    if action == "regle":
        filePrintRegle.printRegle()
    
    elif action == "touche":
        filePrintTouche.printTouche()
    
    elif action == "bouger":
        direction = input("Vers ou souhaitez vous bouger ? ")
        
        while direction not in directionPossible:
            direction = input("Choisissez parmis z, s, q, d, regle ou touche ! ")
        check = fileCheckDeplacement.checkDeplacement(positionJoueurY, positionJoueurX, direction)
        
        while check == "ko":
            direction = input("Vous ne pouvez pas vous deplacer par la, choisissez une autre destination ! ")

        if check == "win":
            fileGameWin.gameWin(nomJoueur)
        else:
            if direction == "z":
                positionJoueurY = positionJoueurY - 1
            elif direction == "s":
                positionJoueurY = positionJoueurY + 1
            elif direction == "q":
                positionJoueurX = positionJoueurX - 1
            elif direction == "d":
                positionJoueurX = positionJoueurX + 1
        
        statSommeil = statSommeil - 3
        statSoif = statSoif - 2
        statFaim = statFaim - 2
        prevMoove = "marcher"

    elif action == "dormir":
        nbHeure = int(input("Combien d'heure voulez vous dormir ? "))
        goSleep = sleepHour.sleepHour(nbHeure, statSommeil, statSoif, statFaim)
        statSommeil = goSleep[0]
        statFaim = goSleep[1]
        statSoif = goSleep[2]
        prevMoove = "dormir"
    clear()

    itemPlaceCheck = checkItemPosition.checkItemPosition(positionJoueurX, positionJoueurY, itemSlot)
    if itemPlaceCheck != None:
        itemAction = input(f"ok tu est a l'emplacement d'un objet, tu creuse et trouve un {itemPlaceCheck} que veux tu en faire, (ramasser, ou rien) ? ")
        while itemAction not in itemActionPossible:
            itemAction = input(f"ramasser ou rien ")
        if itemAction == "ramasser":
            if len(sac) < 10:
                sac.append(itemPlaceCheck)
            else:
                print("votre sac est plein, vous ne pouvez pas rammasser un autre objet")

    if statFaim <= 0 or statSoif <= 0 or statSommeil <= 0:
        statutParti = "ko"

    print("Votre action précedentes était de : " + prevMoove)
    filePrintMap.printMap(positionJoueurY, positionJoueurX, itemSlot)
    intoMyBag.intoMyBag(sac, limitSac)
    print(f"{nomJoueur} voici vos stat, faim = {statFaim}, soif = {statSoif}, sommeil = {statSommeil}")

if statutParti == "ko":
    fileGameOver.gameOver()

