## Racing sköldpaddor

Nu för den roliga biten. Låt oss lägga till några turtles. Det skulle vara väldigt tråkigt om sköldpaddorna gjorde samma sak varje gång så de kommer att flytta ett slumpmässigt antal steg varje tur. Vinnaren är sköldpaddan som blir längst i 100 varv.

+ När du använder kommandon som `framåt (20)` använder du en enda sköldpadda. Men du kan skapa fler sköldpaddor. Lägg till följande kod till slutet av ditt skript (men se till att det inte är indryckt):
    
    ![skärmdump](images/race-red.png)
    
    Den första raden skapar en sköldpadda som heter 'ada'. Nästa rader ställer in sköldpaddans färg och form. Nu ser det verkligen ut som en sköldpadda!

+ Låt oss skicka sköldpaddan till startlinjen:
    
    ![skärmdump](images/race-start.png)

+ Nu behöver du göra sköldpaddsloppet genom att flytta ett slumpmässigt antal steg i taget. Du behöver `randint` funktionen från Python `slumpmässigt` biblioteket. Lägg till den här `importen` raden till toppen av ditt skript:
    
    ![skärmdump](images/race-randint.png)

+ `randint` funktionen returnerar ett slumpmässigt heltal (heltal) mellan de valda värdena. Sköldpaddan flyttar framåt 1, 2, 3, 4 eller 5 steg vid varje tur.
    
    ![skärmdump](images/race-random.png)

+ En sköldpadda är inte mycket av en tävling! Låt oss lägga till en annan:
    
    ![skärmdump](images/race-blue.png)
    
    Observera att koden för att flytta den blå sköldpaddan måste vara i **samma** `för` slinga som koden för att flytta den röda sköldpaddan så att de vart och ett gör ett drag varje gång.