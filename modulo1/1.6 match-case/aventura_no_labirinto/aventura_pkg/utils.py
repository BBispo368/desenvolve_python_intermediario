"""
Módulo de utilitários para o jogo.
Contém funções para impressão de menus, instruções e telas de fim de jogo.
"""
from rich.console import Console
from rich.panel import Panel
import time

console = Console()

def imprime_instrucoes():
    """
    Imprime as instruções do jogo na tela lendo de uma string formatada.
    """
    instrucoes = "Use as setas ou W, A, S, D para mover.\nColete os itens 'I' e chegue ao final 'E'."
    console.print(Panel(instrucoes, title="[bold yellow]Instruções do Jogo[/bold yellow]", expand=False))

def imprime_menu(color="green"):
    """
    Imprime o menu inicial do jogo.
    """
    console.print(f"[{color}]1 - Jogar[/{color}]")
    console.print(f"[{color}]2 - Instruções[/{color}]")
    console.print(f"[{color}]3 - Solução Automática[/{color}]")
    console.print(f"[{color}]4 - Mudar Dificuldade[/{color}]")
    console.print(f"[{color}]5 - Sair[/{color}]")

def tela_vitoria(jogador_nome):
    """
    Imprime a tela de vitória.
    """
    console.print(Panel(f"[bold green]Parabéns, {jogador_nome}! Você venceu o labirinto![/bold green]", expand=False))
    animacao_vitoria(5)

def tela_derrota(jogador_nome):
    """
    Imprime a tela de derrota.
    """
    console.print(Panel(f"[bold red]Que pena, {jogador_nome}! Você perdeu![/bold red]", expand=False))

def animacao_vitoria(passos):
    """
    Função recursiva para fazer uma animação simples de vitória.
    """
    if passos <= 0:
        console.print("[bold yellow]🏆 FIM DA AVENTURA 🏆[/bold yellow]")
        return
    console.print("[bold green]✨ " * passos)
    time.sleep(0.3)
    animacao_vitoria(passos - 1)
