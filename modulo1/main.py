import argparse
import sys
from personalizador import layout, painel, progresso, estilo

# Mapeamento de módulos e funções
MAPA_MODULOS = {
    '1': {'nome': 'layout', 'mod': layout, 'funcs': {'1': layout.exibir_layout_dividido, '2': layout.exibir_layout_lado_a_lado, 'dividido': layout.exibir_layout_dividido, 'lado': layout.exibir_layout_lado_a_lado}},
    'layout': {'nome': 'layout', 'mod': layout, 'funcs': {'1': layout.exibir_layout_dividido, '2': layout.exibir_layout_lado_a_lado, 'dividido': layout.exibir_layout_dividido, 'lado': layout.exibir_layout_lado_a_lado}},
    
    '2': {'nome': 'painel', 'mod': painel, 'funcs': {'1': painel.exibir_painel_simples, '2': painel.exibir_painel_destaque, 'simples': painel.exibir_painel_simples, 'destaque': painel.exibir_painel_destaque}},
    'painel': {'nome': 'painel', 'mod': painel, 'funcs': {'1': painel.exibir_painel_simples, '2': painel.exibir_painel_destaque, 'simples': painel.exibir_painel_simples, 'destaque': painel.exibir_painel_destaque}},
    
    '3': {'nome': 'progresso', 'mod': progresso, 'funcs': {'1': progresso.simular_carregamento, '2': progresso.exibir_com_spinner, 'barra': progresso.simular_carregamento, 'spinner': progresso.exibir_com_spinner}},
    'progresso': {'nome': 'progresso', 'mod': progresso, 'funcs': {'1': progresso.simular_carregamento, '2': progresso.exibir_com_spinner, 'barra': progresso.simular_carregamento, 'spinner': progresso.exibir_com_spinner}},
    
    '4': {'nome': 'estilo', 'mod': estilo, 'funcs': {'1': estilo.exibir_estilo_bold_cyan, '2': estilo.exibir_estilo_reverso, 'cyan': estilo.exibir_estilo_bold_cyan, 'reverso': estilo.exibir_estilo_reverso}},
    'estilo': {'nome': 'estilo', 'mod': estilo, 'funcs': {'1': estilo.exibir_estilo_bold_cyan, '2': estilo.exibir_estilo_reverso, 'cyan': estilo.exibir_estilo_bold_cyan, 'reverso': estilo.exibir_estilo_reverso}},
}

def main():
    parser = argparse.ArgumentParser(description="Ferramenta de formatação de texto usando Rich.")
    parser.add_argument("texto", help="Texto a ser exibido ou caminho do arquivo (se a flag -a for usada).")
    parser.add_argument("-a", "--arquivo", action="store_true", help="Indica que o argumento 'texto' é um caminho para um arquivo.")
    parser.add_argument("-m", "--modulo", required=True, help="Escolha o módulo: 1 (layout), 2 (painel), 3 (progresso), 4 (estilo).")
    parser.add_argument("-f", "--funcao", required=True, help="Escolha a função: 1 ou 2 (ou nome da função).")

    args = parser.parse_args()

    if args.modulo in MAPA_MODULOS:
        info_modulo = MAPA_MODULOS[args.modulo]
        funcoes = info_modulo['funcs']
        
        if args.funcao in funcoes:
            funcao_escolhida = funcoes[args.funcao]
            print(f"Executando: Módulo {info_modulo['nome']} -> Função {funcao_escolhida.__name__}\n")
            funcao_escolhida(args.texto, args.arquivo)
        else:
            print(f"Erro: Função '{args.funcao}' não encontrada no módulo '{args.modulo}'.")
    else:
        print(f"Erro: Módulo '{args.modulo}' não encontrado.")

if __name__ == "__main__":
    main()
