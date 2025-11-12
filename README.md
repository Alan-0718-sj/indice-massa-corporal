# Calculadora de IMC (Índice de Massa Corporal)

Uma aplicação de console simples e robusta, desenvolvida em Python, para calcular o Índice de Massa Corporal (IMC). O programa guia o usuário na inserção de seus dados, valida as informações para evitar erros e apresenta o resultado com a classificação correspondente.

---

## 🎥 Demonstração em Vídeo

Clique na imagem abaixo para assistir a uma demonstração completa do projeto no YouTube.

[![Demonstração da Calculadora de IMC](https://img.youtube.com/vi/ID_DO_SEU_VIDEO_AQUI/hqdefault.jpg)](https://www.youtube.com/watch?v=ID_DO_SEU_VIDEO_AQUI)

> **Como usar:**
> 1.  Faça o upload do seu vídeo para o YouTube.
> 2.  Pegue o ID do seu vídeo. Por exemplo, se o link for `https://www.youtube.com/watch?v=AbC123XyZ-0`, o ID é `AbC123XyZ-0`.
> 3.  Substitua `ID_DO_SEU_VIDEO_AQUI` nos dois lugares do link acima pelo ID do seu vídeo.

---

## ✨ Funcionalidades Principais

-   **Interface Limpa:** A tela do console é limpa a cada execução para uma experiência de usuário mais agradável.
-   **Validação de Entradas:**
    -   **Nome:** Verifica se o campo não está vazio e se contém apenas caracteres válidos (letras e espaços), utilizando expressões regulares (`regex`).
    -   **Peso e Altura:** Garante que os valores inseridos sejam numéricos e positivos, tratando exceções de `ValueError`.
-   **Cálculo Preciso:** Realiza o cálculo do IMC com base na fórmula padrão mundial: `peso / (altura ** 2)`.
-   **Classificação Automática:** Fornece um feedback imediato ao usuário, classificando o resultado em uma das seguintes categorias:
    -   Abaixo do peso
    -   Peso normal
    -   Sobrepeso
    -   Obesidade
    -   Obesidade Mórbida

---

## 🚀 Como Executar o Projeto

Este projeto utiliza apenas bibliotecas padrão do Python, então não há necessidade de instalar pacotes externos.

1.  **Pré-requisitos:**
    -   Certifique-se de ter o [Python 3](https://www.python.org/downloads/) instalado.

2.  **Clone o repositório:**
    ```bash
    git clone https://github.com/Alan-0718-sj/indice-massa-corporal.git
    ```

3.  **Navegue até o diretório do projeto:**
    ```bash
    cd nome-do-diretorio
    ```

4.  **Execute o script:**
    ```bash
    python IMC.py
    ```
    *(Substitua `IMC.py` pelo nome do seu arquivo, se for diferente)*

5.  **Siga as instruções** que aparecerão no terminal.

---

## 🛠️ Tecnologias Utilizadas

-   **Linguagem:** Python 3
-   **Bibliotecas Nativas:**
    -   `os`: Utilizada para interagir com o sistema operacional e limpar a tela do console.
    -   `re`: Utilizada para aplicar expressões regulares na validação do nome do usuário.