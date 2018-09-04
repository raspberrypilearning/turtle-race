## Αγωνιστικές χελώνες

Ας το κάνουμε πιο διασκεδαστικό. Ας προσθέσουμε μερικές αγωνιστικές χελώνες. Θα ήταν πραγματικά βαρετό αν οι χελώνες έκαναν το ίδιο πράγμα κάθε φορά, για αυτό θα κινούνται έναν τυχαίο αριθμό βημάτων. Νικήτρια είναι η χελώνα που φτάνει πιο μακρυά σε 100 στροφές.

+ When you use commands like `forward(20)` you are using a single turtle. But you can create more turtles. Add the following code to the end of your script (but make sure it's not indented):
    
    ![screenshot](images/race-red.png)
    
    The first line creates a turtle called 'ada'. The next lines set the colour and shape of the turtle. Now it really looks like a turtle!

+ Let's send the turtle to the starting line:
    
    ![screenshot](images/race-start.png)

+ Now you need to make the turtle race by moving a random number of steps at a time. You'll need the `randint` function from the Python `random` library. Add this `import` line to the top of your script:
    
    ![screenshot](images/race-randint.png)

+ The `randint` function returns a random integer (whole number) between the values chosen. The turtle will move forward 1, 2, 3, 4, or 5 steps at each turn.
    
    ![screenshot](images/race-random.png)

+ One turtle isn't much of a race! Let's add another one:
    
    ![screenshot](images/race-blue.png)
    
    Note that the code for moving the blue turtle needs to be in **the same** `for` loop as the code for moving the red turtle so that they each make a move every turn.