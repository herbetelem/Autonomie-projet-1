# coding: utf-8
import json
import fileFunction.variableClassic as VarC


def loadVarClassic():
    varLoad = []
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
    VarC.nomJoueur = varLoad[0]
    VarC.avatar = varLoad[1]
    VarC.statSoif = varLoad[2]
    VarC.statFaim = varLoad[3]
    VarC.statSommeil = varLoad[4]
    VarC.positionJoueurY = varLoad[5]
    VarC.positionJoueurX = varLoad[6]
    VarC.sac = varLoad[7]
    VarC.limitSac = varLoad[8]
    VarC.itemSlot = varLoad[9]
    VarC.prevMoove = varLoad[10]
    VarC.statutParti = varLoad[11]
    VarC.actionPossible = varLoad[12]
    VarC.directionPossible = varLoad[13]
    VarC.itemActionPossible = varLoad[14]
    VarC.reponseDebut = varLoad[15]