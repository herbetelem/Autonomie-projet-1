import fileFunction.variableMap as variableMap
import fileFunction.FunctionAboutBag as FBag
import fileFunction.FunctionAboutMap as FMap
import fileFunction.FunctionMain as FMain
import fileFunction.FunctionPrint as FPrint
import fileFunction.FunctionGame as FGame
import fileFunction.variableClassic as VarC
import fileFunction.variableGame as VarG
import os
clear = lambda: os.system('cls')


def jeuxNombreMystere():
    clear()
    FPrint.printMystere()
    FPrint.printRegleMystere()
    test = input("Taper entrer pour continuer")    
    clear()
    tour = 0
    nombreTrouve = 0
    minTrouver = 0
    maxTrouver = 100
    while nombreTrouve < 3 and tour < 20:
        tour += 1
        FPrint.printMystere()
        print(f"Vos possibilité sont entre {minTrouver} et {maxTrouver}")
        print(f"Vous en ête au tour {tour}/20 du nombre {nombreTrouve+1}/3")
        if nombreTrouve == 0:
            print("Cherche bien mon premier nombre")
            choixNombre = int(input("Quel nombre proposé vous ? "))
            clear()
            if VarG.premierNombreMyst == choixNombre:
                print("Bravo tu a trouver mon premier nombre")
                nombreTrouve += 1
                tour = 0
                minTrouver = 0
                maxTrouver = 100
            if choixNombre > VarG.premierNombreMyst:
                print("Sphinx : « Le nombre que j’ai en tête est plus petit».")
                if choixNombre < maxTrouver:
                    maxTrouver = choixNombre
            elif choixNombre < VarG.premierNombreMyst:
                print("Sphinx : « Le nombre que j’ai en tête est plus grand».")
                if choixNombre > minTrouver:
                    minTrouver = choixNombre

        elif nombreTrouve == 1:
            print("Cherche bien mon deuxieme nombre")
            choixNombre = int(input("Quel nombre proposé vous ? "))
            clear()
            if VarG.deuxiemeNombreMyst == choixNombre:
                print("Bravo tu a trouver mon deuxieme nombre")
                nombreTrouve += 1
                tour = 0
                minTrouver = 0
                maxTrouver = 100
            if choixNombre > VarG.deuxiemeNombreMyst:
                print("Sphinx : « Le nombre que j’ai en tête est plus petit».")
                if choixNombre < maxTrouver:
                    maxTrouver = choixNombre
            elif choixNombre < VarG.deuxiemeNombreMyst:
                print("Sphinx : « Le nombre que j’ai en tête est plus grand».")
                if choixNombre > minTrouver:
                    minTrouver = choixNombre

        elif nombreTrouve == 2:
            print("Cherche bien mon troisieme nombre")
            choixNombre = int(input("Quel nombre proposé vous ? "))
            clear()
            if VarG.troisiemeNombreMyst == choixNombre:
                print("Bravo tu a trouver mon troisieme nombre, tu remporte la clef de bronze")
                nombreTrouve += 1
                tour = 20
            if choixNombre > VarG.troisiemeNombreMyst:
                print("Sphinx : « Le nombre que j’ai en tête est plus petit».")
                if choixNombre < maxTrouver:
                    maxTrouver = choixNombre
            elif choixNombre < VarG.troisiemeNombreMyst:
                print("Sphinx : « Le nombre que j’ai en tête est plus grand».")
                if choixNombre > minTrouver:
                    minTrouver = choixNombre
        
    if nombreTrouve == 3:
        print("Félicitation, vous avez gagner. Vous mettez votre clef de bronze dans votre sac")
        VarC.sac.append("clef de bronze")
        variableMap.mapInATab[VarC.positionJoueurY][VarC.positionJoueurX] = " "
        input("Si vous êtes prets a continuer apuyer sur entrer")
    elif tour == 20:
        print("c'est dommage, vous avez mis trop de tour pour trouver la solution, reessayer plus tard")
        input("Si vous êtes prets a continuer apuyer sur entrer")
        VarC.positionJoueurX = VarC.positionJoueurX + 1