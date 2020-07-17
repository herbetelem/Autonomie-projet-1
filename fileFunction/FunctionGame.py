# coding: utf-8
# librairie
import fileFunction.variableMap as VarM
import fileFunction.FunctionAboutBag as FBag
import fileFunction.FunctionAboutMap as FMap
import fileFunction.FunctionMain as FMain
import fileFunction.FunctionPrint as FPrint
import fileFunction.FunctionGame as FGame
import fileFunction.variableClassic as VarC
import fileFunction.variableGame as VarG
import random
import time
import os
clear = lambda: os.system('cls')



# Nombre Mystere
#---------------------------------------------------------------------------------------------------------
def jeuxNombreMystere():
    clear()
    FPrint.printMystere()
    FPrint.printRegleMystere()
    input("Taper entrer pour continuer")    
    clear()
    # je creer mes variable
    tour = 0
    nombreTrouve = 0
    minTrouver = 0
    maxTrouver = 100
    # tant que le joueur n'a pas trouver les 3 chiffres ou que ces tour sont inferieur a 20
    while nombreTrouve < 3 and tour < 20:
        tour += 1
        FPrint.printMystere()
        # je print les possibilité
        print(f"Vos possibilité sont entre {minTrouver} et {maxTrouver}")
        print(f"Vous en ête au tour {tour}/20 du nombre {nombreTrouve+1}/3")
        # premiere manche
        if nombreTrouve == 0:
            print("Cherche bien mon premier nombre")
            choixNombre = int(input("Quel nombre proposé vous ? "))
            clear()
            # si il trouve
            if VarG.premierNombreMyst == choixNombre:
                print("Bravo tu a trouver mon premier nombre")
                # je reset mes variable
                nombreTrouve += 1
                tour = 0
                minTrouver = 0
                maxTrouver = 100
            # si il ce tronpe je lui dit si le nombre est + ou - et je reduit le champs de ces ppossibilité
            if choixNombre > VarG.premierNombreMyst:
                print("Sphinx : « Le nombre que j’ai en tête est plus petit».")
                if choixNombre < maxTrouver:
                    maxTrouver = choixNombre
            elif choixNombre < VarG.premierNombreMyst:
                print("Sphinx : « Le nombre que j’ai en tête est plus grand».")
                if choixNombre > minTrouver:
                    minTrouver = choixNombre
        # deuxieme manche, comme la premiere
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
        # troisime manche toujour pareil
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
    # Si le joueur a trouver les 3 chiffres, je lui donne la clef
    if nombreTrouve == 3:
        print("Félicitation, vous avez gagner. Vous mettez votre clef de bronze dans votre sac")
        VarC.bag.append("clef de bronze")
        VarM.mapInATab[VarC.positionPlayerY][VarC.positionPlayerX] = " "
        input("Si vous êtes prets a continuer apuyer sur entrer")
    # sinon je le fait changer de position pour ne pas lancer le jeu a la chaine
    elif tour == 20:
        print("c'est dommage, vous avez mis trop de tour pour trouver la solution, reessayer plus tard")
        input("Si vous êtes prets a continuer apuyer sur entrer")
        VarC.positionPlayerX = VarC.positionPlayerX + 1
#---------------------------------------------------------------------------------------------------------


# Code Cesar
#---------------------------------------------------------------------------------------------------------
# fonction main du jeux
def jeuxCodeCesar():
    clear()
    # je print les regles et le dessin Ascii
    FPrint.printCesar()
    FPrint.printRegleCesar()
    input("Appuyer sur Entrer pour continuer")
    clear()
    # je demande quel code le jeux vas utiliser ou je le genere de maniere aléatoire
    # Mode FLEMME
    code = input("Choisissez la lettre code : ")
    # Mode NORMAL
    # code = VarG.listeAlphabet[random.randint(1, 26)]
    # Si le code est choisi par le joueur, je m'assure qu'il respecte ce que je veux
    while len(code) > 1:
        code = input("une seul lettre")
    code = code.lower()
    credoCode = codeCesar(code, VarG.credo)
    # et enfin je print le credo crypter avec le code
    print("Voici le credo avec le code")
    print(codeCesar(code, VarG.credo))
    tour = 0

    # tant que le joueur n'a pas depasser les 5 tours
    while tour < 5:
        # j'imprime le dessin
        FPrint.printCesar()
        # je dit au joueur ce que je veux qu'il rentre
        print("saisissez une lettre pour coder le credo avec celle ci")
        print("saisissez Entrer pour voir le credo normal")
        print("saisissez plusieur lettres pour faire une tentative de trouver votre nom")
        actionJoueur = input("Votre saisie : ")
        clear()

        # Si le joueur n'a rien rentrer je le sort le credo en clair 
        if len(actionJoueur) == 0:
            print("Le credo en clair est")
            print(VarG.credo)
        # Si le joueur n'a rentrer qu'une seule lettre, je sort le credo crypter avec cette lettre
        elif len(actionJoueur) == 1:
            print(f"Le credo avec le code {actionJoueur}")
            print(decryptCodeCesar(actionJoueur, credoCode))
        # Si le joueur a rentrer plus d'une lettre, je decrypte sa saisi avec le code du debut
        elif len(actionJoueur) > 1:
            # le fait de rentrer plusieur lettre est la seul action qui consome un tour
            tour += 1
            tentative = decryptCodeCesar(code, actionJoueur)
            print("Votre saisi decrypter donne :")
            print(tentative)
            input(f"Tentative {tour}/5 appuyer sur entrer pour essayer")
            # je check si le retour est egual au nom du joueur
            if tentative == VarC.namePlayer.lower():
                # si il gagne je lui donne la clef
                print("bravo vous avez gagné la clef d'argent.")
                print("Vous la ranger immédiatement dans votre sac.")
                # je met la clef dans le sac (j'ai verifier avant si il avait de la place)
                VarC.bag.append("clef d'argent")
                # je suprime le portail qui amenait au mini jeu
                VarM.mapInATab[VarC.positionPlayerY][VarC.positionPlayerX] = " "
                # je met le tour a 6 pour sortir de la boucle du jeu
                tour = 6
                input("entrer pour continuer")
            else:
                print("Votre saisi ne corespond pas a votre nom")
    # Si j'ai gagné tour = 6 donc pas 5, si tour = 5 c'est que tu a perdu
    if tour == 5:
        # je met un message de loose dans la var qui donne les mooves
        VarC.prevMoove = "Malheureusment vous avez mis plus de 5 tentative a trouver votre nom, reessayer plus tard"
        # je decale le joueur de la position parce que sinon le joueur referait le jeux a l'infinie
        VarC.positionPlayerX = VarC.positionPlayerX - 1

