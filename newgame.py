'''
Module qui permet de choisir la difficulté et de lancer une nouvelle partie.
'''

##########
#NEW GAME#
##########

print('\n', 'NOUVELLE PARTIE',
      '\n'*2, ' CHOISIR DIFFICULTE', '\n'*2,
      '1. FACILE \n',
      '2. NORMAL \n',
      '3. DIFFICILE \n',
      '4. EXPERT \n')

t1 = []
t2 = []
t3 = []
moves = 0

while True:
    
    try:
        choice_difficulty = int(input('Choisir (1, 2, 3 ou 4): '))
    except:
        print('Erreur syntaxe ! Recommencez')
        continue

    if choice_difficulty not in range(1,5):
        print('Erreur syntaxe ! Recommencez')
        continue

    elif choice_difficulty == 1:
        t1 = [1, 2, 3, 4, 5]
        print("Tour 1 :", t1)
        print("Tour 2 :", t2)
        print("Tour 3 :", t3)
        break

    elif choice_difficulty == 2:
        t1 = [1, 2, 3, 4, 5, 6, 7, 8]
        print("Tour 1 :", t1)
        print("Tour 2 :", t2)
        print("Tour 3 :", t3)
        break

    elif choice_difficulty == 3:
        t1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print("Tour 1 :", t1)
        print("Tour 2 :", t2)
        print("Tour 3 :", t3)
        break

    else:
        t1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
        print("Tour 1 :", t1)
        print("Tour 2 :", t2)
        print("Tour 3 :", t3)
        break

while True:

    print('Déplacements :', moves, '\n')
    moves += 1

    try:    
        source = int(input("Retirer un disque de quelle tour ?: "))
    except:
        print('Erreur syntaxe ! Recommencez')
        continue
    
    if source not in range(1,4):
        print('Erreur syntaxe ! Recommencez')
        continue

    elif source == 1:
        disc = t1.pop(0)
        print("Tour 1 :", t1)
        print("Tour 2 :", t2)
        print("Tour 3 :", t3)

    elif source == 2:
        disc = t2.pop(0)
        print("Tour 1 :", t1)
        print("Tour 2 :", t2)
        print("Tour 3 :", t3)

    else:
        disc = t3.pop(0)
        print("Tour 1 :", t1)
        print("Tour 2 :", t2)
        print("Tour 3 :", t3)

    try:    
        destination = int(input("Mettre le disque sur quelle tour ?: "))
    except:
        print('Erreur syntaxe ! Recommencez')
        continue

    if destination not in range(1,4):
        print('Erreur syntaxe ! Recommencez')
        continue

    elif destination == 1:
        t1.insert(0, disc)
        print("Tour 1 :", t1)
        print("Tour 2 :", t2)
        print("Tour 3 :", t3)

    elif destination == 2:
        t2.insert(0, disc)
        print("Tour 1 :", t1)
        print("Tour 2 :", t2)
        print("Tour 3 :", t3)

    else:
        t3.insert(0, disc)
        print("Tour 1 :", t1)
        print("Tour 2 :", t2)
        print("Tour 3 :", t3)

    if (t1 != [] and disc > t1[0]) or (t2 != [] and disc > t2[0]) or \
       (t3 != [] and disc > t3[0]):
        print('Erreur')




        





