## Race track

Crearàs un joc amb tortugues corredores. El primer que necessitaran és un circuit.

+ Obre la plantilla Python en blanc a Trinket: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Afegeix el codi següent per dibuixar una línia mitjançant la 'tortuga':
    
    ![screenshot](images/race-forward.png)

+ Ara utilitzarem la tortuga per dibuixar algunes marques de pista per a la cursa.
    
    La funció `write` de la tortuga escriu text a la pantalla.
    
    Prova-ho:
    
    ![screenshot](images/race-markings1.png)

+ Ara has d'omplir amb números per enumerar les marques:
    
    ![screenshot](images/race-markings2.png)

+ T'has adonat que el teu codi és molt repetitiu? L’únic que canvia és el número a escriure.
    
    Hi ha una manera millor de fer això a Python. Pots utilitzar un bucle `for`.
    
    Actualitza el teu codi per utilitzar un bucle `for`:
    
    ![screenshot](images/race-for.png)

+ Hmm, això només imprimeix nombres fins a 4. Python `rang(5)` retorna cinc números, de 0 a 4. Per obtenir-ne fins al 5, hauries de fer servir ` rang(6) `:
    
    ![screenshot](images/race-range.png)

+ Ara podem dibuixar algunes marques de pistes. La tortuga comença a les coordenades (0,0) a la meitat de la pantalla.
    
    Millor que moguis la tortuga a la part superior esquerra:
    
    ![screenshot](images/race-goto.png)

+ Ah, primer voldràs aixecar el llapis!
    
    ![screenshot](images/race-penup.png)

+ En lloc de dibuixar una línia horitzontalment, dibuixem línies verticals per crear una pista:
    
    ![screenshot](images/race-lines.png)
    
    `right(90)` fa que la tortuga giri a la dreta 90 graus (un angle recte). Avançant `forward(10)` abans d'abaixar el llapis deixa un petit buit entre el nombre i l’inici de la línia. After drawing the line you lift up the pen and go `backward(160)` the length of the line plus the gap.

+ It looks neater if you centre the numbers:
    
    ![screenshot](images/race-center.png)

+ And you can speed up the turtle so it draws faster:
    
    ![screenshot](images/race-speed.png)