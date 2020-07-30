## Carreras de tortugas

Ahora vamos a la parte divertida. Añadamos algunas tortugas de carreras. Sería realmente aburrido si las tortugas hicieran siempre lo mismo, así que se moverán un número aleatorio de pasos en cada turno. Quien gana es la tortuga que llega más lejos en 100 turnos.

+ Cuando usas comandos como `forward(20)` estás usando una sola tortuga, pero puedes crear más tortugas. Añade el siguiente código al final de tu script (pero asegúrate de que no tenga sangría):
    
    ![captura de pantalla](images/race-red.png)
    
    La primera línea crea una tortuga llamada «ana». Las siguientes líneas establecen el color y la forma de la tortuga. ¡Ahora realmente parece una tortuga!

+ Vamos a enviar la tortuga a la línea de partida:
    
    ![captura de pantalla](images/race-start.png)

+ Ahora necesitas hacer que la tortuga se mueva un número aleatorio de pasos a la vez. Necesitarás la función `randint` de la librería de Python `random`. Añade esta línea `import` en la parte superior de tu script:
    
    ![captura de pantalla](images/race-randint.png)

+ La función `randint` devuelve un número aleatorio (número entero) entre los valores elegidos. La tortuga avanzará 1, 2, 3, 4 o 5 pasos en cada turno.
    
    ![captura de pantalla](images/race-random.png)

+ ¡Una tortuga no es suficiente para una gran carrera! Añadamos otra:
    
    ![captura de pantalla](images/race-blue.png)
    
    Ten en cuenta que el código para mover la tortuga azul debe estar en **el mismo** bucle `for` al igual que el código para mover la tortuga roja para que cada una haga un movimiento en cada turno.