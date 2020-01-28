## Race track

You're going to create a game with racing turtles. First they'll need a race track.

+ פתחו את תבנית ה-Trinket הריקה של קובץ Python: <a href="http://jumpto.cc/python-new" target="_blank"> jumpto.cc/python-new </a>.

+ Add the following code to draw a line using the 'turtle':
    
    ![צילום מסך](images/race-forward.png)

+ Now let's use the turtle to draw some track markings for the race.
    
    The turtle `write` function writes text to the screen.
    
    Try it:
    
    ![צילום מסך](images/race-markings1.png)

+ Now you need to fill in the numbers in between to create markings:
    
    ![צילום מסך](images/race-markings2.png)

+ Did you notice that your code is very repetitive? The only thing that changes is the number to write.
    
    There's a better way of doing this in Python. You can use a `for` loop.
    
    Update your code to use a `for` loop:
    
    ![צילום מסך](images/race-for.png)

+ Hmm, that only prints numbers up to 4. In Python `range(5)` returns five numbers, from 0 up to 4. To get it to also return 5 you'll need to use `range(6)`:
    
    ![צילום מסך](images/race-range.png)

+ Now we can draw some track markings. The turtle starts at coordinates (0,0) in the middle of the screen.
    
    Move the turtle to the top left instead:
    
    ![צילום מסך](images/race-goto.png)

+ Ah, you'll want to lift the pen up first!
    
    ![צילום מסך](images/race-penup.png)

+ Instead of drawing a line horizontally, let's draw vertical lines to create a track:
    
    ![צילום מסך](images/race-lines.png)
    
    `right(90)` makes the turtle turn right 90 degrees (a right angle.) Moving `forward(10)` before putting the pen down leaves a small gap between the number and the start of the line. After drawing the line you lift up the pen and go `backward(160)` the length of the line plus the gap.

+ It looks neater if you centre the numbers:
    
    ![צילום מסך](images/race-center.png)

+ And you can speed up the turtle so it draws faster:
    
    ![צילום מסך](images/race-speed.png)