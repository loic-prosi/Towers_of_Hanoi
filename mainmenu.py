'''
Programme qui permet à l'utilisateur de jouer au jeu des tours de Hanoï.

Le plateau de jeu contien 3 tours, une contient des anneaux et les 2 autres
sont vides.

Le joueur commence avec une tour de n anneaux et doit les déplacer d'une tour
à l'autre en gardant l'ordre décroissant de ceux-ci.

On ne peut déplacer qu'un anneau à la fois et on ne peut pas mettre un anneau
de diametre supérieur sur un autre de diametre inférieur.

Le jeu est terminé lorsqu'on a déplacé l'intégralité d'une pile d'anneau vers
une autre tour.
'''

###########
#MAIN MENU#
###########

print('-'*30, 'TOWERS OF HANOI', '-'*30,
      '\n'*2, 'MAIN MENU', '\n'*2,
      '1. NEW GAME \n',
      '2. LOAD GAME\n',
      '3. OPTIONS \n',
      '4. QUIT \n')

while True:
    
    try:
        choice_main_menu = int(input('Choice (1, 2, 3 or 4): '))
    except:
        continue

    if choice_main_menu not in range(1,5):
        continue

    elif choice_main_menu == 1:
        import newgame
        
    elif choice_main_menu == 2:
        import loadgame

    elif choice_main_menu == 3:
        import options

    else:
        break


    

    












    
