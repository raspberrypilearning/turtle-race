## Pista de corrida

Você vai criar um jogo de corrida de tartarugas. Primeiro elas precisam de uma pista de corrida.

+ Abra um modelo Python em branco no Trinket: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Adicione o seguinte código para desenhar uma linha usando o módulo 'turtle':
    
    ![screenshot](images/race-forward.png)

+ Agora vamos usar turte para desenhar algumas marcas para a corrida.
    
    A função turtle `write` escreve texto na tela.
    
    Tente:
    
    ![screenshot](images/race-markings1.png)

+ Agora você precisa preencher os números intermediários para criar marcações:
    
    ![screenshot](images/race-markings2.png)

+ Você notou que seu código é muito repetitivo? A única coisa que muda é o número a ser escrito.
    
    Existe uma maneira melhor de fazer isso em Python. Você pode usar um laço`for`.
    
    Atualize seu código para usar um laço `for`:
    
    ![screenshot](images/race-for.png)

+ Hmm, isso só imprime números até 4. No Python `range(5)` retorna cinco números, de 0 a 4. Para que ele também retorne 5, você precisará usar `range(6)`:
    
    ![screenshot](images/race-range.png)

+ Agora podemos desenhar algumas marcas de pista. A tartaruga começa nas coordenadas (0,0) no meio da tela.
    
    Em vez disso, mova a tartaruga para o canto superior esquerdo:
    
    ![screenshot](images/race-goto.png)

+ Ah, você vai querer levantar a caneta primeiro!
    
    ![screenshot](images/race-penup.png)

+ Em vez de desenhar uma linha horizontalmente, vamos desenhar linhas verticais para criar uma trilha:
    
    ![screenshot](images/race-lines.png)
    
    `right(90)` faz a tartaruga girar 90 graus para a direita (um ângulo reto). Movendo `forward(10)` antes de pousar a caneta, deixa um pequeno espaço entre o número e o início da linha. Após desenhar a linha, você levanta a caneta e volta `backward(160)` o comprimento da linha mais o espaço.

+ Fica mais organizado se você centralizar os números:
    
    ![screenshot](images/race-center.png)

+ E você pode acelerar a tartaruga para que ela desenhe mais rápido:
    
    ![screenshot](images/race-speed.png)