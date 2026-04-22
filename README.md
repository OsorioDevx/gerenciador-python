# 🐍 gerenciador-python

> Projeto de aprendizado — Gerenciador de Tarefas em Python

---

## 📌 Sobre o Projeto

Este repositório documenta o aprendizado da linguagem Python pelo curso da Rockeseat, o projeto final é um **Gerenciador de Tarefas**. O objetivo é praticar conceitos fundamentais da linguagem de forma progressiva.

---

## 🐍 Por que Python?

- Linguagem de **alto nível**, com módulos prontos que em linguagens de baixo nível seriam extremamente complexos de implementar
- Mantida pela **Python Software Foundation**
- Possui muitas referências e influências da linguagem **C**
- Criada em **1990** originalmente para uso por pesquisadores
- Amplamente utilizada em ferramentas, scripts, automação, ciência de dados, IA e muito mais

---

## 📐 Conceitos Estudados

### Sintaxe

> Sintaxe é o conjunto de regras que define como o código deve ser escrito. Não seguir essas regras resulta em um `SyntaxError`.

### Comentários

```python
# Comentário de linha única

"""
Comentário de
múltiplas linhas (docstring)
"""
```

### Variáveis

```python
# Declaração de variáveis não pode conter acentos, espaços ou caracteres especiais
nome_completo = "Maria da Silva"

# Python diferencia maiúsculas de minúsculas (case-sensitive)
caseSensitive = "Python diferencia maiúsculas de minúsculas"

# snake_case → convenção para variáveis e funções em Python
snake_case = "variável escrita com palavras separadas por underline"

# camelCase → convenção para classes em Python
camelCase = "variável escrita com palavras juntas, cada uma iniciando com maiúscula, exceto a primeira"

numero_inteiro = 10
numero_decimal = 3.14
```

### Convenção de Nomenclatura

| Estilo | Uso em Python | Exemplo |
|---|---|---|
| `snake_case` | Variáveis e funções | `minha_variavel` |
| `CamelCase` | Classes | `MinhaClasse` |
| `UPPER_CASE` | Constantes | `VALOR_MAXIMO` |

> 💡 Consulte o **PEP 8** para conhecer todas as convenções de estilo do Python.

### Verificando Tipos

```python
# Use a função type() para verificar o tipo de uma variável
print("Tipo da variável numero_inteiro: ", type(numero_inteiro))   # <class 'int'>
print("Tipo da variável numero_decimal: ", type(numero_decimal))   # <class 'float'>
```

---

## 📁 Estrutura do Projeto

```
gerenciador-python/
├── olaMundo.py       # Primeiro script — Hello World
├── sintaxe.py        # Exemplos de sintaxe básica
├── variaveis.py      # Declaração e tipos de variáveis
├── README.md
└── LICENSE
```

---

## 🚀 Como Executar

**Pré-requisito:** Python 3.x instalado

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/gerenciador-python.git

# Acesse a pasta
cd gerenciador-python

# Execute um arquivo
python variaveis.py
```

---

## 📚 Referências

- [Documentação oficial do Python](https://docs.python.org/pt-br/3/)
- [PEP 8 — Guia de estilo para código Python](https://pep8.org/)
- [Python Software Foundation](https://www.python.org/psf/)