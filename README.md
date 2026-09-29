Pac-Man em Pygame
Um clone do clássico jogo Pac-Man, desenvolvido em Python com a biblioteca Pygame.
O jogo conta com movimentação baseada em grid, labirinto simétrico, colecionáveis,
inteligência artificial para os fantasmas e condições de vitória e derrota.

Funcionalidades Movimentação em Grid: 
Sistema de movimentação e curva alinhado a células de $40 \times 40$ pixels, 
impedindo que os personagens atravessem paredes.
Animação Dinâmica: 
Animação gráfica da boca do Pac-Man abrindo e fechando de acordo com o tempo de jogo.
Inimigos:
(Fantasmas): Presença dos 4 fantasmas clássicos (Blinky, Pinky, Inky e Clyde) 
com movimentação autônoma que decide direções válidas em cruzamentos

Mecanismos de Jogo:
Vitória: 
Ocorre ao coletar todas as bolinhas da 
tela.Derrota:
Ocorre caso o Pac-Man colida com qualquer um dos fantasmas.
Tela de Fim de Jogo: Exibição de mensagens de vitória ou Game Over antes do encerramento automático da aplicação.

Pré-requisitos 
Para rodar o jogo, é necessário ter o Python 3.x e a biblioteca Pygame instalados.
Instalando o Pygame No terminal ou prompt de comando, execute:pip install pygame

Como Executar
Baixe ou clone este repositório para a sua máquina.Navegue até a pasta do projeto.
Execute o arquivo principal do jogo:
python main.py

Controles 
TeclaAçãoSeta para EsquerdaMover para a esquerdaSeta para DireitaMover para a direitaSeta 
para CimaMover para cimaSeta para BaixoMover para baixo 
Estrutura do Códigomapa: 
Matriz de strings utilizada para construir visualmente a disposição das paredes (#) e pontos (.).livre(r, d):
Função de utilidade que calcula se o próximo movimento resultará em colisão com as 
paredes.alinhado(r): Valida se o elemento está centralizado em uma célula do grid antes de permitir mudanças de 
direção.fantasmas: Lista de dicionários que armazena a posição, direção e cor de cada fantasma.

Licença
Este projeto é de uso livre para fins educacionais e de estudo sobre desenvolvimento de jogos em Python.
