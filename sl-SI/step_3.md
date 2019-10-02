## Race track

You're going to create a game with racing turtles. First they'll need a race track.

+ Odpri prazen Python trinket: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Add the following code to draw a line using the 'turtle':
    
    ![posnetek zaslona](images/race-forward.png)

+ Now let's use the turtle to draw some track markings for the race.
    
    The turtle `write` function writes text to the screen.
    
    Try it:
    
    ![posnetek zaslona](images/race-markings1.png)

+ Now you need to fill in the numbers in between to create markings:
    
    ![posnetek zaslona](images/race-markings2.png)

+ Did you notice that your code is very repetitive? The only thing that changes is the number to write.
    
    There's a better way of doing this in Python. You can use a `for` loop.
    
    Update your code to use a `for` loop:
    
    ![posnetek zaslona](images/race-for.png)

+ Hmm, that only prints numbers up to 4. In Python `range(5)` returns five numbers, from 0 up to 4. To get it to also return 5 you'll need to use `range(6)`:
    
    ![posnetek zaslona](images/race-range.png)

+ Now we can draw some track markings. The turtle starts at coordinates (0,0) in the middle of the screen.
    
    Move the turtle to the top left instead:
    
    ![posnetek zaslona](images/race-goto.png)

+ Ah, you'll want to lift the pen up first!
    
    ![posnetek zaslona](images/race-penup.png)

+ Instead of drawing a line horizontally, let's draw vertical lines to create a track:
    
    ![posnetek zaslona](images/race-lines.png)
    
    `right(90)` makes the turtle turn right 90 degrees (a right angle.) Moving `forward(10)` before putting the pen down leaves a small gap between the number and the start of the line. After drawing the line you lift up the pen and go `backward(160)` the length of the line plus the gap.

+ It looks neater if you centre the numbers:
    
    ![posnetek zaslona](images/race-center.png)

+ And you can speed up the turtle so it draws faster:
    
    ![posnetek zaslona](images/race-speed.png)