## Kilpikonnat

Nyt hauskasta bitistä. Lisätään joitain kilpa-kilpikonnia. Olisi todella tylsää, jos kilpikonnat tekisivät saman ajan joka kerta, jotta he siirtäisivät satunnaiset askeleet joka käänteessä. Voittaja on kilpikonna, joka saa kauimpana 100 kierrosta.

+ Kun käytät komentoja kuten `eteenpäin (20)` käytät yhtä kilpikonnaa. Mutta voit luoda enemmän kilpikonnia. Lisää seuraava koodi koodin loppuun (mutta varmista, ettei se ole sisennetty):
    
    ![kuvakaappaus](images/race-red.png)
    
    Ensimmäinen rivi luo kilpikonna nimeltä ada. Seuraavat viivat asettavat kilpikonnan värin ja muodon. Nyt se näyttää siltä kuin kilpikonna!

+ Lähetetään kilpikonna lähtölinjalle:
    
    ![kuvakaappaus](images/race-start.png)

+ Nyt sinun täytyy tehdä kilpikonnaa siirtämällä satunnaisia ​​askeleita kerrallaan. Tarvitset `randint` -toiminnon Python `random` -kirjastosta. Lisää tämä `tuonti` rivi komentosarjan yläosaan:
    
    ![kuvakaappaus](images/race-randint.png)

+ `randint` -toiminto palauttaa satunnaisen kokonaislukuarvon (kokonaisluku) valitun arvon välillä. Kilpikonna siirtyy eteenpäin 1, 2, 3, 4 tai 5 askelta jokaisella kierroksella.
    
    ![kuvakaappaus](images/race-random.png)

+ Yksi kilpikonna ei ole paljon rotuun! Lisää toinen:
    
    ![kuvakaappaus](images/race-blue.png)
    
    Huomaa, että sinisen kilpikonnan siirtämisen koodin on oltava **sama** `` silmukan kohdalla kuin punainen kilpikonna siirrettävän koodin niin, että kukin liikkuu joka kierrosta.