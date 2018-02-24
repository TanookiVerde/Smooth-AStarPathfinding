# Métodos para suavização da movimentação de um personagem com A* Pathfinding
## Introdução
Atualmente os jogos digitais têm explorado mais e mais a área de inteligência artificial, seja para improvisar em diálogos com o jogador, seja para derrotá-lo em alguma partida. O uso de técnicas de IA melhoram a imersão do usuário e o fazem acreditar que ele de fato está jogando com um outro ser humano. Entretanto não necessariamente essa é a parte mais importante para a construção de personagens realistas.

Mesmo que um personagem saiba que deve ir para o ponto A no mapa, como ele andará? Teleporte? Irá em linha reta ultrapassando obstáculos? Para iludir o jogador nenhuma das possibilidades deve ser verdadeira. Sabemos que um humano contornaria os obstáculos e que ele tentaria seguir pelo caminho mais rápido. Por conta disso torna-se necessária a existência de algoritmos específicos que ajude o computador a reproduzir esse movimento.

A mais comum é interpretar o mapa como um grafo ponderado e usar um algoritmo para descobrir o caminho mínimo, porém o resultado é uma trajetória com curvas retas ou, muitas vezes, fechadas. Se o jogo têm o mínimo compromisso com movimentação realista, rapidamente o jogador estranharia o movimento robótico do personagem e a imersão seria quebrada. Pensando nisso deverá existir um tratamento do caminho dado pelo algoritmo De alguma maneira será preciso tornar a trajetória curvilínea e suave. 

Portanto, com o objetivo de entender e resolver o problema da movimentação, irei comparar maneiras diferentes de reproduzir uma movimentação realista. Para isso será abordado no estudo os seguintes tópicos:
* Um algoritmo eficiente para achar o menor caminho de A a B em um mapa.
* Algumas maneiras de suavizar a trajetória que originalmente é a saída do algoritmo acima.

## Metodologia

O problema foi dividido em duas partes: achar o menor caminho entre dois pontos e suavizar a trajetória através de interpolação. Eles foram abordados isoladamente sendo sua única relação a saída P do algoritmo (conjunto dos pontos que formam o caminho).

### Pathfinding

**Objetivos**

O objetivo desta parte foi encontrar o menor caminho entre A e B. A forma mais comum e direta de encontrá-lo é interpretar o cenário como um grafo em que cada nó representa uma parte relevante do cenário (uma sala, um portal, etc).

Olhar o cenário desta maneira deixa o raciocínio por trás da criação de um caminho para guiar um personagem muito mais intuitivo, pois o passo a passo de um caminho qualquer seria andar pelas arestas de nó em nó, até chegar no alvo - um nó chamado de target. Entretanto, algo importante para resolução do problema é que não basta que o algoritmo faça o NPC andar pelo grafo, é necessário que condiga com seus  objetivos - que em geral é chegar no ponto B rápido. 

Fica claro, já que um dos objetivos era reproduzir um movimento realista, que é preciso um algoritmo de pathfinding (um algoritmo que nos dê o menor caminho entre dois vértices).

**Representação do grafo**

Para deixar mais fácil a interação do usuário com o programa foi utilizada uma representação em tabela na qual cada célula da matriz é um nó e cada nó tem arestas para ligar com seus vizinhos (o que inclui as diagonais).

Não foi utilizado peso diferente para as diagonais, elas permanecem como se tivessem distância igual a qualquer outra direção.

**Algoritmo A***

O algoritmo escolhido para encontrar o menor caminho foi o A*. Este algoritmo anexa a cada nó uma propriedade que permite prever a melhor direção para andar no grafo. Este valor não só é relacionado ao custo de chegar até o nó, mas também à distância que ainda falta para chegar no nó target.

Este valor, que chamamos de custo, é definido como:
* Para o nó inicial da busca: Custo(start) = 0
* Para um nó n, cujo nó anterior - ou pai - é m: Custo(n) = Custo(m) + H(n)
A função H(n), onde n é o nó atual, é chamada Heurística, ela deve quantifica a distância entre n e target de maneira que quanto maior a distância mais custoso seja. 

Ela foi definida como

**IMG**

onde x e y são as coordenadas de n e target na tabela que representa o cenário.

**IMG**

Com uma visão mais ampla, é possível perceber que o custo de um nó n é definido pelo somatório das funções H(x) em cada nó que antecedeu seu caminho.

A cada iteração o algoritmo irá retirar de uma heap o vértice de menor custo, pegar seus vizinhos, calcular seus respectivos custos e dizer para cada um que seu pai é o nó atual. Estes filhos serão colocados na heap de prioridade (que sempre mantém no topo o nó com o menor custo). Algumas vezes podemos calcular o custo de um nó mais de uma vez vindo de dois caminhos diferentes, isso não é problema, pois o algoritmo sempre mantêm guardado o menor custo. 

Como cada vez que acha um custo menor o algoritmo armazena o vértice anterior que o levou a este caminho, no final é formada uma cadeia na qual o vértice target armazenou o nó m que levou até ele e o nó m armazenou o vértice n que veio antes, e assim sucessivamente. A saída do nosso algoritmo é justamente essa cadeia em forma de vetor [start,...,n,m,target].

O pseudo código abaixo representa melhor a estrutura do algoritmo:

