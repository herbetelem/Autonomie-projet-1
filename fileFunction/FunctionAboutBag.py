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
            check = FMap.checkDeplacement(y, x, "deplacement", variableMap.mapBinInATab)
            while check == "ko":
                y = random.randint(3, 22)
                x = random.randint(9, 88)
                check = FMap.checkDeplacement(y, x, "deplacement", variableMap.mapBinInATab)
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
        index +=1
    compteur = 2
    while compteur < len(itemList[indexItem]):
        if itemList[indexItem][compteur] == x and itemList[indexItem][compteur+1] == y:
            # itemList[indexItem][compteur] = itemList[indexItem][compteur] * -1
            # itemList[indexItem][compteur+1] = itemList[indexItem][compteur+1] * -1
            del itemList[indexItem][compteur]
            del itemList[indexItem][compteur]
        compteur += 2
    return itemList