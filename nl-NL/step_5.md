## Racing turtles

Now for the fun bit. Let's add some racing turtles. It would be really boring if the turtles did the same thing every time so they will move a random number of steps each turn. The winner is the turtle that gets the furthest in 100 turns.

+ Wanneer je commando's zoals `forward(20)` gebruikt, gebruik je een enkele schildpad. Maar je kunt meer schildpadden maken. Voeg de volgende code toe aan het einde van je script (maar zorg ervoor dat de code niet ingespringt):
    
    ![screenshot](images/race-red.png)
    
    De eerste regel creëert een schildpad genaamd 'ada'. De volgende regels bepalen de kleur en vorm van de schildpad. Nu lijkt het echt op een schildpad!

+ Laten we de schildpad naar de startlijn sturen:
    
    ![screenshot](images/race-start.png)

+ Nu moet je de schildpad laten racen door een willekeurig aantal stappen tegelijk te verplaatsen. Je hebt de ` randint ` functie van de Python ` random ` bibliotheek nodig. Voeg deze `import` regel aan de bovenkant van je script toe:
    
    ![screenshot](images/race-randint.png)

+ De `randint` functie retourneert een tussen de gekozen waarden, willekeurig integer (geheel) getal. De schildpad beweegt bij elke beurt 1, 2, 3, 4 of 5 stappen vooruit.
    
    ![screenshot](images/race-random.png)

+ Met een schildpad is het niet echt een race! Laten we er nog een toevoegen:
    
    ![screenshot](images/race-blue.png)
    
    Merk op dat de code voor het verplaatsen van de blauwe schildpad in **dezelfde** `for` lus moet zijn als de code voor het verplaatsen van de rode schildpad zodat ze elke beurt een zet doen.