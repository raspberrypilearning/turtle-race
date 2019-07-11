## Aufgabe: Das Rennen kann losgehen!

Nun kommen wir zum spaßigen Teil. Fügen wir einige Rennschildkröten hinzu. Es wäre wirklich langweilig, wenn die Schildkröten jedes Mal das Gleiche tun würden, also werden wir sie in jeder Runde eine zufällige Anzahl von Schritten bewegen. Die Schildkröte gewinnt, die in 100 Runden am weitesten kommt.

+ Wenn du Befehle wie `forward (20)` verwendest, bewegst du eine einzelne Schildkröte. Du kannst aber weitere Schildkröten erstellen. Füge den folgenden Code am Ende deines Skripts hinzu (stelle sicher, dass der Anfang nicht eingerückt ist):
    
    ![Screenshot](images/race-red.png)
    
    In der ersten Zeile wird eine Schildkröte namens "Ada" erstellt. Die nächste Zeile legt die Farbe und Form der Schildkröte fest. Jetzt sieht sie wirklich aus wie eine Schildkröte!

+ Lass uns die Schildkröte an die Startlinie schicken:
    
    ![screenshot](images/race-start.png)

+ Jetzt kannst du die Schildkröte zum Rennen bringen, indem du sie eine zufällige Anzahl von Schritten bewegst. Du wirst die die `randint` Funktion aus der Python `random` benötigen. Füge diese `import` Zeile an den Anfang des Skripts hinzu:
    
    ![Screenshot](images/race-randint.png)

+ Die `randint` Funktion produziert eine zufällige Ganzzahl (gerade Zahl) zwischen den gewählten Werten. Die Schildkröte bewegt sich in jeder Runde 1, 2, 3, 4 oder 5 Schritte vorwärts.
    
    ![screenshot](images/race-random.png)

+ Eine Schildkröte allein bedeutet kein großes Rennen! Fügen wir noch eine hinzu:
    
    ![screenshot](images/race-blue.png)
    
    Beachte, dass der Code zum Bewegen der blauen Schildkröte **die gleiche** `for` Loop (Zählschleife) nutzen muss, wie der Code, der die rote Schildkröte bewegt hat, damit beide Schildkröten jede Runde eine Bewegung ausführen.