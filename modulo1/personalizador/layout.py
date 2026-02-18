from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from .utils import obter_conteudo

def exibir_layout_dividido(texto: str, is_arquivo: bool):
    """
    Exibe o texto em um layout dividido verticalmente (topo e base).
    """
    conteudo = obter_conteudo(texto, is_arquivo)
    console = Console()
    layout = Layout()
    layout.split_column(
        Layout(name="topo"),
        Layout(name="base")
    )
    layout["topo"].update(Panel(conteudo, title="Conteúdo Principal"))
    layout["base"].update(Panel("Rodapé do Layout", title="Info"))
    console.print(layout)

def exibir_layout_lado_a_lado(texto: str, is_arquivo: bool):
    """
    Exibe o texto em um layout dividido horizontalmente.
    """
    conteudo = obter_conteudo(texto, is_arquivo)
    console = Console()
    layout = Layout()
    layout.split_row(
        Layout(Panel(conteudo, title="Esquerda"), name="left"),
        Layout(Panel("Área Lateral Reservada", title="Direita"), name="right"),
    )
    console.print(layout)
