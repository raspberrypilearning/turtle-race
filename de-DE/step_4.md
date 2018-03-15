## Schildkröten Wettrennen

Jetzt wird es lustig. Lass uns ein paar konkurrierende Renn-Schildkröten hinzufügen. Es wäre wirklich langweilig, wenn alle Schildkröten die ganze Zeit immer  das Gleiche machen würden, deshalb sollen sie jedes Mal, wenn sie am Zug sind, eine zufällig ausgewählte Anzahl von Schritten nach vorn gehen. Der Gewinner ist die Schildkröte, die nach 100 Mal am weitesten vorne liegt. 

+ Wenn du Befehle wie `forward(20)` (vorwärts(20)) gibst, benutzt du eine einzige Schildkröte. Du kannst jedoch noch mehr Schildkröten herstellen. Füge den folgenden Code zum Ende deines Scripts hinzu (achte aber darauf, dass er nicht eingerückt ist):

  ![screenshot](images/race-red.png)

  Die erste Linie erstellt eine Schildkröte namens 'ada'. Die nächste Linie stellt die Farbe und Form der Schildkröte ein. Jetzt sieht es doch wirklich wie eine Schildkröte aus!
  
+ Lass uns diese Schildkröte zur Startlinie schicken:

  ![screenshot](images/race-start.png)
   
+ Jetzt musst du nur noch die Schildkröte dazu bringen, dass sie rennt, indem sie sich jeweils eine zufällig ausgewählte Anzahl an Schritten vorwärts bewegt. Du brauchst die `randint` Funktion aus der Python `random` (zufälig ausgewählt) Bibliothek. Füge diese `import` (importieren) Line oben zu deinem Script hinzu:

  ![screenshot](images/race-randint.png)

+ Die `randint` Funktion bietet ein zufällig ausgewähltes Integer (Ganzzahl) zwischen den ausgewählten Werten. Die Schildkröte bewegt sich bei jedem Zug 1, 2, 3, 4 oder 5 Schritte nach vorne. 

  ![screenshot](images/race-random.png)
  
+ Aber eine Schildkröte allein macht noch lange kein Rennen! Lass uns eine weitere Schildkröte hinzufügen:

  ![screenshot](images/race-blue.png)
  
  Beachte bitte, dass der Code zum Vorwärtsbewegen der blauen Schildkröte in __der gleichen__ `for` (für) Schleife sein muss wie der Code zum Vorwärtsbewegen der roten Schildkröte, damit jede davon sich bei jedem Zug nach vorne bewegen kann. 
  


