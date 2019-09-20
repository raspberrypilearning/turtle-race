## Schildkröten Wettrennen

Nun kommen wir zum spaßigen Teil. Lass uns ein paar Rennschildkröten hinzufügen. Es wäre wirklich langweilig, wenn die Schildkröten jedes Mal das Gleiche tun würden, also werden sie sich in jeder Runde eine zufällige Anzahl von Schritten bewegen. Die Schildkröte gewinnt, die in 100 Runden am weitesten kommt.

+ Wenn du Befehle wie `forward (20)` verwendest, bewegst du eine einzelne Schildkröte. Du kannst aber weitere Schildkröten erstellen. Füge den folgenden Code am Ende deines Skripts hinzu (stelle sicher, dass der Anfang nicht eingerückt ist):
    
    ![Screenshot](images/race-red.png)
    
    In der ersten Zeile wird eine Schildkröte namens "ada" erstellt. Die nächste Zeile legt die Farbe und Form der Schildkröte fest. Jetzt sieht sie wirklich aus wie eine Schildkröte!

+ Lass uns die Schildkröte an die Startlinie schicken:
    
    ![Screenshot](images/race-start.png)

+ Jetzt kannst du die Schildkröte zum Rennen bringen, indem du sie eine zufällige Anzahl von Schritten bewegst. Du wirst die die `randint` (Zufallszahl) Funktion aus der Python `random` (Zufall) Bibliothek benötigen. Füge diese `import` Zeile an den Anfang des Skripts hinzu:
    
    ![Screenshot](images/race-randint.png)

+ Die `randint` Funktion produziert eine zufällige Ganzzahl zwischen den gewählten Werten. Die Schildkröte bewegt sich in jeder Runde 1, 2, 3, 4 oder 5 Schritte vorwärts.
    
    ![Screenshot](images/race-random.png)

+ Eine Schildkröte allein bedeutet kein großes Rennen! Fügen wir noch eine hinzu:
    
    ![Screenshot](images/race-blue.png)
    
    Beachte, dass der Code zum Bewegen der blauen Schildkröte in **der gleichen** `for` Schleife stehen muss, wie der Code, der die rote Schildkröte bewegt, damit beide Schildkröten jede Runde sich bewegen.