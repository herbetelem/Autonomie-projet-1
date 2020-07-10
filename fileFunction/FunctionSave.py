# coding: utf-8
variable = []
with open("C:/Users/PYTHON/Documents/GitHub/Autonomie-projet-1/fileFunction/data.txt", "r", encoding = "utf-8") as map : 
    displayMap = [line for line in map]
    for test in displayMap:
        if len(test) > 2:
            test = test.replace("\n","")
            print(test)

def loadVarClassic():
    