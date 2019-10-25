## Piste de course

Tu vas créer un jeu avec des tortues de course. D'abord, elles auront besoin d'une piste de course.

+ Ouvre le modèle de Trinket Python vierge : <a href="https://trinket.io/python/f69e360eb8" target="_blank">trinket.io/python/f69e360eb8</a>.

+ Ajoute le code suivant pour dessiner une ligne à l'aide de "turtle":
    
    ![capture d'écran](images/race-forward.png)

+ Utilisons maintenant la tortue pour dessiner des marques de piste pour la course.
    
    La fonction turtle `write` écrit le texte à l'écran.
    
    Essaie-le:
    
    ![capture d'écran](images/race-markings1.png)

+ Maintenant, tu dois remplir les numéros entre les deux pour créer des marquages:
    
    ![capture d'écran](images/race-markings2.png)

+ As-tu remarqué que ton code est très répétitif? La seule chose qui change est le nombre à écrire.
    
    Il y a une meilleure façon de faire cela en Python. Tu peux utiliser une boucle `for`.
    
    Mets à jour ton code pour utiliser une boucle `for`:
    
    ![capture d'écran](images/race-for.png)

+ Hmm, cela n'imprime que des nombres allant jusqu'à 4. En Python `range(5)` renvoie cinq nombres, allant de 0 à 4. Pour que le code retourne également 5, tu dois utiliser `range(6)`:
    
    ![capture d'écran](images/race-range.png)

+ Nous pouvons maintenant dessiner des marques de piste. La tortue commence aux coordonnées (0,0) au milieu de l'écran.
    
    Déplace la tortue en haut à gauche à la place:
    
    ![capture d'écran](images/race-goto.png)

+ Ah, tu voudras d'abord lever le stylo!
    
    ![capture d'écran](images/race-penup.png)

+ Au lieu de dessiner une ligne horizontalement, dessinons des lignes verticales pour créer une piste:
    
    ![capture d'écran](images/race-lines.png)
    
    `right(90)` fait tourner la tortue à droite de 90 degrés (un angle droit.) Avance `forward(10)` avant de poser le stylo, laisse un petit espace entre le nombre et le début de la ligne. Après avoir tracé la ligne, relève le stylo et va `backward(160)` la longueur de la ligne plus l'écart.

+ Cela semble plus net si tu centres les chiffres:
    
    ![capture d'écran](images/race-center.png)

+ Et tu peux accélérer la tortue pour qu'elle s'approche plus vite:
    
    ![capture d'écran](images/race-speed.png)