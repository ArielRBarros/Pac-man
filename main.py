import pygame
import random

pygame.init()
pygame.font.init() 

tela = pygame.display.set_mode((640, 400))
relogio = pygame.time.Clock()
T = 40

fonte = pygame.font.SysFont("arial", 48, bold=True)

mapa = [
    "################",
    "#......##......#",
    "#.####.##.####.#",
    "#..............#",
    "#.##.######.##.#",
    "#......##......#",
    "###.##.##.##.###",
    "#..............#",
    "#...##....##...#",
    "################"
]

paredes = []
pontos = []
for y, linha in enumerate(mapa):
    for x, c in enumerate(linha):
        r = pygame.Rect(x * T, y * T, T, T)
        if c == "#":
            paredes.append(r)
        else:
            pontos.append(r.inflate(-32, -32))
            
pac = pygame.Rect(7 * T, 8 * T, T, T)
direcao = quer = (0, 0)
setas = {
    pygame.K_LEFT: (-1, 0), pygame.K_RIGHT: (1, 0),
    pygame.K_UP: (0, -1), pygame.K_DOWN: (0, 1)
}

fantasmas = [
    {"rect": pygame.Rect(7 * T, 3 * T, T, T), "dir": (1, 0), "cor": "red"},
    {"rect": pygame.Rect(8 * T, 3 * T, T, T), "dir": (-1, 0), "cor": "pink"},
    {"rect": pygame.Rect(7 * T, 5 * T, T, T), "dir": (0, 1), "cor": "cyan"},
    {"rect": pygame.Rect(8 * T, 5 * T, T, T), "dir": (0, -1), "cor": "orange"}
]

def livre(r, d):
    novo = r.move(d[0] * T, d[1] * T)
    return novo.collidelist(paredes) == -1

def alinhado(r):
    return r.x % T == 0 and r.y % T == 0

rodando = True
game_over = False
vitoria = False

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key in setas:
                quer = setas[evento.key]
    
    if not game_over and not vitoria:

        if alinhado(pac) and livre(pac, quer):
            direcao = quer
        if not alinhado(pac) or livre(pac, direcao):
            pac.x += direcao[0] * 5
            pac.y += direcao[1] * 5
            
        i = pac.collidelist(pontos)
        if i >= 0:
            pontos.pop(i)
            

        if len(pontos) == 0:
            vitoria = True

        for f in fantasmas:
            if alinhado(f["rect"]):
                possiveis = []
                for d in [(1,0), (-1,0), (0,1), (0,-1)]:
                    if livre(f["rect"], d):
                        possiveis.append(d)
                
                oposto = (-f["dir"][0], -f["dir"][1])
                if oposto in possiveis and len(possiveis) > 1:
                    possiveis.remove(oposto)
                    
                if possiveis:
                    f["dir"] = random.choice(possiveis)
                    
            f["rect"].x += f["dir"][0] * 5
            f["rect"].y += f["dir"][1] * 5
            
            if pac.colliderect(f["rect"]):
                game_over = True

    tela.fill("black")
    
    for r in paredes:
        pygame.draw.rect(tela, "mediumblue", r)
    for p in pontos:
        pygame.draw.circle(tela, "wheat", p.center, 4)
        
    cx, cy = pac.center
    pygame.draw.circle(tela, "yellow", (cx, cy), 17)
    dx, dy = direcao
    a = pygame.time.get_ticks() // 80 % 3 * 8
    p1 = (cx + dx * 20 - dy * a, cy + dy * 20 + dx * a)
    p2 = (cx + dx * 20 + dy * a, cy + dy * 20 - dx * a)
    pygame.draw.polygon(tela, "black", [(cx, cy), p1, p2])
    
    for f in fantasmas:
        fx, fy = f["rect"].center
        pygame.draw.circle(tela, f["cor"], (fx, fy), 17)
        pygame.draw.circle(tela, "white", (fx - 6, fy - 4), 5)
        pygame.draw.circle(tela, "white", (fx + 6, fy - 4), 5)
        pygame.draw.circle(tela, "blue", (fx - 6, fy - 4), 2)
        pygame.draw.circle(tela, "blue", (fx + 6, fy - 4), 2)

    if vitoria:
        texto = fonte.render("VOCÊ VENCEU!", True, "green")
        rect_texto = texto.get_rect(center=(320, 200))
        tela.blit(texto, rect_texto)
        pygame.display.flip()
        pygame.time.delay(3000) 
        rodando = False
        
    elif game_over:
        texto = fonte.render("GAME OVER!", True, "red")
        rect_texto = texto.get_rect(center=(320, 200))
        tela.blit(texto, rect_texto)
        pygame.display.flip()
        pygame.time.delay(3000) 
        rodando = False
    else:
        pygame.display.flip()

    relogio.tick(60)
        
pygame.quit()