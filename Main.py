import fileFunction.variableMap as variableMap
import fileFunction.FunctionAboutBag as FBag
import fileFunction.FunctionAboutMap as FMap
import fileFunction.FunctionMain as FMain
import fileFunction.FunctionPrint as FPrint
import fileFunction.FunctionGame as FGame
import fileFunction.variableClassic as VarC
import random
import os
clear = lambda: os.system('cls')


def Main():
    # Call all the function
    VarC.nomJoueur = FPrint.debutDuJeux()
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
        if variableMap.mapInATab[VarC.positionJoueurY][VarC.positionJoueurX] == "@":
            if "clef d'or" in VarC.sac and "clef d'argent" in VarC.sac and "clef de bronze" in VarC.sac:
                FPrint.gameWin(VarC.nomJoueur)
            else:
                VarC.prevMoove = "Vous avez essayé de sortir du jeu sans toute les clefs, \n                                    un singe vous assome et vous traine quelque part dans l'ile"
                punitionY = random.randint(0, len(variableMap.mapInATab) - 1)
                punitionX = random.randint(0, len(variableMap.mapInATab[0]) - 1)
                while variableMap.mapInATab[punitionY][punitionX] != " ":
                    punitionY = random.randint(0, len(variableMap.mapInATab) - 1)
                    punitionX = random.randint(0, len(variableMap.mapInATab[0]) - 1)
                VarC.positionJoueurY = punitionY
                VarC.positionJoueurX = punitionX
                
        elif variableMap.mapInATab[VarC.positionJoueurY][VarC.positionJoueurX] == "£":
            FGame.jeuxNombreMystere()
        elif variableMap.mapInATab[VarC.positionJoueurY][VarC.positionJoueurX] == "$":
            FGame.jeuxCodeCesar()
        elif variableMap.mapInATab[VarC.positionJoueurY][VarC.positionJoueurX] == "€":
            recompense = FGame.jeuxNombreMystere()
        else:
            action = input("Que souhaitez vous faire ? ")
            
            while action not in VarC.actionPossible:
                action = input(f"Vous pouvez {VarC.actionPossible}")
            
            if action == "regle":
                FPrint.printRegle()
            
            elif action == "touche":
                FPrint.printTouche()
            
            elif action == "bouger":
                FMain.bouger()

            elif action == "dormir":
                FMain.dormir()
            
            elif action == "inventaire":
                FMain.inventaire()

            if VarC.statFaim <= 0 or VarC.statSoif <= 0 or VarC.statSommeil <= 0:
                VarC.statutParti = "ko"

        FMap.endTurn()

    if VarC.statutParti == "ko":
        FPrint.gameOver()


if __name__ == "__main__":
    Main()
