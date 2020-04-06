## Závodící želvy

A teď ta zábavná část. Pojďme přidat nějaké závodící želvy. Bylo by opravdu nudné, kdyby želvy dělaly pokaždé tu stejnou věc, tudíž se budou každým tahem pohybovat o náhodný počet kroků. Vítězem bude ta želva, která se dostane za 100 tahů nejdále.

+ Používáš-li příkazy jako `forward(20)`, hýbeš pouze s jednou želvou. Můžeš ale přidat více želv. Přidej následující kód na konec svého skriptu (ale ujisti se, že jej neodsadíš):
    
    ![screenshot](images/race-red.png)
    
    První řádek vytváří želvu se jménem „ada“. Další řádky nastavují barvu a tvar želvy. Teď to vypadá jako opravdická želva!

+ Pojďme poslat želvu na startovní čáru:
    
    ![screenshot](images/race-start.png)

+ Nyní budeš muset želvu přinutit závodit tím, že se bude pohybovat a náhodný počet kroků najednou. Budeš potřebovat funkci `randint` z knihovny `random` od jazyka Python. Na začátek svého skriptu přidej tento `import` řádek:
    
    ![screenshot](images/race-randint.png)

+ Funkce `randint` navrací náhodné celé číslo mezi zvolenými hodnotami. Želva se každým tahem pohne dopředu o 1, 2, 3, 4, nebo 5 kroků.
    
    ![screenshot](images/race-random.png)

+ S jednou želvou závodit nelze! Pojďme přidat další:
    
    ![screenshot](images/race-blue.png)
    
    Měj na paměti, že kód pro rozpohybování modré želvy musí mít **ten stejný** cyklus `for`, jako je v kódu pro rozpohybování červené želvy tak, že obě udělají v každém tahu krok.