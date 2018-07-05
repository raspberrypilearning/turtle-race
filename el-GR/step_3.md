## Πίστα αγώνα

Πρόκειται να δημιουργήσεις ένα παιχνίδι με αγωνιστικές χελώνες. Πρώτα θα χρειαστείς μια αγωνιστική πίστα.

+ Άνοιξε το κενό πρότυπο Python Trinket: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Πρόσθεσε τον ακόλουθο κώδικα για να σχεδιάσεις μια γραμμή χρησιμοποιώντας τη 'χελώνα':
    
    ![screenshot](images/race-forward.png)

+ Τώρα ας χρησιμοποιήσουμε τη χελώνα για να σχεδιάσεις μερικές σημάνσεις στην πίστα για τον αγώνα.
    
    Η λειτουργία `write` της χελώνας γράφει κείμενο στην οθόνη.
    
    Δοκίμασέ το:
    
    ![screenshot](images/race-markings1.png)

+ Τώρα πρέπει να συμπληρώσεις τους αριθμούς για να δημιουργήσεις σημάνσεις:
    
    ![screenshot](images/race-markings2.png)

+ Παρατήρησες ότι ο κώδικας είναι επαναλαμβανόμενος; Το μόνο που αλλάζει είναι ο αριθμός που γράφεις.
    
    Υπάρχει καλύτερος τρόπος να το κάνεις αυτό στην Python. Μπορείς να χρησιμοποιήσεις ένα βρόχο `for`.
    
    Ενημέρωσε τον κώδικα για να χρησιμοποιεί ένα βρόχο `for`:
    
    ![screenshot](images/race-for.png)

+ Χμμ, αυτό εκτυπώνει μόνο αριθμούς μέχρι 4. Στην Python η `range(5)` επιστρέφει πέντε αριθμούς, από 0 έως 4. Για να το κάνεις να επιστρέφει και το 5, θα χρειαστεί να χρησιμοποιήσεις την `range(6)`:
    
    ![screenshot](images/race-range.png)

+ Now we can draw some track markings. The turtle starts at coordinates (0,0) in the middle of the screen.
    
    Move the turtle to the top left instead:
    
    ![screenshot](images/race-goto.png)

+ Ah, you'll want to lift the pen up first!
    
    ![screenshot](images/race-penup.png)

+ Instead of drawing a line horizontally, let's draw vertical lines to create a track:
    
    ![screenshot](images/race-lines.png)
    
    `right(90)` makes the turtle turn right 90 degrees (a right angle.) Moving `forward(10)` before putting the pen down leaves a small gap between the number and the start of the line. After drawing the line you lift up the pen and go `backward(160)` the length of the line plus the gap.

+ It looks neater if you centre the numbers:
    
    ![screenshot](images/race-center.png)

+ And you can speed up the turtle so it draws faster:
    
    ![screenshot](images/race-speed.png)