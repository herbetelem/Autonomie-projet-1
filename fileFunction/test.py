
def saveData():
    with open("C:/Users/PYTHON/Documents/GitHub/Autonomie-projet-1/fileVarTxt/save/save.txt", "w", encoding = "utf-8") as file : 
        file.write("Premier test d'écriture dans un fichier via Python\n")
        file.write("Deuxieme test d'écriture dans un fichier via Python\n")
        file.write("Troisieme test d'écriture dans un fichier via Python\n")


saveData()