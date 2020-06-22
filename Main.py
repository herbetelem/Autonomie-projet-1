import fileFunction.debutDuJeux as fileDebutDuJeux
import fileFunction.printRegle as filePrintRegle
import fileFunction.printTouche as filePrintTouche
import fileFunction.printMap as filePrintMap
import fileFunction.checkDeplacement as fileCheckDeplacement
import fileFunction.gameOver as fileGameOver




# Call all the function*
nomJoueur = fileDebutDuJeux.debutDuJeux()
reponse = ["oui", "yes", "si"]
question = str(input("Est ce que vous êtes pret ? "))
while question not in reponse:
    question = str(input("Prenez votre temps et dite moi quand vous serez prêt ! "))
print()
avatar = 0
statSoif = 100
statFaim = 100
statSommeil = 100
positionJoueurY = 3
positionJoueurX = 10
filePrintMap.printMap(positionJoueurY, positionJoueurX)
statutParti = "ok"
directionPossible = ["s", "z", "q", "d", "regle", "touche"]
print()
while statutParti == "ok":
    direction = input("Que souhaitez vous faire ? ")
    while direction not in directionPossible:
        direction = input("Choisissez parmis z, s, q, d, regle ou touche ! ")
    if direction == "regle":
        filePrintRegle.printRegle()
    elif direction == "touche":
        filePrintTouche.printTouche()
    else:
        while fileCheckDeplacement.checkDeplacement(positionJoueurY, positionJoueurX, direction) == "ko":
            direction = input("Vous ne pouvez pas vous deplacer par la, choisissez une autre destination ! ")
        
        if direction == "z":
            positionJoueurY = positionJoueurY - 1
        elif direction == "s":
            positionJoueurY = positionJoueurY + 1
        elif direction == "q":
            positionJoueurX = positionJoueurX - 1
        elif direction == "d":
            positionJoueurX = positionJoueurX + 1
        filePrintMap.printMap(positionJoueurY, positionJoueurX)
        statSommeil = statSommeil - 3
        statSoif = statSoif - 2
        statFaim = statFaim - 2
        print(str(nomJoueur) + " voici vos stat, faim = " + str(statFaim) + ", soif = " + str(statSoif) + ", sommeil = " + str(statSommeil))
        if statFaim <= 0 or statSoif <= 0 or statSommeil <= 0:
            statutParti = "ko"
if statutParti == "ko":
    fileGameOver.gameOver()
