## Loppspår

Du ska skapa ett spel med racing sköldpaddor. Först behöver de ett racerbanor.

+ Öppna den tomma Python-mallen. Trinket: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Lägg till följande kod för att rita en rad med "sköldpaddan":
    
    ![skärmdump](images/race-forward.png)

+ Låt oss nu använda sköldpaddan för att rita några spårmarkeringar för loppet.
    
    Sköldpaddan `skriv` funktionen skriver text till skärmen.
    
    Försök:
    
    ![skärmdump](images/race-markings1.png)

+ Nu måste du fylla i siffrorna mellan att skapa markeringar:
    
    ![skärmdump](images/race-markings2.png)

+ Visste du att din kod är mycket repetitiv? Det enda som ändras är numret att skriva.
    
    Det finns ett bättre sätt att göra detta i Python. Du kan använda en `för` slinga.
    
    Uppdatera din kod för att använda en `för` slinga:
    
    ![skärmdump](images/race-for.png)

+ Hmm, att endast skriver tal upp till 4. I Python `rad (5)` returnerar fem siffror, från 0 till 4. För att få det att också återvända 5 måste du använda `intervall (6)`:
    
    ![skärmdump](images/race-range.png)

+ Nu kan vi rita några spårmarkeringar. Sköldpaddan börjar vid koordinaterna (0,0) mitt på skärmen.
    
    Flytta sköldpaddan till vänster till vänster istället:
    
    ![skärmdump](images/race-goto.png)

+ Åh, du vill lyfta pennan först!
    
    ![skärmdump](images/race-penup.png)

+ Istället för att dra en linje horisontellt, låt vi rita vertikala linjer för att skapa ett spår:
    
    ![skärmdump](images/race-lines.png)
    
    `höger (90)` gör sköldpaddan till höger 90 grader (en rätt vinkel.) Flytta `framåt (10)` innan du lägger pennan ner lämnar ett litet mellanrum mellan linjen och början. Efter att du har ritat linjen lyfter du upp pennan och går `bakåt (160)` längden på linjen plus gapet.

+ Det ser snygg ut om du centrerar siffrorna:
    
    ![skärmdump](images/race-center.png)

+ Och du kan påskynda sköldpaddan så att den drar snabbare:
    
    ![skärmdump](images/race-speed.png)