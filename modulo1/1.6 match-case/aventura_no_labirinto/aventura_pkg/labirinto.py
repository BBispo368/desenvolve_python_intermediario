"""
Módulo para criação e gerenciamento do labirinto.
"""
import random

def criar_labirinto(dificuldade=1):
    """
    Cria um labirinto baseado na dificuldade escolhida.
    Gera as paredes, caminhos, inicio, fim e itens garantindo solução.
    Retorna a matriz do labirinto.
    """
    # Tamanho sempre ímpar para o algoritmo de labirinto perfeito funcionar
    tamanho = 5 + (dificuldade * 4)
    labirinto = [['#' for _ in range(tamanho)] for _ in range(tamanho)]
    
    def visit(r, c):
        labirinto[r][c] = ' '
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 1 <= nr < tamanho - 1 and 1 <= nc < tamanho - 1 and labirinto[nr][nc] == '#':
                labirinto[r + dr//2][c + dc//2] = ' '
                visit(nr, nc)

    # Inicia a geração a partir da posição inicial
    visit(1, 1)
                
    # Garantir inicio e fim
    labirinto[1][1] = 'S' # Start
    labirinto[tamanho-2][tamanho-2] = 'E' # End
    
    # Colocar itens
    num_itens = dificuldade * 2
    for _ in range(num_itens):
        while True:
            r = random.randint(1, tamanho - 2)
            c = random.randint(1, tamanho - 2)
            if labirinto[r][c] == ' ':
                labirinto[r][c] = 'I'
                break
                
    return labirinto

def imprimir_labirinto(labirinto, pos_jogador, cor="green"):
    """
    Imprime o labirinto na tela usando a biblioteca rich.
    """
    from rich.console import Console
    console = Console()
    
    for r in range(len(labirinto)):
        linha = ""
        for c in range(len(labirinto[r])):
            if r == pos_jogador[0] and c == pos_jogador[1]:
                linha += f"[{cor}]@[/{cor}]"
            elif labirinto[r][c] == '#':
                linha += "[white on white]#[/white on white]"
            elif labirinto[r][c] == 'I':
                linha += "[yellow]I[/yellow]"
            elif labirinto[r][c] == 'E':
                linha += "[bold red]E[/bold red]"
            elif labirinto[r][c] == 'S':
                linha += "[bold blue]S[/bold blue]"
            else:
                linha += " "
        console.print(linha)
