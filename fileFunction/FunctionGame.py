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

def jeuxCodeCesar():
    clear()
    FPrint.printCesar()
    FPrint.printRegleCesar()
    input("Appuyer sur Entrer pour continuer")
    clear()
    code = input("Choisissez la lettre code : ")
    while len(code) > 1:
        code = input("une seul lettre")
    code = code.lower()
    print("Voici le credo avec le code")
    print(codeCesar(code, VarG.credo))
    tour = 0

    while tour < 5:
        FPrint.printCesar()
        print("saisissez une lettre pour coder le credo avec celle ci")
        print("saisissez Entrer pour voir le credo normal")
        print("saisissez plusieur lettres pour faire une tentative de trouver votre nom")
        actionJoueur = input("Votre saisie : ")
        clear()
        if len(actionJoueur) == 0:
            print("Le credo en clair est")
            print(VarG.credo)
        elif len(actionJoueur) == 1:
            print(f"Le credo avec le code {actionJoueur}")
            print(codeCesar(actionJoueur, VarG.credo))
        elif len(actionJoueur) > 1:
            tour += 1
            tentative = decryptCodeCesar(code, actionJoueur)
            print("Votre saisi decrypter donne :")
            print(tentative)
            input(f"Tentative {tour}/5 appuyer sur entrer pour essayer")
            if tentative == VarC.nomJoueur.lower():
                print("bravo vous avez gagné la clef d'argent.")
                print("Vous la ranger immédiatement dans votre sac.")
                VarC.sac.append("clef d'argent")
                variableMap.mapInATab[VarC.positionJoueurY][VarC.positionJoueurX] = " "
                tour = 6
                input("entrer pour continuer")
            else:
                print("Votre saisi ne corespond pas a votre nom")
    if tour == 5:
        VarC.prevMoove = "Malheureusment vous avez mis plus de 5 tentative a trouver votre nom, reessayer plus tard"
        VarC.positionJoueurX = VarC.positionJoueurX - 1

def letterToNb(letter):
    letter = letter.lower()
    for i in range(0, len(VarG.listeAlphabet)):
        if VarG.listeAlphabet[i] == letter:
            return i


def codeCesar(clef, mots):
    clef = clef.lower()
    clef = letterToNb(clef)
    mots = list(mots)
    for i in range(0, len(mots)):
        if mots[i] != " ":
            lettreX = letterToNb(mots[i])
            mots[i] = VarG.listeAlphabet2[lettreX+clef]
    mots = ''.join(mots)
    return mots

def decryptCodeCesar(clef, mots):
    clef = clef.lower()
    clef = letterToNb(clef)
    mots = list(mots)
    for i in range(0, len(mots)):
        if mots[i] != " ":
            lettreX = letterToNb(mots[i])
            mots[i] = VarG.listeAlphabet2[lettreX-clef]
    mots = ''.join(mots)
    return mots
