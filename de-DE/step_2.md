## Rennstrecke

Du wirst ein Spiel mit Schildkröten erstellen, die an einem Wettrennen teilnehmen. Als erstes wird eine Rennstrecke benötigt.

+ Das leere Python Vorlage- Trinket öffnen: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>. 

+ Füge den folgenden Code hinzu, um eine Linie mit Hilfe der 'turtle' (Schildkröte) zu zeichnen:

  ![screenshot](images/race-forward.png)
   
+ Lass uns jetzt die Schildkröte benutzen, um die Markierung für die Rennstrecke einzuzeichnen. 

  Die `write` (schreiben) Funktion der Schildkröte schreibt den Text auf den Bildschirm. 
  
  Probiere es mal aus:

  ![screenshot](images/race-markings1.png)
  
+ Jetzt musst du nur die Zahlen dazwischen setzen, um die Markierung zu erstellen:

  ![screenshot](images/race-markings2.png)
  
+ Hast du gemerkt, dass sich der Code immer wiederholt? Das Einzige, das sich ändert, ist die Zahl, die geschrieben werden muss.

  Es gibt eine bessere Methode dies in Python zu tun. Du kannst eine `for` (für) Schleife benutzen. 
  
  Aktualisiere deinen Code, um eine `for` (für) Schleife zu benutzen:
  
  ![screenshot](images/race-for.png)
   
+ Hmm, das druckt nur die Zahlen bis Nr. 4. In Python bietet `range(5)` (Bereich(5)) nur fünf Zahlen: von 0 bis 4. Damit du auch die Zahl 5 erhältst, musst du `range(6)` (Bereich(6)) angeben:

  ![screenshot](images/race-range.png)
   
+ Jetzt können wir die Rennstreckenmarkierung einzeichnen. Die Schildkröte beginnt bei den Koordinaten (0,0) in der Mitte des Bildschirms. 

  Bewege die Schildkröte statt dessen nach oben links:
  
  ![screenshot](images/race-goto.png)

+ Oh, du musst als erstes den Stift hochheben!

  ![screenshot](images/race-penup.png)
  
+ Anstatt eine horizontale Linie zu zeichnen, lass uns vertikale Linien zeichnen, um die Rennstrecke zu erstellen:

  ![screenshot](images/race-lines.png)
  
  `right(90)` (rechts(90)) bringt die Schildkröte dazu, sich 90 Grad nach rechts zu drehen (ein rechter Winkel). Nach `forward(10)` (vorwärts(10)) gehen, ehe der Stift abgesetzt wird, hinterlässt eine kleine Lücke zwischen der Zahl und dem Start der Linie. Nach dem Zeichnen der Linie, hebst du den Stift hoch und gehst `backward(160)` (zurück(160)), die Länge der Linie plus die Lücke. 
  
+ Es sieht sauberer aus, wenn du die Zahlen in die Mitte setzt:

  ![screenshot](images/race-center.png)

+ Und du kannst die Geschwindigkeit der Schildkröte steigern, damit sie schneller zeichnet:

  ![screenshot](images/race-speed.png)
