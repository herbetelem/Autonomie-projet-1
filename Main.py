def debutDuJeux():
    print("------------")
    print("----Jeux----")
    print("------------")
    nomJoueur = str(input("Bonjour anonyme joueur, comment te prénome-tu ? "))
    print()
    print("Bonjour " + str(nomJoueur) + " !")
    print()
    print("Vous allez voir une carte aparaitre, les caractere suivants coresponde au element suivant")
    print()
    print("# correspond au bord de la carte")
    print()
    print("V correspond au zone montagneuse")
    print()
    print("~ correspond au zone nautique")
    print()
    print("† correspond au zone desertique")
    print()
    print("* correspond au zone de foret")
    print()
    print("∅ correspond au zone de foret")
    print()
    reponse = ["oui", "yes", "si"]
    question = str(input("Est ce que vous êtes pret ? "))
    while question not in reponse:
        question = str(input("Prenez votre temps et dite moi quand vous serez prêt ! "))
    print()









# def the map
def printMap (y, x):
    map1 = [["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "#"],
    ["#", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "#"],
    ["#", "V", "V", "V", "V", "V", "V", "V", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", " ", " ", " ", " ", " ", " ", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "V", "V", "V", "V", "V", "V", "#"],
    ["#", "V", "V", "V", "V", "V", "V", "V", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "V", "V", "V", "V", "V", "V", "#"],
    ["#", "V", "V", "V", "V", "V", "V", "V", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", " ", " ", " ", " ", " ", " ", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "V", "V", "V", "V", "V", "V", "#"],
    ["#", "V", "V", "V", "V", "V", "V", "V", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "V", "V", "V", "V", "V", "V", "#"],
    ["#", "V", "V", "V", "V", "V", "V", "V", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", "V", "V", "V", "V", "V", "V", "#"],
    ["#", "V", "V", "V", "V", "V", "V", "V", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "V", "V", "V", "V", "V", "V", "#"],
    ["#", "V", "V", "V", "V", "V", "V", "V", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", "V", "V", "V", "V", "V", "V", "#"],
    ["#", "V", "V", "V", "V", "V", "V", "V", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "V", "V", "V", "V", "V", "V", "#"],
    ["#", "V", "V", "V", "V", "V", "V", "V", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", "V", "V", "V", "V", "V", "V", "#"],
    ["#", "V", "V", "V", "V", "V", "V", "V", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "V", "V", "V", "V", "V", "V", "#"],
    ["#", "V", "V", "V", "V", "V", "V", "V", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "V", "V", "V", "V", "V", "V", "#"],
    ["#", "~", "~", "~", "~", "~", "~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "V", "V", "V", "V", "V", "V", "#"],
    ["#", "~", "~", "~", "~", "~", "~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "V", "V", "V", "V", "V", "V", "#"],
    ["#", "~", "~", "~", "~", "~", "~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "V", "V", "V", "V", "V", "V", "#"],
    ["#", "~", "~", "~", "~", "~", "~", "~", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "†", " ", "†", " ", "†", " ", "V", "V", "V", "V", "V", "V", "#"],
    ["#", "~", "~", "~", "~", "~", "~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "#"],
    ["#", "~", "~", "~", "~", "~", "~", "~", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", " ", " ", "~", " ", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "†", " ", "†", " ", "†", " ", "~", "~", "~", "~", "~", "~", "#"],
    ["#", "~", "~", "~", "~", "~", "~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "#"],
    ["#", "~", "~", "~", "~", "~", "~", "~", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", " ", " ", "~", " ", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "†", " ", "†", " ", "†", " ", "~", "~", "~", "~", "~", "~", "#"],
    ["#", "~", "~", "~", "~", "~", "~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "#"],
    ["#", "~", "~", "~", "~", "~", "~", "~", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", " ", " ", "~", " ", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "†", " ", "†", " ", "†", " ", "~", "~", "~", "~", "~", "~", "#"],
    ["#", "~", "~", "~", "~", "~", "~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "~", "~", "#"],
    ["#", "~", "~", "~", "~", "~", "~", "~", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", " ", " ", "~", " ", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "#"],
    ["#", "~", "~", "~", "~", "~", "~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "#"],
    ["#", "~", "~", "~", "~", "~", "~", "~", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", "*", " ", " ", " ", "~", "~", "~", "~", "~", " ", " ", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "#"],
    ["#", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "#"],
    ["#", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "#"],
    ["#", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]

    compteur1 = 0
    print()
    while compteur1 < 32:
        compteur2 = 0
        ligne = ""
        while compteur2 < 52:
            if compteur1 == y and compteur2 == x:
                ligne = str(ligne) + "@"
            else:
                ligne = str(ligne) + str(map1[compteur1][compteur2])
            compteur2 = compteur2 + 1
        compteur1 = compteur1 + 1
        print(ligne)
    print()



def checkDeplacement(y, x, deplacement):
    mapBinaire = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    if direction == "haut":
        y = y - 1
    elif direction == "bas":
        y = y + 1
    elif direction == "gauche":
        x = x - 1
    elif direction == "droite":
        x = x + 1

    if mapBinaire[y][x] == 1:
        return "ok"
    else:
        return "ko"



# Call all the function*
debutDuJeux()
avatar = 0
positionJoueurY = 3
positionJoueurX = 10
printMap(positionJoueurY, positionJoueurX)
statutParti = "ok"
directionPossible = ["bas", "haut", "gauche", "droite"]
print()
while statutParti == "ok":    
    direction = input("Quel direction souhaitez vous prendre ? ")
    while direction not in directionPossible:
        direction = input("Choisissez parmis haut, bas, gauche ou droite ! ")
    while checkDeplacement(positionJoueurY, positionJoueurX, direction) == "ko":
        direction = input("Vous ne pouvez pas vous deplacer par la, choisissez une autre destination ! ")
    if direction == "haut":
        positionJoueurY = positionJoueurY - 1
    elif direction == "bas":
        positionJoueurY = positionJoueurY + 1
    elif direction == "gauche":
        positionJoueurX = positionJoueurX - 1
    elif direction == "droite":
        positionJoueurX = positionJoueurX + 1
    printMap(positionJoueurY, positionJoueurX)
    avatar = avatar + 1
    if avatar == 10:
        statutParti = "ko"


