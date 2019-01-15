## Tartarughe da corsa

Ora arriva la parte divertente. Aggiungiamo alcune tartarughe da corsa. Sarebbe davvero noioso se le tartarughe facessero la stessa cosa ogni volta; per questo si muoveranno di numero casuale di passi ad ogni turno. La vincitrice è la tartaruga che arriva più lontana in 100 turni.

+ Quando usi comandi come `forward(20)` stai usando una sola tartaruga. Ma puoi crearne di più. Aggiungi il seguente codice alla fina del tuo codice (assicurati che non sia identato):
    
    ![screenshot](images/race-red.png)
    
    La prima linea crea una tartaruga chiamata 'ada'. Le linee successive impostano il colore e la forma della tartaruga. Ora sembra davvero una tartaruga!

+ Mandiamola alla linea d'inizio:
    
    ![screenshot](images/race-start.png)

+ Ora dovrai far muovere la tartaruga da corsa di un numero casuale di passi ogni volta. Avrai bisogna della funzione `randint` della libreria di Python `random`. Aggiungi questa istruzione `import` in cima al tuo codice:
    
    ![screenshot](images/race-randint.png)

+ La funzione `randint` dà in output un numero intero casuale compreso tra i valori scelti. La tartaruga si muoverà in avanti di 1, 2, 3, 4 o 5 passi ad ogni turno.
    
    ![screenshot](images/race-random.png)

+ Non è una gran bella gara con una tartaruga! Aggiungiamone un'altra:
    
    ![screenshot](images/race-blue.png)
    
    Nota che il codice per muovere la tartaruga blu deve essere **nello stesso** ciclo `for` del codice che muove quella rossa, così che ognuna faccia una mossa ad ogni turno.