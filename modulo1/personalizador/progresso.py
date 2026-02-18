import time
from rich.console import Console
from rich.progress import track, Progress, SpinnerColumn, TextColumn
from .utils import obter_conteudo

def simular_carregamento(texto: str, is_arquivo: bool):
    """
    Simula uma barra de progresso antes de exibir o texto.
    """
    conteudo = obter_conteudo(texto, is_arquivo)
    console = Console()
    
    # Simula um processamento
    for _ in track(range(10), description="Processando texto..."):
        time.sleep(0.1)
        
    console.print(f"\n[green]Concluído![/]\n{conteudo}")

def exibir_com_spinner(texto: str, is_arquivo: bool):
    """
    Exibe um spinner animado enquanto 'prepara' o texto para exibição.
    """
    conteudo = obter_conteudo(texto, is_arquivo)
    console = Console()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Carregando...", total=None)
        time.sleep(2)  # Simula tempo de carga
        
    console.print(Panel(conteudo, title="Carregamento Finalizado"))
