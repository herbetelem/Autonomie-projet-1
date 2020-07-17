# coding: utf-8
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
    FMap.printMap(VarC.positionPlayerY, VarC.positionPlayerX, VarM.mapInATab)

    print()
    while VarC.statutParty == "ok":
        FMain.formatVar()
        # je verifie si le joueur est au point de victoire avec les 3 clef
        if VarM.mapInATab[VarC.positionPlayerY][VarC.positionPlayerX] == "@":
            if "clef d'or" in VarC.bag and "clef d'argent" in VarC.bag and "clef de bronze" in VarC.bag:
                FPrint.gameWin(VarC.namePlayer, VarC.playerTurn, VarC.playerAction)
            # si il n'a pas les clef je le degage de maniere aleatoire dans un espace vide
            else:
                VarC.prevMoove = "Vous avez essayé de sortir du jeu sans toute les clefs, \n                                    un singe vous assome et vous traine quelque part dans l'ile"
                punitionY = random.randint(0, len(VarM.mapInATab) - 1)
                punitionX = random.randint(0, len(VarM.mapInATab[0]) - 1)
                while VarM.mapInATab[punitionY][punitionX] != " ":
                    punitionY = random.randint(0, len(VarM.mapInATab) - 1)
                    punitionX = random.randint(0, len(VarM.mapInATab[0]) - 1)
                VarC.positionPlayerY = punitionY
                VarC.positionPlayerX = punitionX
                
        # je verifie si il est a la position d'un jeu et si oui je lance le jeux
        #------------------------------------------------------------------------------
        elif VarM.mapInATab[VarC.positionPlayerY][VarC.positionPlayerX] == "£":
            if len(VarC.bag) == VarC.limitBag:
                print("Vous n'avez pas assez de place pour potentielement recuperer la clef")
                VarC.positionPlayerX = VarC.positionPlayerX + 1
            else:
                FGame.jeuxNombreMystere()
                VarC.playerAction += 1
        elif VarM.mapInATab[VarC.positionPlayerY][VarC.positionPlayerX] == "$":
            if len(VarC.bag) == VarC.limitBag:
                print("Vous n'avez pas assez de place pour potentielement recuperer la clef")
                VarC.positionPlayerX = VarC.positionPlayerX - 1
            else:
                FGame.jeuxCodeCesar()
                VarC.playerAction += 1
        elif VarM.mapInATab[VarC.positionPlayerY][VarC.positionPlayerX] == "€":
            if len(VarC.bag) == VarC.limitBag:
                print("Vous n'avez pas assez de place pour potentielement recuperer la clef")
                VarC.positionPlayerX = VarC.positionPlayerX - 1
            else:
                FGame.jeuxFizzBuzz()
                VarC.playerAction += 1
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
                        VarC.positionPlayerY = 24
                        VarC.positionPlayerX = 3
                    elif destination == "cesar":
                        VarC.prevMoove = "Comme vous êtes un tricheur vous aller direct voir cesar"
                        VarC.positionPlayerY = 24
                        VarC.positionPlayerX = 92
                    elif destination == "singe":
                        VarC.prevMoove = "Comme vous êtes un tricheur vous aller direct voir les singes"
                        VarC.positionPlayerY = 3
                        VarC.positionPlayerX = 84
                    elif destination == "porte":
                        VarC.prevMoove = "Comme vous êtes un tricheur vous aller direct voir la porte"
                        VarC.positionPlayerY = 3
                        VarC.positionPlayerX = 44
                    else:
                        input("tricher c'est bien, regarder les options c'est mieux")
                else:
                    print("Raté")
            
            elif action == "touche":
                FPrint.printTouche()
            
            elif action == "bouger":
                FMain.bouger()
                VarC.playerTurn += 1

            elif action == "dormir":
                FMain.dormir()
                VarC.playerAction += 1
            
            elif action == "inventaire":
                FMain.inventaire()
                VarC.playerAction += 1
            
            elif action == "sauvegarder":
                FSave.saveData()

            elif action == "quitter":
                if str(input("Vous êtes sur ? ") == "oui"):
                    clear()
                    sys.exit()
                else:
                    print("vous n'avez pas confirmer, j'annule donc votre demande.")

            # je verifie que le joueur ai encore des stats pour continuer
            if VarC.hunger <= 0 or VarC.thirst <= 0 or VarC.sleep <= 0:
                VarC.statutParty = "ko"
        # j'apelle la fonction fin de tour qui imprime la carte et les stats
        FMap.endTurn()

    # si la parti est ko game over
    if VarC.statutParty == "ko":
        FPrint.gameOver(VarC.namePlayer)

# truc d'Alain pour appeler le main propre
if __name__ == "__main__":
    Main()
