# Import de mes fichiers et des libs
import fileFunction.variableMap as variableMap
import fileFunction.FunctionAboutBag as FBag
import fileFunction.FunctionAboutMap as FMap
import fileFunction.FunctionMain as FMain
import fileFunction.FunctionPrint as FPrint
import fileFunction.FunctionGame as FGame
import fileFunction.variableClassic as VarC
import fileFunction.FunctionSave as FSave
import random
import os
clear = lambda: os.system('cls')


def Main():
    # je recupere les variable dans mon fichier txt
    FSave.loadVarClassic()
    # Call all the function
    # appelle de la fonction pour demander le nom du joueur et print les regles
    VarC.nomJoueur = FPrint.debutDuJeux()
    # je m'assure que le joueur ai lu les regle
    question = str(input("Est ce que vous êtes pret ? "))
    while question not in VarC.reponseDebut:
        question = str(input("Prenez votre temps et dite moi quand vous serez prêt ! "))

    print()

    # je cree de maniere aleatoire les diferent point de spawn des items
    VarC.itemSlot = FBag.createItemSlot(VarC.itemSlot)
    clear()
    # j'ajoute les items sur la map
    variableMap.mapInATab = FMap.addItemPointOnMap(variableMap.mapInATab, VarC.itemSlot)
    # j'affiche la carte
    FMap.printMap(VarC.positionJoueurY, VarC.positionJoueurX, variableMap.mapInATab)

    print()
    while VarC.statutParti == "ok":
        # je verifie si le joueur est au point de victoire avec les 3 clef
        if variableMap.mapInATab[VarC.positionJoueurY][VarC.positionJoueurX] == "@":
            if "clef d'or" in VarC.sac and "clef d'argent" in VarC.sac and "clef de bronze" in VarC.sac:
                FPrint.gameWin(VarC.nomJoueur)
            # si il n'a pas les clef je le degage de maniere aleatoire dans un espace vide
            else:
                VarC.prevMoove = "Vous avez essayé de sortir du jeu sans toute les clefs, \n                                    un singe vous assome et vous traine quelque part dans l'ile"
                punitionY = random.randint(0, len(variableMap.mapInATab) - 1)
                punitionX = random.randint(0, len(variableMap.mapInATab[0]) - 1)
                while variableMap.mapInATab[punitionY][punitionX] != " ":
                    punitionY = random.randint(0, len(variableMap.mapInATab) - 1)
                    punitionX = random.randint(0, len(variableMap.mapInATab[0]) - 1)
                VarC.positionJoueurY = punitionY
                VarC.positionJoueurX = punitionX
                
        # je verifie si il est a la position d'un jeu et si oui je lance le jeux
        #------------------------------------------------------------------------------
        elif variableMap.mapInATab[VarC.positionJoueurY][VarC.positionJoueurX] == "£":
            if len(sac) == VarC.limitSac:
                print("Vous n'avez pas assez de place pour potentielement recuperer la clef")
                VarC.positionJoueurX = VarC.positionJoueurX + 1
            else:
                FGame.jeuxNombreMystere()
                VarC.actionJoueur += 1
        elif variableMap.mapInATab[VarC.positionJoueurY][VarC.positionJoueurX] == "$":
            if len(sac) == VarC.limitSac:
                print("Vous n'avez pas assez de place pour potentielement recuperer la clef")
                VarC.positionJoueurX = VarC.positionJoueurX - 1
            else:
                FGame.jeuxCodeCesar()
                VarC.actionJoueur += 1
        elif variableMap.mapInATab[VarC.positionJoueurY][VarC.positionJoueurX] == "€":
            if len(sac) == VarC.limitSac:
                print("Vous n'avez pas assez de place pour potentielement recuperer la clef")
                VarC.positionJoueurX = VarC.positionJoueurX - 1
            else:
                FGame.jeuxFizzBuzz()
                VarC.actionJoueur += 1
        #------------------------------------------------------------------------------

        else:
            # je demande l'action du joueur
            action = input("Que souhaitez vous faire ? ")
            # je verifie que l'action est possible
            while action not in VarC.actionPossible:
                action = input(f"Vous pouvez {VarC.actionPossible}")
            
            # j'apelle la fonction qui correspond a l'action du joueur
            if action == "regle":
                FPrint.printRegle()
            
            elif action == "touche":
                FPrint.printTouche()
            
            elif action == "bouger":
                FMain.bouger()
                VarC.tourJoueur += 1

            elif action == "dormir":
                FMain.dormir()
                VarC.actionJoueur += 1
            
            elif action == "inventaire":
                FMain.inventaire()
                VarC.actionJoueur += 1

            # je verifie que le joueur ai encore des stats pour continuer
            if VarC.statFaim <= 0 or VarC.statSoif <= 0 or VarC.statSommeil <= 0:
                VarC.statutParti = "ko"
        # j'apelle la fonction fin de tour qui imprime la carte et les stats
        FMap.endTurn()

    # si la parti est ko game over
    if VarC.statutParti == "ko":
        FPrint.gameOver()

# truc d'Alain pour appeler le main propre
if __name__ == "__main__":
    Main()
