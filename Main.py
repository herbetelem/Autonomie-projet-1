# Import de mes fichiers et des libs
import fileFunction.variableMap as VarM
import fileFunction.FunctionAboutBag as FBag
import fileFunction.FunctionAboutMap as FMap
import fileFunction.FunctionMain as FMain
import fileFunction.FunctionPrint as FPrint
import fileFunction.FunctionGame as FGame
import fileFunction.variableClassic as VarC
import fileFunction.FunctionSave as FSave
import random
import os
import sys
clear = lambda: os.system('cls')


def Main():
    # J'affiche le menu qui gere new parti
    FMain.menu()
    # j'affiche la carte
    FMap.printMap(VarC.positionJoueurY, VarC.positionJoueurX, VarM.mapInATab)

    print()
    while VarC.statutParti == "ok":
        FMain.formatVar()
        # je verifie si le joueur est au point de victoire avec les 3 clef
        if VarM.mapInATab[VarC.positionJoueurY][VarC.positionJoueurX] == "@":
            if "clef d'or" in VarC.sac and "clef d'argent" in VarC.sac and "clef de bronze" in VarC.sac:
                FPrint.gameWin(VarC.nomJoueur, VarC.tourJoueur, VarC.actionJoueur)
            # si il n'a pas les clef je le degage de maniere aleatoire dans un espace vide
            else:
                VarC.prevMoove = "Vous avez essayé de sortir du jeu sans toute les clefs, \n                                    un singe vous assome et vous traine quelque part dans l'ile"
                punitionY = random.randint(0, len(VarM.mapInATab) - 1)
                punitionX = random.randint(0, len(VarM.mapInATab[0]) - 1)
                while VarM.mapInATab[punitionY][punitionX] != " ":
                    punitionY = random.randint(0, len(VarM.mapInATab) - 1)
                    punitionX = random.randint(0, len(VarM.mapInATab[0]) - 1)
                VarC.positionJoueurY = punitionY
                VarC.positionJoueurX = punitionX
                
        # je verifie si il est a la position d'un jeu et si oui je lance le jeux
        #------------------------------------------------------------------------------
        elif VarM.mapInATab[VarC.positionJoueurY][VarC.positionJoueurX] == "£":
            if len(VarC.sac) == VarC.limitSac:
                print("Vous n'avez pas assez de place pour potentielement recuperer la clef")
                VarC.positionJoueurX = VarC.positionJoueurX + 1
            else:
                FGame.jeuxNombreMystere()
                VarC.actionJoueur += 1
        elif VarM.mapInATab[VarC.positionJoueurY][VarC.positionJoueurX] == "$":
            if len(VarC.sac) == VarC.limitSac:
                print("Vous n'avez pas assez de place pour potentielement recuperer la clef")
                VarC.positionJoueurX = VarC.positionJoueurX - 1
            else:
                FGame.jeuxCodeCesar()
                VarC.actionJoueur += 1
        elif VarM.mapInATab[VarC.positionJoueurY][VarC.positionJoueurX] == "€":
            if len(VarC.sac) == VarC.limitSac:
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

            elif action == "42":
                mdp = str(input("donne moi pi avec 20 chiffre derriere : "))
                if mdp == "flemme":
                    destination = str(input("Vers ou voulez vous aller ? (sphinx, cesar, singe, porte) : "))
                    if destination == "sphinx":
                        VarC.prevMoove = "Comme vous êtes un tricheur vous aller direct voir le sphinx"
                        VarC.positionJoueurY = 24
                        VarC.positionJoueurX = 3
                    elif destination == "cesar":
                        VarC.prevMoove = "Comme vous êtes un tricheur vous aller direct voir cesar"
                        VarC.positionJoueurY = 24
                        VarC.positionJoueurX = 92
                    elif destination == "singe":
                        VarC.prevMoove = "Comme vous êtes un tricheur vous aller direct voir les singes"
                        VarC.positionJoueurY = 3
                        VarC.positionJoueurX = 84
                    elif destination == "porte":
                        VarC.prevMoove = "Comme vous êtes un tricheur vous aller direct voir la porte"
                        VarC.positionJoueurY = 3
                        VarC.positionJoueurX = 44
                    else:
                        input("tricher c'est bien, regarder les options c'est mieux")
                else:
                    print("Raté")
            
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
            
            elif action == "sauvegarder":
                FSave.saveData()

            elif action == "quitter":
                if str(input("Vous êtes sur ? ") == "oui"):
                    clear()
                    sys.exit()
                else:
                    print("vous n'avez pas confirmer, j'annule donc votre demande.")

            # je verifie que le joueur ai encore des stats pour continuer
            if VarC.statFaim <= 0 or VarC.statSoif <= 0 or VarC.statSommeil <= 0:
                VarC.statutParti = "ko"
        # j'apelle la fonction fin de tour qui imprime la carte et les stats
        FMap.endTurn()

    # si la parti est ko game over
    if VarC.statutParti == "ko":
        FPrint.gameOver(VarC.nomJoueur)

# truc d'Alain pour appeler le main propre
if __name__ == "__main__":
    Main()
