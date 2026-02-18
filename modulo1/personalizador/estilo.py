from rich.console import Console
from rich.style import Style
from .utils import obter_conteudo

def exibir_estilo_bold_cyan(texto: str, is_arquivo: bool):
    """
    Exibe o texto em negrito e cor ciano.
    """
    conteudo = obter_conteudo(texto, is_arquivo)
    console = Console()
    estilo = Style(color="cyan", bold=True)
    console.print(conteudo, style=estilo)

def exibir_estilo_reverso(texto: str, is_arquivo: bool):
    """
    Exibe o texto com as cores de fundo e frente invertidas.
    """
    conteudo = obter_conteudo(texto, is_arquivo)
    console = Console()
    estilo = Style(reverse=True)
    console.print(conteudo, style=estilo)
