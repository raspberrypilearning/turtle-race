## Trkalište

Napravićeš igru u kojoj se trkaju kornjače. Za to će im prvo trebati trkalište.

+ Otvori prazan Python šablon u Trinketu: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Dodaj sljedeći kôd za crtanje linije koristeći 'kornjaču' (turtle):
    
    ![screenshot](images/race-forward.png)

+ Sada, koristeći kornjaču, nacrtajmo oznake trkališta.
    
    Funkcija `write` ispisuje tekst na ekranu.
    
    Isprobaj:
    
    ![screenshot](images/race-markings1.png)

+ Sada treba da upišeš brojeve kako bi napravio/napravila oznake:
    
    ![screenshot](images/race-markings2.png)

+ Primjećuješ li da se tvoj kôd u velikoj mjeri ponavlja? Mijenjaju se jedino brojevi koje treba upisati.
    
    U Pythonu postoji bolji način da to napraviš. Možeš da koristiš `for` petlju.
    
    Izmijeni svoj kôd koristeći `for` petlju:
    
    ![screenshot](images/race-for.png)

+ Hm, ovo ispisuje samo brojeve do 4. U Pythonu, `range(5)` daje pet brojeva, od 0 do 4. Ako želiš da ispiše i broj 5, moraš da koristiš `range(6)`:
    
    ![screenshot](images/race-range.png)

+ Sada možemo da nacrtamo oznake trkališta. Kornjača počinje od koordinata (0,0) koje se nalaze na sredini ekrana.
    
    Pomjeri kornjaču u gornji lijevi ugao:
    
    ![screenshot](images/race-goto.png)

+ Ah, prvo moraš da podigneš olovku!
    
    ![screenshot](images/race-penup.png)

+ Umjesto da crtamo liniju horizontalno, nacrtajmo trkalište pomoću vertikalnih linija:
    
    ![screenshot](images/race-lines.png)
    
    Naredbom `right(90)` kornjača će okreće udesno za 90 stepeni (pravi ugao). Pomjeranjem naprijed pomoću naredbe `forward(10)` prije spuštanja olovke ostaje mala praznina između broja i početka linije. Nakon što nacrtaš liniju, podigni olovku i koristi `backward(160)` da ideš unazad za dužinu linije i praznine.

+ Izgledaće urednije ako centriraš brojeve:
    
    ![screenshot](images/race-center.png)

+ Takođe, možeš da ubrzaš kornjaču kako bi brže crtala:
    
    ![screenshot](images/race-speed.png)