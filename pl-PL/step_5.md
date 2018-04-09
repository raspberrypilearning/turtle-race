## Wyścigi żółwi

A teraz najważniejsza część gry. Dodajmy parę wyścigowych żółwi. Gra będzie naprawdę nudna, jeśli żółwie będą robić to samo za każdym razem, więc będziemy przesuwać je o losową liczbę kroków w każdej turze. Zwycięzcą będzie żółw, który dotrze najdalej po 100 turach.

+ Kiedy używasz poleceń takich jak `forward(20)`, używasz pojedynczego żółwia. Możesz jednak stworzyć więcej żółwi. Dodaj następujący kod na końcu skryptu (ale upewnij się, że nie jest wcięty):
    
    ![screenshot](images/race-red.png)
    
    Pierwsza linia tworzy żółwia o nazwie "ada". Następne wiersze określają kolor i kształt żółwia. Teraz naprawdę wygląda jak żółw!

+ Ustawmy żółwia na linii startowej:
    
    ![screenshot](images/race-start.png)

+ Teraz musisz zrobić wyścig, przesuwając żółwia o losową liczbę kroków. You'll need the `randint` function from the Python `random` library. Add this `import` line to the top of your script:
    
    ![screenshot](images/race-randint.png)

+ The `randint` function returns a random integer (whole number) between the values chosen. The turtle will move forward 1, 2, 3, 4, or 5 steps at each turn.
    
    ![screenshot](images/race-random.png)

+ One turtle isn't much of a race! Let's add another one:
    
    ![screenshot](images/race-blue.png)
    
    Note that the code for moving the blue turtle needs to be in **the same** `for` loop as the code for moving the red turtle so that they each make a move every turn.