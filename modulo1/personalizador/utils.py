import os

def obter_conteudo(texto: str, is_arquivo: bool) -> str:
    """
    Retorna o conteúdo do texto ou lê o arquivo se is_arquivo for True.
    """
    if is_arquivo:
        if os.path.exists(texto):
            with open(texto, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            return f"Erro: O arquivo '{texto}' não foi encontrado."
    return texto
