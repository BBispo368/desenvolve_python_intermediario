"""
Script principal para executar Aventura no Labirinto.
"""
import argparse
import time
from aventura_pkg import labirinto, jogador, utils
from pynput import keyboard
from rich.console import Console

console = Console()

def jogar_game(nome, cor, dificuldade, usar_som):
    """
    Laço principal de jogabilidade interativa.
    """
    console.print(f"[bold]Iniciando jogo para {nome} na dificuldade {dificuldade}[/bold]")
    lab = labirinto.criar_labirinto(dificuldade)
    jogador.iniciar_jogador([1, 1])
    
    listener = keyboard.Listener(on_press=jogador.on_press)
    listener.start()
    
    try:
        while jogador.jogando:
            console.clear()
            console.print(f"[{cor}]Jogador: {nome} | Pontuação: {jogador.pontuacao}[/{cor}]")
            labirinto.imprimir_labirinto(lab, jogador.posicao, cor)
            
            jogador.mover(lab)
            lab = jogador.pontuar(lab)
            
            r, c = jogador.posicao
            if lab[r][c] == 'E':
                jogador.jogando = False
                console.clear()
                utils.tela_vitoria(nome)
                break
                
            time.sleep(0.1)
    finally:
        listener.stop()

def ver_solucao(dificuldade):
    """
    Executa e exibe a solução recursiva para um labirinto gerado.
    """
    console.print(f"[bold]Assistindo solução automática para dificuldade {dificuldade}[/bold]")
    lab = labirinto.criar_labirinto(dificuldade)
    
    # Encontrar S
    inicio = (1, 1)
    for r in range(len(lab)):
        for c in range(len(lab[r])):
            if lab[r][c] == 'S':
                inicio = (r, c)
                
    solucao = jogador.resolver_labirinto_recursivo(lab, inicio[0], inicio[1], set())
    if solucao is None:
        console.print("[red]Este labirinto não tem solução devido à geração aleatória![/red]")
        return
        
    jogador.iniciar_jogador(inicio)
    for mov in solucao:
        console.clear()
        labirinto.imprimir_labirinto(lab, jogador.posicao)
        time.sleep(0.5)
        
        jogador.ultimo_movimento = mov
        jogador.mover(lab)
    
    console.clear()
    labirinto.imprimir_labirinto(lab, jogador.posicao)
    console.print("[bold green]Chegou ao final automaticamente![/bold green]")

def main():
    """
    Função principal e definição de CLI (Arguments & Options).
    """
    parser = argparse.ArgumentParser(description="Aventura no Labirinto CLI")
    # Pelo menos 5 elementos
    parser.add_argument('--name', type=str, required=True, help="Nome do(a) jogador(a) (Obrigatório)")
    parser.add_argument('--color', type=str, default="green", help="Escolher a cor principal do jogo (ex: green, red, blue)")
    parser.add_argument('--dificuldade', type=int, choices=[1, 2, 3], default=1, help="Nível de dificuldade do labirinto (1, 2, 3)")
    parser.add_argument('--disable-sound', action='store_true', help="Desligar o som do jogo")
    # O argparse adiciona --help automaticamente, então aqui estão os 5 elementos de CLI.
    
    args = parser.parse_args()
    
    while True:
        console.clear()
        console.print(f"[bold {args.color}]Bem-vindo(a) à Aventura no Labirinto, {args.name}! (Dificuldade Atual: {args.dificuldade})[/bold {args.color}]")
        utils.imprime_menu(args.color)
        
        opcao = input("Escolha uma opção: ")
        
        # Match-case
        match opcao:
            case "1":
                jogar_game(args.name, args.color, args.dificuldade, not args.disable_sound)
                input("Pressione Enter para continuar...")
            case "2":
                utils.imprime_instrucoes()
                input("Pressione Enter para voltar ao menu...")
            case "3":
                ver_solucao(args.dificuldade)
                input("Pressione Enter para continuar...")
            case "4":
                nova_dif = input("Digite a nova dificuldade (1, 2 ou 3): ")
                if nova_dif in ["1", "2", "3"]:
                    args.dificuldade = int(nova_dif)
                    console.print(f"[green]Dificuldade alterada para {nova_dif}![/green]")
                else:
                    console.print("[red]Dificuldade inválida![/red]")
                time.sleep(1)
            case "5":
                console.print("Obrigado por jogar!")
                break
            case _:
                console.print("[red]Opção inválida![/red]")
                time.sleep(1)

if __name__ == "__main__":
    main()
