import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def title():
    print('=-' * 20)
    print('           CÁLCULO DE IMC')
    print('=-' * 20)

def main():
    import re # Importa o módulo de expressões regulares

    while True:
        # Pede ao usuário para digitar o nome e remove espaços extras no início e no fim.
        nome = input('Qual o seu nome? ').strip()

        # Condição 1: Verifica se o nome está vazio.
        if not nome:
            print('O nome não pode estar em branco. Tente novamente.')
            continue # Volta para o início do laço

        # Condição 2: Verifica se o nome contém APENAS letras, espaços e acentos.
        # A expressão regular '^[a-zA-ZÀ-ú\s]+$' faz o seguinte:
        # ^       -> Começo da string
        # [ ... ] -> Um conjunto de caracteres permitidos
        # a-z     -> Letras minúsculas
        # A-Z     -> Letras maiúsculas
        # À-ú     -> Caracteres acentuados (cobre a maioria dos casos em português)
        # \s      -> Espaços em branco
        # +       -> O padrão anterior deve aparecer uma ou mais vezes
        # $       -> Fim da string
        if not re.match(r'^[a-zA-ZÀ-ú\s]+$', nome):
            print('O nome deve conter apenas letras e espaços. Tente novamente.')
            continue # Volta para o início do laço

        # Se todas as condições passaram, o nome é válido.
        break

    # Exibe o nome para confirmar.
    print(f'Olá, {nome}!')


    while True:
        try:
            peso =float(input('Qual o seu peso? (kg) '))
            if peso <= 0:
                print('O peso deve ser um valor positivo. Tente novamente.')
                continue
            break
        except ValueError:
            print('Entrada inválida para o peso. Por favor, digite um número.')
    
    while True:
        try:
            altura = float(input('Qual a sua altura? (m) '))
            if altura <= 0:
                print('A altura deve ser um valor positivo. Tente novamente.')
                continue
            break
        except ValueError:
            print('Entrda inválida para altura. Por favor digite um número.')
    
    # --- Cálculo do IMC ---
    # A divisão por zero já é prevenida pela validação de altura > 0
    imc = peso / (altura ** 2)
    
    # --- Apresentação do resultado ---
    print(f'O seu IMC é de {imc:.1f}')
    
    # --- Classificação do IMC ---
    if imc < 18.5:
        print('Você está ABAIXO DO PESO normal.')
    elif 18.5 <= imc < 25:
        print('PARABÉNS, você está na faixa de PESO NORMAL')
    elif 25 <= imc < 30:
        print('Você está em SOBREPESO.')
    elif 30 <= imc < 40:
        print('Você está em OBESIDADE.')
    else:
        print('Você está em OBESIDADE MÓRBIDA, cuidado!')

if __name__ == "__main__":
    clear()
    title()
    main() 
