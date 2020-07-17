# coding: utf-8
# Import des librairie
import random
import fileFunction.FunctionAboutMap as FMap
import fileFunction.variableMap as VarM
import fileFunction.variableClassic as VarC

# [["item", nombre d'item, x1, y1, x2, y2, etc], etc ...]

# fonction pour creer les slot pour chaque item
def createItemSlot(items):
    porte = ["£", "$", "€", "@"]
    for index in items:
        compteur = 0
        # tant que mon compteur est inferieur au nombre d'item a creer
        while compteur < index[1]:
            # je genere random une position x et y
            y = random.randint(0, (len(VarM.mapInATab)  - 1))
            x = random.randint(0, (len(VarM.mapInATab[0]) - 1))
            # je verifie que les coordonée soit libre et si c'est ko je recommence jusqu'a ce que soit ok
            check = FMap.checkDeplacement(
                y, x, "deplacement", VarM.mapInATab)
            # while check == "ko" or VarM.mapInATab[y][x] != " ":
            # while VarM.mapInATab[y][x] != " ":
            while VarM.mapInATab[y][x] not in VarM.slotMoove or VarM.mapInATab[y][x] in porte:
                y = random.randint(0, (len(VarM.mapInATab)  - 1))
                x = random.randint(0, (len(VarM.mapInATab[0])  - 1))
                check = FMap.checkDeplacement(
                    y, x, "deplacement", VarM.mapInATab)
            # si c'est bon j'ajoute X et Y dans le tablea de l'objet
            index.append(x)
            index.append(y)
            compteur += 1
    return items

# Fonction qui liste l'interrieur du sac
def intoMyBag(bag, limitBag):
    # la place restante est :
    placeRestant = limitBag - len(bag)
    returned = "vous avez dans votre sac ["
    # je parcours mon sac et je l'affiche
    for index in bag:
        if index == bag[len(bag) - 1]:
            if isinstance(index, list):
                returned = f"{returned} {index[0]}"
            else:
                returned = f"{returned} {index}"
        else:
            if isinstance(index, list):
                returned = f"{returned} {index[0]} ], ["
            else:
                returned = returned + index + "], ["
    returned = f"{returned} ]. Il vous reste {placeRestant} de places dans votre sac"
    print(returned)

# fonction pour suprimer un objet
def dellAnItem(x, y, itemList, nomItem):
    indexItem = 0
    index = 0
    # petite boucle pour trouver l'index de l'item a suprimer
    while index < len(itemList):
        if itemList[index][0] == nomItem:
            indexItem = index
        index += 1
    compteur = 2
    # petite boucle pour trouver les deux coordonée et les suprimer du tableau
    while compteur < len(itemList[indexItem]):
        if itemList[indexItem][compteur] == x and itemList[indexItem][compteur+1] == y:
            del itemList[indexItem][compteur]
            del itemList[indexItem][compteur]
        compteur += 2
    return itemList

# fonction pour utiliser un objet
def useAnItem(item, soif, faim, sommeil):
    # je verifis que l'item ne sois pas deletable apres use et j'utilise l'objet
    if item in ["PC portable", "chargeur solaire", "couteau suisse", "carte", "clef de bronze", "clef d'argent", "clef d'or"]:
        itemDelete = False
        if item == "PC portable":
            phrase = "Apres avoir regarder un episode de big bang theorie sur netflix\nVous relevez la tete et vous rendez compte avoir perdu 3h"
            sommeil = sommeil - (3 * 3)
            soif = soif - (2 * 3)
            faim = faim - (2 * 3)
            return itemDelete, phrase, sommeil, soif, faim
        if item == "chargeur solaire":
            phrase = "Vous ne pouvez pas utiliser cet objet pour l'instant"
            return itemDelete, phrase, sommeil, soif, faim
        
        if item == "couteau suisse":
            phrase = "Vous ne pouvez pas utiliser cet objet pour l'instant, mais il est tres utilse pour couper des légumes"
            return itemDelete, phrase, sommeil, soif, faim

        if item == "carte":
            phrase = "vous utilisez deja votre carte pour vous deplacer"
            return itemDelete, phrase, sommeil, soif, faim
        if item == "clef de bronze" or item == "clef d'argent" or item == "clef d'or":
            phrase = "vous pourrez utiliser les clefs que une fois a la porte final"
            return itemDelete, phrase, sommeil, soif, faim
    # sinon l'objet sera suprimer apres utilisation et j'utilise l'objet
    else:
        itemDelete = True
        if item == "bouteille d'eau":
            phrase = "Vous videz votre bouteille d'eau"
            soif = soif + 50
            if soif > int(VarC.maxThirst):
                soif = VarC.maxThirst
            return itemDelete, phrase, sommeil, soif, faim

        if item == "ananas":
            phrase = "Vous manger votre ananas"
            faim = faim + 50
            if faim > int(VarC.maxHunger):
                faim = VarC.maxHunger
            return itemDelete, phrase, sommeil, soif, faim

        if item == "kit de cookie":
            phrase = "c'est balo vous n'avez pas de quoi faire ces cookies"
            return itemDelete, phrase, sommeil, soif, faim

        if item == "noix de coco":
            phrase = "Vous manger la chair de la noix et buvez son jus"
            soif = soif + 25
            if soif > VarC.maxThirst:
                soif = int(VarC.maxThirst)
            faim = faim + 25
            if faim > int(VarC.maxHunger):
                faim = VarC.maxHunger
            return itemDelete, phrase, sommeil, soif, faim
    return


