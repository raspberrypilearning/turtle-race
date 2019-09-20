## Rennstrecke

Du wirst ein Spiel erstellen, indem Schildkröten um die Wette rennen. Zuerst brauchen sie eine Rennstrecke.

+ Öffne das leere Python-Vorlage-Trinket: <a href="https://trinket.io/python/f69e360eb8" target="_blank">https://trinket.io/python/f69e360eb8</a>.

+ Füge folgenden Code hinzu, um eine Zeile mit der 'Schildkröte' (turtle) zu zeichnen:
    
    ![Screenshot](images/race-forward.png)

+ Lass uns jetzt turtle verwenden, um ein paar Bahnmarkierungen für das Rennen zu zeichnen.
    
    Die `write` Funktion schreibt Text auf den Bildschirm.
    
    Versuche es:
    
    ![Screenshot](images/race-markings1.png)

+ Jetzt musst du die dazwischen liegenden Zahlen eingeben, um weitere Bahnmarkierungen zu erstellen:
    
    ![Screenshot](images/race-markings2.png)

+ Hast du bemerkt, dass dein Code sich wiederholt? Das einzige, was sich verändert, ist die Zahl.
    
    Es gibt eine bessere Möglichkeit, dies in Python zu tun. Du kannst eine `for` loop (Zählschleife) verwenden.
    
    Aktualisiere deinen Code, um eine `for` loop (Zählschleifen) zu verwenden:
    
    ![Screenshot](images/race-for.png)

+ Hmm, das zeigt nur Zahlen bis 4 an. In Python zeigt `range(5)` fünf Zahlen an (von 0 bis 4). Damit dir Python auch die Nummer 5 anzeigt, musst du den Bereich `range(6)` verwenden.
    
    ![Screenshot](images/race-range.png)

+ Jetzt können wir Bahnmarkierungen zeichnen. Die Schildkröte beginnt bei den Koordinaten (0,0) in der Mitte des Bildschirms.
    
    Bewege stattdessen die Schildkröte nach oben links:
    
    ![Screenshot](images/race-goto.png)

+ Ah, du wirst zuerst den Stift heben wollen (schreibe hierfür "penup()")!
    
    ![Screenshot](images/race-penup.png)

+ Anstatt eine Linie horizontal zu zeichnen, zeichnen wir vertikale Linien, um Distanz Markierungen zu erstellen:
    
    ![Screenshot](images/race-lines.png)
    
    Mit `right(90)` lässt sich die Schildkröte um 90 Grad nach rechts drehen (in einem rechten Winkel). Wenn du `forward(10)` schreibst, bevor du den Stift ablegst (schreibe hierfür "pendown()", bleibt eine kleine Lücke zwischen der Nummer und dem Zeilenanfang. Nach dem Zeichnen der Linie kannst du den Stift wieder hochheben ("penup()"). Schreibe danach `backward(160)`, um zurück an den Anfang zu gelangen.

+ Es sieht besser aus, wenn du die Zahlen zentrierst. 
    
    ![Screenshot](images/race-center.png)

+ Und du kannst die Schildkröte beschleunigen, damit es schneller zeichnet:
    
    ![Screenshot](images/race-speed.png)