"""
Módulo para controle do jogador.
"""
from pynput import keyboard

posicao = [1, 1]
pontuacao = 0
jogando = False
ultimo_movimento = None

def iniciar_jogador(pos_inicial=[1, 1]):
    """
    Inicia o jogador na posição informada e zera a pontuação.
    """
    global posicao, pontuacao, jogando, ultimo_movimento
    posicao = list(pos_inicial)
    pontuacao = 0
    jogando = True
    ultimo_movimento = None

def on_press(key):
    """
    Callback para leitura de teclas e atribuição do último movimento.
    """
    global ultimo_movimento, jogando
    if not jogando:
        return False
        
    try:
        if key == keyboard.Key.up or key.char == 'w':
            ultimo_movimento = 'C'
        elif key == keyboard.Key.down or key.char == 's':
            ultimo_movimento = 'B'
        elif key == keyboard.Key.left or key.char == 'a':
            ultimo_movimento = 'E'
        elif key == keyboard.Key.right or key.char == 'd':
            ultimo_movimento = 'D'
    except AttributeError:
        pass

def mover(labirinto):
    """
    Move o jogador de acordo com a última tecla pressionada e validando limites de paredes.
    """
    global ultimo_movimento, posicao
    
    nova_pos = list(posicao)
    if ultimo_movimento == 'C':
        nova_pos[0] -= 1
    elif ultimo_movimento == 'B':
        nova_pos[0] += 1
    elif ultimo_movimento == 'E':
        nova_pos[1] -= 1
    elif ultimo_movimento == 'D':
        nova_pos[1] += 1
        
    ultimo_movimento = None
    
    # Verifica se bateu na parede
    if 0 <= nova_pos[0] < len(labirinto) and 0 <= nova_pos[1] < len(labirinto[0]):
        if labirinto[nova_pos[0]][nova_pos[1]] != '#':
            posicao = nova_pos

def pontuar(labirinto):
    """
    Verifica se a posição do jogador possui um item para aumentar a pontuação.
    """
    global pontuacao
    r, c = posicao
    if labirinto[r][c] == 'I':
        pontuacao += 10
        labirinto[r][c] = ' ' # remove o item
    
    return labirinto

def resolver_labirinto_recursivo(labirinto, r, c, visitados):
    """
    Função recursiva que retorna a lista de comandos (C,B,E,D) para resolver o labirinto.
    """
    if r < 0 or r >= len(labirinto) or c < 0 or c >= len(labirinto[0]):
        return None
    if labirinto[r][c] == '#':
        return None
    if (r, c) in visitados:
        return None
        
    if labirinto[r][c] == 'E':
        return []
        
    visitados.add((r, c))
    
    # Cima
    res = resolver_labirinto_recursivo(labirinto, r - 1, c, visitados)
    if res is not None: return ['C'] + res
    # Baixo
    res = resolver_labirinto_recursivo(labirinto, r + 1, c, visitados)
    if res is not None: return ['B'] + res
    # Esquerda
    res = resolver_labirinto_recursivo(labirinto, r, c - 1, visitados)
    if res is not None: return ['E'] + res
    # Direita
    res = resolver_labirinto_recursivo(labirinto, r, c + 1, visitados)
    if res is not None: return ['D'] + res
    
    return None
