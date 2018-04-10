## Corrida de tartarugas

Agora para o pouco de diversão. Vamos adicionar algumas tartarugas de corrida. Seria muito chato se as tartarugas fizessem a mesma coisa todas as vezes, então elas moveriam um número aleatório de passos a cada turno. O vencedor é a tartaruga que fica mais distante em 100 voltas.

+ Quando você usa comandos como `para a frente (20)` você está usando uma única tartaruga. Mas você pode criar mais tartarugas. Adicione o seguinte código ao final do seu script (mas certifique-se de que não esteja recuado):
    
    ![captura de tela](images/race-red.png)
    
    A primeira linha cria uma tartaruga chamada 'ada'. As próximas linhas definem a cor e a forma da tartaruga. Agora parece mesmo uma tartaruga!

+ Vamos mandar a tartaruga para a linha de partida:
    
    ![captura de tela](images/race-start.png)

+ Agora você precisa fazer a corrida de tartaruga movendo um número aleatório de etapas de cada vez. Você precisará da função `randint` da biblioteca</code> aleatória do Python `. Adicione esta linha <code>import` ao topo do seu script:
    
    ![captura de tela](images/race-randint.png)

+ A função `randint` retorna um inteiro aleatório (número inteiro) entre os valores escolhidos. A tartaruga irá avançar 1, 2, 3, 4 ou 5 passos em cada turno.
    
    ![captura de tela](images/race-random.png)

+ Uma tartaruga não é muito corrida! Vamos adicionar outro:
    
    ![captura de tela](images/race-blue.png)
    
    Note que o código para mover a tartaruga azul precisa estar em **o mesmo** `para` loop como o código para mover a tartaruga vermelha para que cada um faça um movimento a cada turno.