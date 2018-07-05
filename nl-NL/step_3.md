## Racebaan

Je gaat een spel maken met raceschildpadden. Eerst hebben ze een racebaan nodig.

+ Open de lege Python-sjabloon Trinket: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Voeg de volgende code toe om een ​​lijn te tekenen met de 'turtle" (schildpad):
    
    ![screenshot](images/race-forward.png)

+ Laten we nu de schildpad gebruiken om de baanmarkeringen voor de race te tekenen.
    
    De turtle `write` functie schrijft tekst naar het scherm.
    
    Probeer het uit:
    
    ![screenshot](images/race-markings1.png)

+ Nu moet je getallen ertussen invoegen om markeringen te maken:
    
    ![screenshot](images/race-markings2.png)

+ Is het je opgevallen dat de code steeds weer herhaald wordt? Het enige dat verandert, is het getal achter write.
    
    Er is een betere manier om dit in Python te doen. Je kunt een `for` -lus gebruiken.
    
    Werk je code bij door een​​ `for` lus te gebruiken:
    
    ![screenshot](images/race-for.png)

+ Hmm, dat drukt alleen getallen tot 4 af. `range(5)` geeft In Python vijf getallen, van 0 tot en met 4. Om ook 5 te krijgen, moet je `range(6)` gebruiken:
    
    ![screenshot](images/race-range.png)

+ Nu kunnen we wat baanmarkeringen tekenen. De turtle begint op coördinaten (0,0) in het midden van het scherm.
    
    Beweeg de turtle naar linksboven:
    
    ![screenshot](images/race-goto.png)

+ Ah, je moet eerst de pen optillen!
    
    ![screenshot](images/race-penup.png)

+ In plaats van een lijn horizontaal te tekenen, tekenen we verticale lijnen om een baan te maken:
    
    ![screenshot](images/race-lines.png)
    
    `right(90)` zorgt ervoor dat de turtle een hoek van 90 graden rechtsom (een rechte hoek) maakt. Een `forward(10)` beweging laat een kleine opening tussen het nummer en het begin van de lijn ontstaan voordat de pen naar beneden wordt gedaan,. Nadat je de lijn hebt getekend, til je de pen op en ga je `backward(160)` (achteruit) over de lengte van de lijn plus de tussenruimte.

+ Het ziet er netter uit als je de cijfers centreert:
    
    ![screenshot](images/race-center.png)

+ En je kunt de turtle versnellen zodat hij sneller tekent:
    
    ![screenshot](images/race-speed.png)