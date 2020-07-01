def checkItemPosition(playerX, playerY, listItems):
    result = None
    for index in listItems:
        pointer = 2
        while pointer < len(index):
            if index[pointer] == playerX and index[pointer + 1] == playerY:
                result = index[0]
            pointer += 2
    return result