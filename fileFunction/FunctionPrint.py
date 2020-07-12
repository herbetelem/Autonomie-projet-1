import sys

# rien a expliquer ici ce n'est que des print

def gameWin(nomJouteur, tourJoueur, actionJoueur):
    print()
    print("-----------------VOUS AVEZ GAGNER------------------")
    print()	
	
    print("                         vv")
    print("                     vvv^^^^vvvvv")
    print("                 vvvvvvvvv^^vvvvvv^^vvvvv")
    print("        vvvvvvvvvvv^^^^^^^^^^^^^vvvvv^^^vvvvv")
    print("    vvvvvvv^^^^^^^^^vvv^^^^^^^vvvvvvvvvvv^^^vvv")
    print("  vvvv^^^^^^vvvvv^^^^^^^vv^^^^^^^vvvv^^^vvvvvv")
    print(" vv^^^^^^^^vvv^^^^^vv^^^^vvvvvvvvvvvv^^^^^^vv^")
    print(" vvv^^^^^vvvv^^^^^^vvvvv^^vvvvvvvvv^^^^^^vvvvv^")
    print("  vvvvvvvvvv^^^v^^^vvvvvv^^vvvvvvvvvv^^^vvvvvvvvv")
    print("   ^vv^^^vvvvvvv^^vvvvv^^^^^^^^vvvvvvvvv^^^^^^vvvvvv")
    print("     ^vvvvvvvvv^^^^vvvvvv^^^^^^vvvvvvvv^^^vvvvvvvvvv^v")
    print("        ^^^^^^vvvv^^vvvvv^vvvv^^^v^^^^^^vvvvvv^^^^vvvvv")
    print(" vvvv^^vvv^^^vvvvvvvvvv^vvvvv^vvvvvv^^^vvvvvvv^^vvvvv^")
    print("vvv^vvvvv^^vvvvvvv^^vvvvvvv^^vvvvv^v##vvv^vvvv^^vvvvv^v")
    print(" ^vvvvvv^^vvvvvvvv^vv^vvv^^^^^^_____##^^^vvvvvvvv^^^^")
    print("    ^^vvvvvvv^^vvvvvvvvvv^^^^/\@@@@@@\#vvvv^^^")
    print("         ^^vvvvvv^^^^^^vvvvv/__\@@@@@@\^vvvv^v")
    print("             ;^^vvvvvvvvvvv/____\@@@@@@\vvvvvvv")
    print("             ;      \_  ^\|[  -:] ||--| | _/^^")
    print("             ;        \   |[   :] ||_/| |/")
    print("             ;         \\ ||___:]______/")
    print("             ;          \   ;=; /")
    print("             ;           |  ;=;|")
    print("             ;          ()  ;=;|")
    print("            (()          || ;=;|")
    print("                        / / \;=;\ ")
    print()
    print()
    print(f"Félicitation {nomJouteur}, vous avez gagner cette partie !")
    print(f"Vous avez gagné en fesant {VarC.tourJoueur} deplacements et {VarC.actionJoueur} actions")
    sys.exit()

def gameOver():
    print()
    print("-----------------GAME OVER------------------")
    print()	
    print("                      :::!~!!!!!:.")
    print("                  .xUHWH!! !!?M88WHX:.")
    print("                .X*#M@$!!  !X!M$$$$$$WWx:.")
    print("               :!!!!!!?H! :!$!$$$$$$$$$$8X:")
    print("              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:")
    print("             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!")
    print("             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!")
    print("               !:~~~ .:!M'T#$$$$WX??#MRRMMM!")
    print("               ~?WuxiW*`   `'#$$$$8!!!!??!!!")
    print("             :X- M$$$$       `'T#$T~!8$WUXU~")
    print("            :%`  ~#$$$m:        ~!~ ?$$$$$$")
    print("          :!`.-   ~T$$$$8xx.  .xWW- ~''##*'")
    print(".....   -~~:<` !    ~?T#$$@@W@*?$$      /`")
    print("W$@@M!!! .!~~ !!     .:XUW$W!~ `'~:    :")
    print("#'~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`")
    print(":::~:!!`:X~ .: ?H.!u '$$$B$$$!W:U!T$$M~")
    print(".~~   :X@!.-~   ?@WTWo('*$$$W$TH$! `")
    print("Wi.~!X$?!-~    : ?$$$B$Wu('**$RM!")
    print("$R@i.~~ !     :   ~$$$$$B$$en:``")
    print("?MXT@Wx.~    :     ~'##*$$$$M~")
    print()
    print()

def printRegle():
    print()
    print("Bienvenue sur ce jeux de survie, l'objectif est de ce déplacer sur la carte et d'atteindre different point,")
    print("d'y accomplir des quètes, de les reussir afin de gagner des clefs, et enfin d'atteindre la porte mysterieuse,0")
    print("et de l'ouvrir a l'aide de vos clefs")
    print()
    print("Vous allez voir apparaitre une carte, les # * V ~ et † coresponde a des decorts, vous ne pouvez pas marcher dessus")
    print("# = bord du terrain, * = foret, V = montagne, † = desert")
    print("Pour vous deplacer le jeux vas vous demander ou vous souhaitez aller et vous devrez lui repondre")
    print("Vous pourrez repondre par 'haut', 'bas', 'gauche', droite")
    print("si vous souhaitez revoir vos touche saisissez 'touche'")
    print("pour revoir les règles, saississez 'regle'")
    print()

