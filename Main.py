import fileFunction.variableMap as variableMap
import fileFunction.FunctionAboutBag as FBag
import fileFunction.FunctionAboutMap as FMap
import fileFunction.FunctionMain as FMain
import fileFunction.FunctionPrint as FPrint
import fileFunction.variableClassic as VarC
import os
clear = lambda: os.system('cls')


def Main():
    # Call all the function
    VarC.nomJoueur = FPrint.debutDuJeux()
    reponse = ["oui", "yes", "si"]
    question = str(input("Est ce que vous êtes pret ? "))
    while question not in reponse:
        question = str(input("Prenez votre temps et dite moi quand vous serez prêt ! "))

    print()

    VarC.itemSlot = FBag.createItemSlot(VarC.itemSlot)
    clear()
    variableMap.mapInATab = FMap.addItemPointOnMap(variableMap.mapInATab, VarC.itemSlot)
    FMap.printMap(VarC.positionJoueurY, VarC.positionJoueurX, variableMap.mapInATab)

    print()
    while VarC.statutParti == "ok":
        action = input("Que souhaitez vous faire ? ")
        
        while action not in VarC.actionPossible:
            action = input(f"Vous pouvez {VarC.actionPossible}")
        
        if action == "regle":
            FPrint.printRegle()
        
        elif action == "touche":
            FPrint.printTouche()
        
        elif action == "bouger":
            FMain.bouger()

        elif action == "dormir":
            FMain.dormir()
        
        elif action == "inventaire":
            FMain.inventaire()

        if VarC.statFaim <= 0 or VarC.statSoif <= 0 or VarC.statSommeil <= 0:
            VarC.statutParti = "ko"

        FMap.endTurn()

    if VarC.statutParti == "ko":
        FPrint.gameOver()


if __name__ == "__main__":
    Main()
