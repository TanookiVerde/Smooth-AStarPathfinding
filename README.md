# Métodos para suavização da movimentação de um personagem com A* Pathfinding
## Introdução
Atualmente os jogos digitais têm explorado mais e mais a área de inteligência artificial, seja para improvisar em diálogos com o jogador, seja para derrotá-lo em alguma partida. O uso de técnicas de IA melhoram a imersão do usuário e o fazem acreditar que ele de fato está jogando com um outro ser humano. Entretanto não necessariamente essa é a parte mais importante para a construção de personagens realistas.

Mesmo que um personagem saiba que deve ir para o ponto A no mapa, como ele andará? Teleporte? Irá em linha reta ultrapassando obstáculos? Para iludir o jogador nenhuma das possibilidades deve ser verdadeira. Sabemos que um humano contornaria os obstáculos e que ele tentaria seguir pelo caminho mais rápido. Por conta disso torna-se necessária a existência de algoritmos específicos que ajude o computador a reproduzir esse movimento.

A mais comum é interpretar o mapa como um grafo ponderado e usar um algoritmo para descobrir o caminho mínimo, porém o resultado é uma trajetória com curvas retas ou, muitas vezes, fechadas. Se o jogo têm o mínimo compromisso com movimentação realista, rapidamente o jogador estranharia o movimento robótico do personagem e a imersão seria quebrada. Pensando nisso deverá existir um tratamento do caminho dado pelo algoritmo De alguma maneira será preciso tornar a trajetória curvilínea e suave. 

Portanto, com o objetivo de entender e resolver o problema da movimentação, irei comparar maneiras diferentes de reproduzir uma movimentação realista. Para isso será abordado no estudo os seguintes tópicos:
* Um algoritmo eficiente para achar o menor caminho de A a B em um mapa.
* Algumas maneiras de suavizar a trajetória que originalmente é a saída do algoritmo acima.

