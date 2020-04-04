## Race track

Crearàs un joc amb tortugues corredores. El primer que necessitaran és un circuit.

+ Obre la plantilla Python en blanc a Trinket: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Afegeix el codi següent per dibuixar una línia mitjançant la 'tortuga':
    
    ![captura de pantalla](images/race-forward.png)

+ Ara utilitzarem la tortuga per dibuixar algunes marques de pista per a la cursa.
    
    La funció `write` de la tortuga escriu text a la pantalla.
    
    Prova-ho:
    
    ![captura de pantalla](images/race-markings1.png)

+ Ara has d'omplir amb números per enumerar les marques:
    
    ![captura de pantalla](images/race-markings2.png)

+ T'has adonat que el teu codi és molt repetitiu? L’únic que canvia és el número a escriure.
    
    Hi ha una manera millor de fer això a Python. Pots utilitzar un bucle `for`.
    
    Actualitza el teu codi per utilitzar un bucle `for`:
    
    ![captura de pantalla](images/race-for.png)

+ Hmm, això només imprimeix nombres fins a 4. A Python `rang(5)` retorna cinc números, de 0 a 4. Per obtenir-ne fins al 5, hauries de fer servir ` rang(6) `:
    
    ![captura de pantalla](images/race-range.png)

+ Ara podem dibuixar algunes marques de pistes. La tortuga comença a les coordenades (0,0) a la meitat de la pantalla.
    
    Millor que moguis la tortuga a la part superior esquerra:
    
    ![captura de pantalla](images/race-goto.png)

+ Ah, primer voldràs aixecar el llapis!
    
    ![captura de pantalla](images/race-penup.png)

+ En lloc de dibuixar una línia horitzontalment, dibuixem línies verticals per crear una pista:
    
    ![captura de pantalla](images/race-lines.png)
    
    `right(90)` fa que la tortuga giri a la dreta 90 graus (un angle recte). Avançant `forward(10)` abans d'abaixar el llapis deixa un petit buit entre el nombre i l’inici de la línia. Després de traçar la línia, puja el llapis i ves `backward(160)` la longitud de la línia més el buit.

+ Es veu millor si centres els números:
    
    ![captura de pantalla](images/race-center.png)

+ I pots accelerar la tortuga perquè es dibuixi més ràpidament:
    
    ![captura de pantalla](images/race-speed.png)