# fonction qui trouve le chiffre par rapport au lettre
def letterToNb(letter):
    letter = letter.lower()
    for i in range(0, len(VarG.listeAlphabet)):
        if VarG.listeAlphabet[i] == letter:
            return i

# fonction qui code une phrase avec une clef
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

# fonction qui decode une phrase avec une clef
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
#---------------------------------------------------------------------------------------------------------

# FizzBuzz
def jeuxFizzBuzz():
    clear()
    # je print le singe et les regles
    FPrint.printFizzBuzz()
    FPrint.printRegleFizz()
    # je créer une liste de singe 
    listeJoueur = list(VarG.listeSinge)
    # je met le nom du joueur dans la liste
    listeJoueur[10][0] = VarC.namePlayer
    random.shuffle(listeJoueur)
    # cette variable est ok tant que le joueur est encore dans la partie
    joueurStatut = "ok"
    input("Taper entrer pour continuer")
    # la parti continue tant que le joueur est encore en course et qu'il y a plus d'un joueur encore dans la parti
    while len(listeJoueur) > 1 and joueurStatut == "ok":
        clear()
        FPrint.printFizzBuzz()
        print()
        print(f"Joueur dans la parti {len(listeJoueur)}/11")
        print()
        statutManche = "ok"
        depart = 1
        while statutManche == "ok":
            for joueur in listeJoueur:
                if statutManche == "ok":
                    # si le tour en cour doit etre fizz buzz ou fizzbuzz
                    # je verifie par un rand si le joueur en cours a suffisament de chance pour reussir
                    # si oui il donne le bon therme si non il donne le mauvais therme est et eliminer
                    if depart % 3 == 0 and depart % 5 == 0:
                        if joueur[1] > random.randint(1, 100):
                            print(f"{joueur[0]} : FizzBuzz")
                        else:
                            print(f"{joueur[0]} : {depart}")
                            print(f"Erreur de {joueur[0]}, vas ramassez des bananes")
                            indexJoueur = listeJoueur.index([joueur[0], joueur[1]])
                            del listeJoueur[indexJoueur]
                            statutManche = "ko"
                    elif depart % 3 == 0:
                        if joueur[1] > random.randint(1, 100):
                            print(f"{joueur[0]} : Fizz")
                        else:
                            print(f"{joueur[0]} : {depart}")
                            print(f"Erreur de {joueur[0]}, vas ramassez des bananes")
                            indexJoueur = listeJoueur.index([joueur[0], joueur[1]])
                            del listeJoueur[indexJoueur]
                            statutManche = "ko"
                    elif depart % 5 == 0:
                        if joueur[1] > random.randint(1, 100):
                            print(f"{joueur[0]} : Buzz")
                        else:
                            print(f"{joueur[0]} : {depart}")
                            print(f"Erreur de {joueur[0]}, vas ramassez des bananes")
                            indexJoueur = listeJoueur.index([joueur[0], joueur[1]])
                            del listeJoueur[indexJoueur]
                            statutManche = "ko"
                    else:
                        print(f"{joueur[0]} : {depart}")
                    if statutManche == "ko":
                        if joueur[0] == VarC.namePlayer:
                            joueurStatut = "ko"
                    depart += 1
                    # time.sleep permet d'avoir un peu de temp entre chaque tour
                    time.sleep(1)
    # si le joueur est le dernier dans la parti il gagne
    if joueurStatut == "ok":
        print(f"{listeJoueur[0][0]} a gagné la parti, vous prenez la clef d'or et partez")
        VarC.bag.append("clef d'or")
        VarM.mapInATab[VarC.positionPlayerY][VarC.positionPlayerX] = " "
        input("Taper entrer pour continuer")
    
    # sinon il perd et bah c'est balo
    else:
        VarC.prevMoove = "Malheureusment vous avez perdu au FizzBuzz, reessayer plus tard"
        VarC.positionPlayerX = VarC.positionPlayerX - 1
        print("vous avez perdu")
        input("Taper entrer pour continuer")