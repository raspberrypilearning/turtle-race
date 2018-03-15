## Percorso di gara

Creerai un gioco con tartarughe che gareggiano. Per prima cosa, avranno bisogno di un percorso di gara.

+ Apri il modello vuoto di Python Trinket: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Aggiungi il seguente codice per disegnare una linea usando  'turtle':

  ![screenshot](images/race-forward.png)

+ Ora usiamo la tartaruga per disegnare slcune linee del percorso.

  La funzione 'write' della tartaruga scrive il testo allo schermo.

  Prova:

  ![screenshot](images/race-markings1.png)

+ Ora dovrai riempire i numeri in mezzo per creare le linee:

  ![screenshot](images/race-markings2.png)

+ Hai notato che il tuo codice è molto ripetitivo? L'unica cosa che cambia è il numero da scrivere.

  C'è una maniera migliore per farlo in Python. Puoi usare il loop 'for'.

  Aggiorna il tuo codice per usare un loop 'for':

  ![screenshot](images/race-for.png)

+ Vediamo un po', quello stampa solo numeri fino a 4. In Python 'range(5)' restituisce cinque numeri, da 0 a 4. Per fare in modo che restituisca anche il numero 5, ddovrai usare 'range(6)':

  ![screenshot](images/race-range.png)

+ Ora possiamo tracciare alcune linee di percorso. La tartaruga inizia alle coordinate (0,0) nel mezzo dello schermo.

  Muovi invece la tartaruga in alto a sinistra:

  ![screenshot](images/race-goto.png)

+ Ah, prima dovrai sollevare la penna!

  ![screenshot](images/race-penup.png)

+ Invece di disegnare una linea in orizzontale, disegniamo delle linee verticali per creare un percorso:

  ![screenshot](images/race-lines.png)

  `right(90)` fa girare la tartaruga a destra di 90 gradi (un angolo retto.) Muovere 'forward(10)' prima di mettere giù la penna lascia un piccolo vuoto tra il numero e l'inizio della riga. Dopo aver disegnato la linea, solleva la penna e vai 'backward(160)' la lunghezza della linea più il vuoto.

+ Se centri i numeri sembrerà più ordinato:

  ![screenshot](images/race-center.png)

+ E puoi anche accelerare la tartaruga così che disegni più velocemente:

  ![screenshot](images/race-speed.png)
