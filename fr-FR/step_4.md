## La course de tortues

Maintenant voici la partie amusante. Ajoutons quelques tortues de course. Ce serait vraiment ennuyant si les tortues faisaient la même chose alors elles se déplaceront d'une distance aléatoire à chaque tour. La tortue gagnante est celle qui se rend le plus loin en 100 tours.

+ Lorsque tu utilises des commandes comme `forward(20)`, tu utilises une tortue unique. Tu peux aussi créer plus de tortues. Ajoute le code suivant à la fin de ton script (assure toi qu'il est aligné complétement à gauche).


  ![screenshot](images/race-red.png)

  La première ligne crée une tortue nommée 'ada'. Les lignes suivante règlent la couleur et la forme de la tortue. Maintenant elle ressemble vraiment à une tortue!

+ Déplaçons la tortue à la ligne de départ:

  ![screenshot](images/race-start.png)

+ Tu dois maintenant faire déplacer la tortue d'une distance aléatoire. Tu auras besoin de la fonction `randint` de la librarie Python `random`. Ajoute la ligne d'importation suivante au haut de ton script:

  ![screenshot](images/race-randint.png)

+ La fonction `randint` retourne un nombre entier ('integer') compris entre les valeurs choisies. La tortue avancera de 1, 2, 3, 4 ou 5 pas à chaque tour.

  ![screenshot](images/race-random.png)

+ Une tortue seule ne fait pas une course très intéressante! Ajoutons-en une autre:

  ![screenshot](images/race-blue.png)

  Note que le code pour déplacer la tortue bleue doit être dans __la même__ boucle `for` que le code pour déplacer la tortue rouge pour qu'elles se déplacent toutes les deux à chaque tour.


