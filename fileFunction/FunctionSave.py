# coding: utf-8
import json
import fileFunction.variableClassic as VarC
import fileFunction.variableMap as VarM
import datetime
import sys

# sa fonctionne mais j'ai rien compris donc j'ai rien a expluquer
def loadVarClassic():
    varLoad = []
    try:
        with open("C:/Users/PYTHON/Documents/GitHub/Autonomie-projet-1/fileVarTxt/variableClassic.txt", "r", encoding = "utf-8") as file : 
            fileLoaded = [line for line in file]
            for lineX in fileLoaded:
                lineX = lineX.replace("\n", "")
                varLoad.append(lineX)
        varLoad[2] = int(varLoad[2])
        varLoad[3] = int(varLoad[3])
        varLoad[4] = int(varLoad[4])
        varLoad[5] = int(varLoad[5])
        varLoad[6] = int(varLoad[6])
        varLoad[8] = int(varLoad[8])

        varLoad[7] = varLoad[7].split(" | ")
        varLoad[12] = varLoad[12].split(" | ")
        varLoad[13] = varLoad[13].split(" | ")
        varLoad[14] = varLoad[14].split(" | ")
        varLoad[15] = varLoad[15].split(" | ")

        varLoad[9] = varLoad[9].split(" | ")
        compteur = 0
        for index in varLoad[9]:
            varLoad[9][compteur] = index.split(" ! ")
            varLoad[9][compteur][1] = int(varLoad[9][compteur][1])
            compteur += 1
        VarC.namePlayer = varLoad[0]
        VarC.avatar = varLoad[1]
        VarC.thirst = varLoad[2]
        VarC.hunger = varLoad[3]
        VarC.sleep = varLoad[4]
        VarC.positionPlayerY = varLoad[5]
        VarC.positionPlayerX = varLoad[6]
        VarC.bag = varLoad[7]
        VarC.limitBag = varLoad[8]
        VarC.itemSlot = varLoad[9]
        VarC.prevMoove = varLoad[10]
        VarC.statutParty = varLoad[11]
        VarC.actionPossible = varLoad[12]
        VarC.directionPossible = varLoad[13]
        VarC.itemActionPossible = varLoad[14]
        VarC.answerStart = varLoad[15]
        VarC.maxThirst = varLoad[16]
        VarC.maxHunger = varLoad[17]
        VarC.maxSleep = varLoad[18]
        VarC.playerAction = int(varLoad[19])
        VarC.playerTurn = int(varLoad[20])
    except:
        print("Votre ficher de config n'a pas été trouvé, veuillez verifier vos dossiers")
        sys.exit()

def loadVarSaved():
    varLoad = []
    try:
        with open("C:/Users/PYTHON/Documents/GitHub/Autonomie-projet-1/fileVarTxt/save/save.txt", "r", encoding = "utf-8") as file : 
            fileLoaded = [line for line in file]
            for lineX in fileLoaded:
                lineX = lineX.replace("\n", "")
                varLoad.append(lineX)

        varLoad[2] = int(varLoad[2])
        varLoad[3] = int(varLoad[3])
        varLoad[4] = int(varLoad[4])
        varLoad[5] = int(varLoad[5])
        varLoad[6] = int(varLoad[6])
        varLoad[8] = int(varLoad[8])

        varLoad[7] = varLoad[7].split(" | ")
        varLoad[12] = varLoad[12].split(" | ")
        varLoad[13] = varLoad[13].split(" | ")
        varLoad[14] = varLoad[14].split(" | ")
        varLoad[15] = varLoad[15].split(" | ")

        varLoad[9] = varLoad[9].split(" | ")
        compteur = 0
        for index in varLoad[9]:
            varLoad[9][compteur] = index.split(" ! ")
            varLoad[9][compteur][1] = int(varLoad[9][compteur][1])
            compteur += 1
        for listCoord in varLoad[9]:
            for item in range(0, len(listCoord)):
                if item > 1:
                    listCoord[item] = listCoord[int(str(item))]

        VarC.namePlayer = varLoad[0]
        VarC.avatar = varLoad[1]
        VarC.thirst = varLoad[2]
        VarC.hunger = varLoad[3]
        VarC.sleep = varLoad[4]
        VarC.positionPlayerY = varLoad[5]
        VarC.positionPlayerX = varLoad[6]
        VarC.bag = varLoad[7]
        VarC.limitBag = varLoad[8]
        VarC.itemSlot = varLoad[9]
        VarC.prevMoove = varLoad[10]
        VarC.statutParty = varLoad[11]
        VarC.actionPossible = varLoad[12]
        VarC.directionPossible = varLoad[13]
        VarC.itemActionPossible = varLoad[14]
        VarC.answerStart = varLoad[15]
        VarC.maxThirst = varLoad[16]
        VarC.maxHunger = varLoad[17]
        VarC.maxSleep = varLoad[18]
        VarC.playerAction = int(varLoad[19])
        VarC.playerTurn = int(varLoad[20])
    except:
        print("Votre ficher de config n'a pas été trouvé, veuillez verifier vos dossiers")
        sys.exit()

