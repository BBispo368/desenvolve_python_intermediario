
# Aventura no Labirinto

Um jogo interativo de exploração de labirintos via terminal escrito em Python. Este projeto explora conceitos como funções recursivas, match-case, modularização e criação de CLIs.

## Estrutura do Projeto

- `aventura_pkg`: Pacote contendo toda a lógica do jogo (jogador, labirinto, utilitários).
- `main.py`: Ponto de entrada do sistema contendo a interface de linha de comando.
- `requirements.txt`: Dependências do projeto.
- `aventura_pkg.html`: Documentação das docstrings.

## Como Instalar e Executar

1. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```
2. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
3. Instale as dependências externas:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o jogo fornecendo o argumento obrigatório `--name`:
   ```bash
   python main.py --name "Seu Nome"
   ```

Você pode usar o comando `python main.py --help` para ver as outras opções disponíveis como `--color`, `--dificuldade`, etc.

## Como Jogar

Navegue pelo menu usando o número das opções e a tecla Enter. Durante o jogo, utilize as teclas `W`, `A`, `S`, `D` ou as `Setas Direcionais` do seu teclado para se mover. 
Seu objetivo é coletar itens (`I`) e alcançar o final (`E`) do labirinto partindo do início (`S`).
