

def loadVarMap():
    mapLoad = []
    with open("C:/Users/PYTHON/Documents/GitHub/Autonomie-projet-1/fileVarTxt/variableMap.txt", "r", encoding = "utf-8") as file : 
        fileLoaded = [line for line in file]
        for lineX in fileLoaded:
            lineX = lineX.replace("\n", "")
            mapLoad.append(list(lineX))
    print(mapLoad)

loadVarMap()