```
função AStar(grafo,start,target):
  Custo do vértice start é 0.
  Vértice atual começa sendo start.

  Enquanto a heap não for vazia.
	  Retirar da heap o nó não visitado com menor custo e colocar ele como atual
	  Se o nó atual for igual a target, terminamos o algoritmo aqui

	  Para todos os vizinhos do nó atual x onde c é seu custo:
		  Calcule c usando custo(x) + h(x)
		  Se c for menor que o custo do vizinho escolhido:
        Custo fica igual a c
			  Diga que este vizinho veio pelo nó atual
```

**Tratando a saída do algoritmo**

Como já dito antes, a saída do algoritmo é um vetor que mostra a trajetória pelo grafo. Para preparar estes dados para a interpolação foi preciso

* Coletar as coordenadas de cada nó na tabela
* Transformar essa coordenadas para o valor real em pixels
  * Em uma tabela 10x10 a saída poderia ser [(0,0),(1,0),...,(9,9)] o que não nos dá os pontos em valores do cenário. Precisamos multiplicar cada coordenada pelo tamanho de cada célula da tabela. Ex.: (1,2)*50 = (50,100) = 50px horizontais e 100px verticais.

### Interpolação

**Objetivos**

O objetivo desta parte é interpolar os pontos definidos na saída do algoritmo de pathfinding, uma sequência de k pontos que mostra a trajetória do personagem pelo cenário. Estes pontos foram chamados de

**IMG**

Esta etapa do projeto passou por algumas modelagens diferentes em relação a técnica que seria utilizada. As três cogitadas foram Piecewise (interpolação por partes), Curvas Bezier e Curvas B-Spline.

**Interpolando usando Piecewise**

A primeira tentativa de modelagem para o problema foi utilizando um polinômio de grau três 

**IMG**

a cada dois pontos. Foi utilizado este grau, pois ele nos possibilita quatro pedidos:

**IMG**

Para cada ponto  foi definido a derivada discreta  é igual a

**IMG**

Usando estes pedidos foi possível calcular um polinômio de grau três que passa por dois pontos de maneira razoavelmente suave, pois apenas pedimos que a primeira derivada fosse relevante no polinômio.

A matriz para cálculo de um dos polinômios ficou:

**IMG**

Mas seria muito mais prático, escrever todas as equações e variáveis em uma matriz só, tal qual normalmente é feito no método piecewise.

O problema de usar este método é que parte das vezes não seria possível calcular um polinômio, pois não existem funções que descrevem tal formato.

**IMG**

Outro ponto negativo é que se o grafo utilizado não fosse de um formato “comportado” com as distâncias entre os nós iguais, nem sempre iriamos encontrar um polinômio com forma adequada para descrever o caminho. A movimentação não estaria sendo realista.

**IMG**

Uma maneira de resolver estes problemas seria rotacionar os eixos para todo polinômio a ser calculado. Porém a complexidade do problema aumenta e deixa este método menos interessante. 

**Interpolando usando Curvas Bézier**

_Definiçao e exemplos_

Curvas Bézier nada mais são que uma função que interpola linearmente pontos em função de um parâmetro t, que é entre 0 e 1. A forma como a curva se comporta é definida usando pontos de controle, que são os pontos intermediários entre o início e o fim da curva. Para t = 0 estamos no ponto inicial, t = 1 estamos no ponto final e t = 0.5 estamos na metade do caminho.

Por conta do uso de t como parâmetro, a curva não é definida em função de um valor ligado ao eixo, portanto não precisa ser feita nenhuma rotação.

Imaginando que temos três pontos, p1,p2,p3 , definimos p1 como inicial, p3 como ponto final e p2 como ponto de controle. Inicialmente o caminho sem interpolação seria ir do ponto p1 ao p2 e do p2 ao p3, ou seja, duas retas. Para um exemplo simples, um ponto da curva Bézier pode ser definido usando estas retas da seguinte maneira:

Se andarmos 25% da reta p1p2, andamos 25% da reta p2p3. Assim obtemos dois pontos, c1, c2, um em cada reta e ambos 25% de distância do ponto de origem. 

Traçando uma reta c1c2 entre esses dois pontos e também traçamos um ponto em 25% dela obtemos um ponto que pertence a curva Bézier de maneira que bezier(0.25) = d1.

**IMG**

Um passo a passo geral para desenhar um ponto seria: trace retas entre os pontos, ande n% em todas as retas formando novos pontos. Ligue estes pontos e repita o processo de andar n% até chegar em apenas um ponto. Ele pertence a curva.

**IMG**

_Função Bézier_

A função que descreve a curva completa com **n-1** pontos é da forma:

**IMG**

onde é um ponto de controle.

Tendo isso em mente, poderia ser aplicado no problema diretamente usando os pontos dados pelo algoritmo de pathfinding com a ressalva que:
* A  curva não encosta nos pontos de controle, portanto não é recomendado que se use todos os pontos para criar uma única curva, mas sim um conjunto de curvas com três pontos cada.
* Dependendo da quantidade de pontos para definir uma curva a função pode começar a ficar cara em termos de complexidade, pois a combinação de n, i a i é calculada usando fatorial.

**IMG**

**Interpolando usando B-Splines**


