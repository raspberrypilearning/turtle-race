## Závodní dráha

Chystáš se vytvořit hru se závodními želvami. Nejprve budou potřebovat závodní dráhu.

+ Otevři prázdnou šablonu pro Python na Trinketu: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Přidej následující kód pro nakreslení čáry s využitím knihovny „turtle“:
    
    ![screenshot](images/race-forward.png)

+ Nyní použijeme želvu pro nakreslení pár značek na závodní dráhu.
    
    Funkce `write`, kterou želva obsahuje, vypíše na obrazovku text.
    
    Vyzkoušej si to:
    
    ![screenshot](images/race-markings1.png)

+ Nyní musíš mezi to vyplnit čísla pro vytvoření značek:
    
    ![screenshot](images/race-markings2.png)

+ Povšimni si, že se tvůj kód velmi často opakuje. Mění se pouze číslo.
    
    V jazyce Python existuje lepší způsob, jak to udělat. Můžeš použít cyklus `for`.
    
    Aktualizuj svůj kód tak, aby používal cyklus `for`:
    
    ![screenshot](images/race-for.png)

+ Hmm, to pouze vypisuje čísla do 4. V Pythonu `range(5)` vrátí pět čísel, od 0 do 4. Aby ti to vrátilo i 5, budeš muset použít `range(6)`:
    
    ![screenshot](images/race-range.png)

+ Nyní můžeme nakreslit pár značek na dráhu. Želva začíná na souřadnicích (0,0) uprostřed obrazovky.
    
    Místo toho přesuň želvu doleva nahoru:
    
    ![screenshot](images/race-goto.png)

+ Ach, nejprve budeš muset zvednout pero!
    
    ![screenshot](images/race-penup.png)

+ Než abychom nakreslili vodorovnou čáru, pojďme nakreslit svislé čáry pro vytvoření dráhy:
    
    ![screenshot](images/race-lines.png)
    
    `right(90)` způsobí to, že se želva otočí o 90 stupňů doprava (pravý úhel). Pohyb `forward(10)` před položením pera zapříčiní to, že před číslem a začátkem čáry vynechá malou mezeru. Po nakreslení čáry zvedni pero a přejdi `backward(160)` po délce čáry včetně mezery.

+ Pokud vycentruješ čísla, vypadá to ještě lépe:
    
    ![screenshot](images/race-center.png)

+ Taky můžeš zrychlit želvu, aby kreslila rychleji:
    
    ![screenshot](images/race-speed.png)