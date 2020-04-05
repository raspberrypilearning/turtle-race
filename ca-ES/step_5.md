## Tortugues corredores

Ara una mica més de diversió. Afegim algunes tortugues de cursa. Seria realment avorrit si les tortugues fessin el mateix cada vegada, per la qual cosa es mouran un nombre aleatori de passos cada torn. La tortuga guanyadora serà la que arribi més lluny en 100 voltes.

+ Quan fas servir comandes com `forward(20)` estàs fent servir una única tortuga. Però pots crear més tortugues. Afegeix el següent codi al final del teu programa (però assegura't que no tingui sagnat):
    
    ![captura de pantalla](images/race-red.png)
    
    La primera línia crea una tortuga anomenada "ada". Les següents línies estableixen el color i la forma de la tortuga. Ara realment sembla una tortuga!

+ Anem a enviar la tortuga a la línia de sortida:
    
    ![captura de pantalla](images/race-start.png)

+ Ara has de fer que la tortuga corri movent-se un nombre aleatori de passos alhora. Necessitaràs la funció `randint` de la biblioteca de Python `random`. Afegeix aquesta línia `import` a la part superior del teu codi:
    
    ![captura de pantalla](images/race-randint.png)

+ La funció `randint` retorna un enter aleatori (un número sencer) entre els valors escollits. La tortuga es mourà endavant 1, 2, 3, 4, o 5 passes a cada torn.
    
    ![captura de pantalla](images/race-random.png)

+ Una tortuga no és gaire per fer una cursa! Afegim-ne una altra:
    
    ![captura de pantalla](images/race-blue.png)
    
    Pren nota que el codi per moure la tortuga blava necessita estar **al mateix** bucle `for` que el codi per moure la tortuga vermella de manera que cadascuna faci un moviment cada torn.