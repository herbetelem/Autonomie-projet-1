import random
import fileFunction.FunctionAboutMap as FMap
import fileFunction.variableMap as variableMap

# [["item", nombre d'item, x1, y1, x2, y2, etc], etc ...]


def createItemSlot(items):
    for index in items:
        compteur = 0
        while compteur < index[1]:
            y = random.randint(3, 22)
            x = random.randint(9, 88)
            check = FMap.checkDeplacement(
                y, x, "deplacement", variableMap.mapBinInATab)
            while check == "ko":
                y = random.randint(3, 22)
                x = random.randint(9, 88)
                check = FMap.checkDeplacement(
                    y, x, "deplacement", variableMap.mapBinInATab)
            index.append(x)
            index.append(y)
            compteur += 1
    return items


def intoMyBag(bag, limitBag):
    placeRestant = limitBag - len(bag)
    returned = "vous avez dans votre sac ["
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


def dellAnItem(x, y, itemList, nomItem):
    indexItem = 0
    index = 0
    while index < len(itemList):
        if itemList[index][0] == nomItem:
            indexItem = index
        index += 1
    compteur = 2
    while compteur < len(itemList[indexItem]):
        if itemList[indexItem][compteur] == x and itemList[indexItem][compteur+1] == y:
            del itemList[indexItem][compteur]
            del itemList[indexItem][compteur]
        compteur += 2
    return itemList


def useAnItem(item, soif, faim, sommeil):
    if item in ["PC portable", "chargeur solaire", "couteau suisse", "carte"]:
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
    else:
        itemDelete = True
        if item == "bouteille d'eau":
            phrase = "Vous videz votre bouteille d'eau"
            soif = soif + 50
            if soif > 100:
                soif = 100
            return itemDelete, phrase, sommeil, soif, faim

        if item == "poireau":
            phrase = "Vous manger votre poireau"
            faim = faim + 50
            if faim > 100:
                faim = 100
            return itemDelete, phrase, sommeil, soif, faim

        if item == "kit de cookie":
            phrase = "c'est balo vous n'avez pas de quoi faire ces cookies"
            return itemDelete, phrase, sommeil, soif, faim

        if item == "noix de coco":
            phrase = "Vous manger la chair de la noix et buvez son jus"
            soif = soif + 25
            if soif > 100:
                soif = 100
            faim = faim + 25
            if faim > 100:
                faim = 100
            return itemDelete, phrase, sommeil, soif, faim
    return


