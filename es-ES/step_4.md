## Tortugas de carreras

Ahora viene la parte divertida. Añadamos algunas tortugas de carreras. Sería muy aburrido si las tortugas hicieran lo mismo todo el tiempo, así que se moverán una serie de pasos al azar en cada turno. La ganadora es la tortuga que llegue más lejos en 100 turnos.

+ Cuando utilizas comandos como `forward(20)`, estás usando la tortuga 1. Pero puedes crear más tortugas. Añade el siguiente código al final de tu secuencia de comandos:

  ![screenshot](images/race-red.png)

  La primera línea crea una tortuga llamada 'red'. Las líneas siguientes establecen el color y la forma de la tortuga. ¡Ahora sí que parece una tortuga!
  
+ Enviemos a la tortuga a la línea de salida:

  ![screenshot](images/race-start.png)
   
+ Ahora tienes que hacer que la tortuga corra moviéndose una serie de pasos al azar cada vez. Necesitarás la función `randint` de la biblioteca Python `random`. Añade esta línea de `import` en la parte superior de tu secuencia de comandos:

  ![screenshot](images/race-randint.png)

+ La función `randint` nos da un número entero entre los valores elegidos. La tortuga se moverá 1, 2, 3, 4, o 5 pasos en cada turno. 

  ![screenshot](images/race-random.png)
  
+ ¡Una tortuga sola no es suficiente para una carrera! Añadamos otra.

  ![screenshot](images/race-blue.png)
  
  Ten en cuenta que el código para mover la tortuga azul tiene que ser el mismo bucle `for` que el código para mover la tortuga roja para que cada una se ponga en movimiento en cada turno.