def checkIsSaved():
    varLoad = []
    with open("C:/Users/PYTHON/Documents/GitHub/Autonomie-projet-1/fileVarTxt/save/save.txt", "r", encoding = "utf-8") as file : 
        fileLoaded = [line for line in file]
        for lineX in fileLoaded:
            lineX = lineX.replace("\n", "")
            varLoad.append(lineX)
    print(f"nom joueur {varLoad[0]}")
    if varLoad[0] != " ":
        return True
    else:
        return False

def loadVarMap():
    mapLoad = []
    with open("C:/Users/PYTHON/Documents/GitHub/Autonomie-projet-1/fileVarTxt/variableMap.txt", "r", encoding = "utf-8") as file : 
        fileLoaded = [line for line in file]
        for lineX in fileLoaded:
            lineX = lineX.replace("\n", "")
            mapLoad.append(list(lineX))
    VarM.mapInATab = mapLoad

def loadScore():
    with open("C:/Users/PYTHON/Documents/GitHub/Autonomie-projet-1/fileVarTxt/score/score.txt", "r", encoding = "utf-8") as file : 
        fileLoaded = [line for line in file]
        for lineX in fileLoaded:
            lineX = lineX.replace("\n", "")
            lineX = lineX.split(" | ")
            print(f"{lineX[0]} à terminé le jeu en {lineX[1]} déplacements et {lineX[2]} actions")

def loadHistoric():
    with open("C:/Users/PYTHON/Documents/GitHub/Autonomie-projet-1/fileVarTxt/historic/historic.txt", "r", encoding = "utf-8") as file : 
        fileLoaded = [line for line in file]
        for lineX in fileLoaded:
            lineX = lineX.replace("\n", "")
            lineX = lineX.split(" | ")
            print(f"Le {lineX[0]} {lineX[1]} à jouer jeu et a {lineX[2]}")

def saveData():
    with open("C:/Users/PYTHON/Documents/GitHub/Autonomie-projet-1/fileVarTxt/save/save.txt", "w", encoding = "utf-8") as file : 
        sacJoin = " | ".join(VarC.bag)
        actionPossibleJoin = " | ".join(VarC.actionPossible)
        itemActionPossibleJoin = " | ".join(VarC.itemActionPossible)
        directionPossibleJoin = " | ".join(VarC.directionPossible)
        reponseDebutJoin = " | ".join(VarC.answerStart)
        itemSlotJoin = []
        for i in range(0, len(VarC.itemSlot)):
            lineX = []
            for o in VarC.itemSlot[i]:
                lineX.append(str(o))
            lineXJoin = " ! ".join(lineX)
            itemSlotJoin.append(lineXJoin)
        itemSlotJoin = " | ".join(itemSlotJoin)
        file.write(f"{VarC.namePlayer}\n")
        file.write(f"{VarC.avatar}\n")
        file.write(f"{VarC.thirst}\n")
        file.write(f"{VarC.hunger}\n")
        file.write(f"{VarC.sleep}\n")
        file.write(f"{VarC.positionPlayerY}\n")
        file.write(f"{VarC.positionPlayerX}\n")
        file.write(f"{sacJoin}\n")
        file.write(f"{VarC.limitBag}\n")
        file.write(f"{itemSlotJoin}\n")
        file.write(f"{VarC.prevMoove}\n")
        file.write(f"{VarC.statutParty}\n")
        file.write(f"{actionPossibleJoin}\n")
        file.write(f"{directionPossibleJoin}\n")
        file.write(f"{itemActionPossibleJoin}\n")
        file.write(f"{reponseDebutJoin}\n")
        file.write(f"{VarC.maxThirst}\n")
        file.write(f"{VarC.maxHunger}\n")
        file.write(f"{VarC.maxSleep}\n")
        file.write(f"{VarC.playerAction}\n")
        file.write(f"{VarC.playerTurn}\n")

def winAddScore(nom, tour, action):
    winner = [f"{nom} | {tour} | {action}\n"]
    with open("C:/Users/PYTHON/Documents/GitHub/Autonomie-projet-1/fileVarTxt/score/score.txt", "r", encoding = "utf-8") as file : 
        fileLoaded = [line for line in file]
        for lineX in fileLoaded:
            winner.append(lineX)
    
    with open("C:/Users/PYTHON/Documents/GitHub/Autonomie-projet-1/fileVarTxt/score/score.txt", "w", encoding = "utf-8") as file :
        for winnerX in winner:
            file.write(winnerX)

def addHistory(nom, game):
    date = datetime.date.today()
    history = [f"{date} | {nom} | {game}\n"]
    with open("C:/Users/PYTHON/Documents/GitHub/Autonomie-projet-1/fileVarTxt/historic/historic.txt", "r", encoding = "utf-8") as file : 
        fileLoaded = [line for line in file]
        for lineX in fileLoaded:
            history.append(lineX)
    
    with open("C:/Users/PYTHON/Documents/GitHub/Autonomie-projet-1/fileVarTxt/historic/historic.txt", "w", encoding = "utf-8") as file :
        compteur = 0
        for historyX in history:
            if compteur < 20:
                file.write(historyX)
            compteur += 1