def printTouche():
    print("Pour vous deplacer saisissez 'z' pour haut, 's' pour bas, 'q' pour gauche, 'd' pour droite vers une direction disponible ! ")

def debutDuJeux():
    print("------------")
    print("----Jeux----")
    print("------------")
    nomJoueur = str(input("Bonjour anonyme joueur, comment te prénommes-tu ? "))
    nomJoueur = nomJoueur.capitalize()
    print()
    print(f"Bonjour {nomJoueur} !")
    print()
    print("Bienvenue sur ce jeu de survie, l'objectif est de ce déplacer sur la carte et d'atteindre different point,")
    print("d'y accomplir des quètes, de les reussir afin de gagner des clefs, et enfin d'atteindre la porte mysterieuse,0")
    print("et de l'ouvrir a l'aide de vos clefs")
    print()
    print("Vous allez voir apparaitre une carte, les # * V ~ et † coresponde a des decorts, vous ne pouvez pas marcher dessus")
    print("# = bord du terrain, * = foret, V = montagne, † = desert")
    print("Pour vous deplacer le jeux vas vous demander ou vous souhaitez aller et vous devrez lui repondre")
    print("Vous pourrez repondre par 'z' pour haut, 's' pour bas, 'q' pour gauche, 'd' pour droite ")
    print("si vous souhaitez revoir vos touche saisissez 'touche'")
    print("pour revoir les règles, saississez 'regle'")
    return nomJoueur

def printMystere():
    print("                    ___")
    print("                   /III\\")
    print("                  /{= =}\__")
    print("                  |_\-/_|  \\")
    print("             jjs  |-| |-|{ |")
    print("                 /-_--_'-nn/")
    print("                nnn/  nnn|")

def printBag():
    print("                :*-")
    print("            =--+    =: *:")
    print("           -=           :-@")
    print("            *#:        :#")
    print("            -++:+=@*=@-")
    print("         -@:  #   #    *+")
    print("       -#-              -#")
    print("      #+                 -#")
    print("     @-                   #-")
    print("    @-                    *+")
    print("   #:                     ++")
    print("  **                      ++")
    print(" -#                       #-")
    print(" @                          +=")
    print("+=                           **")
    print("+=                            #")
    print(" #:                          #")
    print("  *@:                     +@#")
    print("     :#=*+++**=***+*+:     ")

def printRegleMystere():
    print()
    print("En haut de la falaise en bordure de forêt, pas très loin de la plage, \ntu découvres la statue d’un Sphinx avec une grosse clé en bronze posée sur les pattes.")
    print("Lorsque tu t’en approches, les yeux de la statue s’illuminent et une voix se fait entendre :")
    print("« Bonjour explorateur ! Pour ouvrir la porte de la montagne, atteindre le cœur de l’île \net rejoindre tes compagnons, tu devras tout d’abord prouver ta valeur individuelle \nen gagnant les 3 clés que tu obtiendras en relevant les défis appropriés. Ceci est le premier d’entre eux. »")
    print("Il est bien entendu impossible de prendre la clé (qui semble collée aux pattes du Sphinx) \ntant que le défi n’est pas gagné.")
    print("La voix poursuit : « 3 fois de suite, tu devras deviner le nombre que j’ai en tête, \ntu as 20 essais maximum pour tous les trouver, es-tu prêt ? »")

def printCesar():
    print("             / ,(//            /((. /         "    )
    print("           *((*                     ((          "  )
    print("         (( /*((/               ./((., /*         ")
    print("         ((,*(((                  ((/..((         ")
    print("       ,/*    *                   *.  . /(        ")
    print("        ((,,(/.                    /(( /(/        ")
    print("       ((/   /(                   ,// . //*       ")
    print("         ((,,  (( (            ( ((  /*//         ")
    print("         #(((. ( (/( (*    /( (/, (.*(((#         ")
    print("             ,**.,*  ##*  ((( *.* */.             ")
    print("             .(*  */( *(  (,.((   */           "   )
    print("                 ./* (      / */     ")

def printRegleCesar():
    print("Ce jeux est galere, demerde-toi mais si tu gagne tu aura la clef d'argent")

def printFizzBuzz():
    print("                      __------__")
    print("                    /~          ~\ ")
    print("                   |    //^\//^\|    ")      
    print("                 /~~\  ||  o| |o|:~\ ") 
    print("                | |6   ||___|_|_||:| ")     
    print("                 \__.  /      o  \/' ")   
    print("                  |   (       O   ) ")
    print("         /~~~~\    `\  \         /")
    print("        | |~~\ |     )  ~------~`\ ")
    print("       /' |  | |   /     ____ /~~~)\ ")
    print("      (_/'   | | |     /'    |    ( |")
    print("             | | |     \    /   __)/ \ ")
    print("             \  \ \      \/    /' \   `\ ")
    print("               \  \|\        /   | |\___|")
    print("                 \ |  \____/     | |")
    print("                 /^~>  \        _/ <")
    print("                |  |         \       \ ")
    print("                |  | \        \        \ ")
    print("                -^-\  \       |        )")
    print("                     `\_______/^\______/")

def printRegleFizz():
    print("Regarde il n'y a rien a faire")










