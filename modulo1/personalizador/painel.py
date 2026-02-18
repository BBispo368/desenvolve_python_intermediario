from rich.console import Console
from rich.panel import Panel
from .utils import obter_conteudo

def exibir_painel_simples(texto: str, is_arquivo: bool):
    """
    Exibe o texto dentro de um painel simples com borda padrão.
    """
    conteudo = obter_conteudo(texto, is_arquivo)
    console = Console()
    console.print(Panel(conteudo, title="Painel Simples"))

def exibir_painel_destaque(texto: str, is_arquivo: bool):
    """
    Exibe o texto dentro de um painel vermelho com subtítulo.
    """
    conteudo = obter_conteudo(texto, is_arquivo)
    console = Console()
    console.print(Panel(conteudo, title="[bold red]IMPORTANTE[/]", subtitle="Fim da mensagem", border_style="red"))
