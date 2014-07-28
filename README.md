Towers_of_Hanoi
===============

Towers of Hanoi game in Python


But du jeu: Faire passer tous les anneaux de la première à la dernière tour en un minimum de coups.

Règles du jeu : Les anneaux doivent rester dans l'ordre décroissant.


#DEBUT DU PROGRAMME#

Lorsqu'on lance le programme le menu principal apparaît proposant plusieurs options:

- Nouvelle partie (Cela commencera une nouvelle partie)
- Charger une partie (Affiche une fenêtre avec la liste de toutes les parties sauvegardées et à la date auquel elles on été sauvegardées, l'utilisateur peut sélectionner la sauvegarde de son choix avec la souris et double-cliquer dessus pour la lancer)
- Options (Affiche une fenêtre contenant certains paramètres du programme que l'utilisateur peut modifier. Ex : couleur et taille des tours, des anneaux, du halo de sélection etc...)
- Quitter (On ferme le programme)

#EN JEU#

Lorsqu'on lance une nouvelle partie, 3 tours apparaissent à l'écran l'une après l'autre.

Un message indique alors à quelle difficulté l'utilisateur souhaite jouer (Facile, Normal, Difficile, Expert).

Après avoir sélectionné la difficulté de son choix, des anneaux apparaissent sur la 1ere tour:

- 5 anneaux en difficulté facile
- 8 anneaux en difficulté normale
- 10 anneaux en difficulté difficile
- 12 anneaux en difficulté expert

Pour faire passer un anneau d'une tour à un autre, l'utilisateur devra cliquer à la souris sur la tour contenant l'anneau qu'il souhaite déplacer puis sur la tour qui recevra cet anneau.

Lorsque l'utilisateur sélectionne une des tours pour jouer, un halo de couleur entoure la tour et le 1er anneau confirmant ainsi la sélection.

A chaque fois que l’utilisateur réalise une action contraire aux règles du jeu, le programme, met le jeu en pause, empêche son action de se dérouler et une fenêtre lui indique "Vous ne pouvez pas faire ça". Pour fermer la fenêtre et reprendre le jeu il faudra cliquer sur "OK".

Un compteur visible sera présent en jeu et comptera le temps ainsi que chaque déplacement d'anneau.

Lorsque l'utilisateur gagne une partie, une fenêtre apparaît lui indiquant qu'il a gagné et affichera son temps et le nombre total des déplacements d'anneaux réalisés. On lui demandera aussi si il souhaite rejouer avec la même difficulté ou avec une difficulté différente. Il pourra aussi revenir au menu principal.

A tout moment de la partie un bouton "Menu" sera présent. Quand l'utilisateur clique dessus, le programme met le jeu en pause et affichera à l'écran un menu:

- Revenir à la partie (Le programme enlève la pause et on revient à la partie en cours)
- Sauvegarder la partie (Sauvegarde la partie en mémoire)
- Charger la partie (Même fenêtre que dans le menu principal)
- Options (Même fenêtre que dans le menu principal)
- Menu principal (Une fenêtre apparaît demandant à l'utilisateur si il souhaite oui ou non sauvegarder sa partie. Si "oui" le programme sauvegarde sa partie et reviens au menu principal, si  "non" il quitte la partie en cours et reviens au menu principal)
- Quitter (Une fenêtre apparaît demandant à l'utilisateur si il souhaite oui ou non sauvegarder sa partie. Si "oui" le programme sauvegarde sa partie et ferme le programme, si  "non" il quitte la partie en cours et ferme le programme)
