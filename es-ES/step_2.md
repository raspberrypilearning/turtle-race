## Pista de carreras

Vas a crear un juego con tortugas de carreras. Primero necesitarán una pista de carreras.

+ Abre la plantilla Python en blanco de Trinket: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>. Si estás leyendo esto por Internet, también puedes usar la versión integrada de esta trinket que aparece debajo.

<div class="trinket">
<iframe src="https://trinket.io/embed/python/33e5c3b81b?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
</div>

+ Añade el siguiente código para dibujar una línea utilizando la 'turtle':

  ![screenshot](images/race-forward.png)

+ Ahora utilicemos la tortuga para dibujar unas marcas de la pista para la carrera.

  La función `write` de la tortuga escribe texto en la pantalla.

  Inténtalo:

  ![screenshot](images/race-markings1.png)

+ Ahora tienes que rellenar los números en el medio para crear marcas:

  ![screenshot](images/race-markings2.png)

+ ¿Te diste cuenta de que tu código se repite mucho? Lo único que cambia es el número que hay que escribir.

  Hay una forma mejor de hacer esto en Python. Puedes usar un bucle `for`.

  Actualiza tu código para utilizar un bucle `for`:

  ![screenshot](images/race-for.png)

+ Mmm, esto solo escribe números hasta 4. En Python `range(5)` nos da cinco números, del 0 al 4. Para hacer que nos dé 5, tendrás que utilizar `range(6)`:

  ![screenshot](images/race-range.png)

+ Ahora podemos dibujar algunas marcas de la pista. La tortuga empieza en las coordinadas (0,0) en el medio de la pantalla.

  Mueve la tortuga hasta la parte superior izquierda en su lugar:

  ![screenshot](images/race-goto.png)

+ ¡Ah, tendrás que levantar el lápiz primero!

  ![screenshot](images/race-penup.png)

+ En lugar de dibujar una línea horizontalmente, dibujemos líneas verticales para crear una pista:

  ![screenshot](images/race-lines.png)

+ Parece más ordenado si centras los números:

  ![screenshot](images/race-center.png)

+ Y puedes acelerar la tortuga para que dibuje más rápido:

  ![screenshot](images/race-speed.png)
