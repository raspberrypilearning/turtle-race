## Race track

Aiot luoda pelin kilpikonnat. Ensin he tarvitsevat kilparadan.

+ Avaa tyhjä Python-mallipohja Trinket: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Piirtämään viiva "turtle" käyttämällä seuraavaa koodia:
    
    ![kuvakaappaus](images/race-forward.png)

+ Käytämme nyt kilpikonnaa piirtääksesi radan jäljet.
    
    Kilpikonna `kirjoittaa` -toiminto kirjoittaa tekstiä ruudulle.
    
    Kokeile:
    
    ![kuvakaappaus](images/race-markings1.png)

+ Nyt sinun on täytettävä numerot, jotta voit luoda merkkejä:
    
    ![kuvakaappaus](images/race-markings2.png)

+ Huomasitko, että koodisi on hyvin toistuva? Ainoa muutos on numero kirjoitettavaksi.
    
    Parempi tapa on tehdä tämä pythonilla. Voit käyttää `: a` silmukkaa.
    
    Päivitä koodisi `: n` silmukan käyttämiseen:
    
    ![kuvakaappaus](images/race-for.png)

+ Hmm, joka tulostaa numeroita vain 4: een. Python `-alueella (5)` palauttaa viisi numeroa 0: stä 4: een. Jotta se palaa myös 5, sinun tarvitsee käyttää `alue (6)`:
    
    ![kuvakaappaus](images/race-range.png)

+ Nyt voimme tehdä joitain jäljen merkintöjä. Kilpikonna alkaa koordinaattien (0,0) näytön keskellä.
    
    Siirrä kilpikonna vasempaan yläkulmaan sen sijaan:
    
    ![kuvakaappaus](images/race-goto.png)

+ Haluat nostaa kynän ensin!
    
    ![kuvakaappaus](images/race-penup.png)

+ Piirtämällä linjaa vaakasuunnassa vetämällä pystysuoria viivoja raidan luomiseksi:
    
    ![kuvakaappaus](images/race-lines.png)
    
    `oikealle (90)` tekee kilpikonnaa oikealle 90 astetta (oikealle kulmalle). Siirrä `eteenpäin (10)` ennen kynän asettamista alas jättää pienen raon numeron ja rivin alun välillä. Piirtämisen jälkeen nostat kynän ja menkät `taaksepäin (160)` rivin pituuden ja raon.

+ Se näyttää paremmalta, jos keskit numerot:
    
    ![kuvakaappaus](images/race-center.png)

+ Ja voit nopeuttaa kilpikonnaa niin, että se vetää nopeammin:
    
    ![kuvakaappaus](images/race-speed.png)