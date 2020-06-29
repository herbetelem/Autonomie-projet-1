import random
import fileFunction.checkDeplacement as checkDeplacement

# [["item", nombre d'item, x1, y1, x2, y2, etc], etc ...]
def createItemSlot(items):
    for index in items:
        compteur = 0
        while compteur < index[1]:
            y = random.randint(1, 30)
            x = random.randint(1, 50)
            check = checkDeplacement.checkDeplacement(y, x, "deplacement")
            while check == "ko":
                y = random.randint(1, 30)
                x = random.randint(1, 50)
                check = checkDeplacement.checkDeplacement(y, x, "deplacement")
            index.append(x)
            index.append(y)
            compteur += 1
    return items
