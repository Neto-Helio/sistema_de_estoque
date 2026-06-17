# 📦 Sistema de Controle de Estoque

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Database-green?style=for-the-badge&logo=sqlite)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

Sistema de controle de estoque desenvolvido em **Python** utilizando **SQLite** para persistência dos dados.

O projeto foi criado com o objetivo de praticar conceitos fundamentais de desenvolvimento back-end, banco de dados, lógica de programação e organização de código, simulando funcionalidades encontradas em sistemas reais de gerenciamento de estoque.

---

# 🚀 Funcionalidades

### 📋 Gerenciamento de Produtos

- Cadastro de produtos
- Listagem completa de produtos
- Atualização de informações
- Remoção de produtos
- Busca por:
  - Produto
  - Marca
  - ID

---

### 🔎 Busca Inteligente

O sistema possui correção de busca utilizando similaridade de texto.

Exemplo:

```text
Produto: aaroz

Produto não encontrado.
Você quis dizer 'Arroz'?
(S/N):
```

Isso melhora a experiência do usuário e reduz erros de digitação.

---

### 📥 Entrada de Estoque

Permite adicionar novas unidades a produtos já cadastrados.

Exemplo:

```text
Produto: Arroz
Quantidade Atual: 142

Adicionar: 20

Novo Estoque: 162
```

---

### 📤 Saída de Estoque

Permite registrar a retirada de produtos do estoque.

Exemplo:

```text
Produto: Arroz
Quantidade Atual: 162

Retirar: 10

Novo Estoque: 152
```

---

### ⚠️ Alerta Automático de Estoque

Sempre que o sistema é iniciado ou retorna ao menu principal, é realizada uma verificação automática dos produtos com estoque baixo.

Níveis de alerta:

| Situação | Indicador |
|-----------|-----------|
| Sem estoque | 🚨 |
| Estoque crítico | 🔴 |
| Estoque baixo | 🟡 |

Exemplo:

```text
⚠ ALERTA DE ESTOQUE

🚨 ID:9 | Sabonete | Nivea | SEM ESTOQUE
🔴 ID:5 | Iogurte | Danone | Apenas 4 unidades
🟡 ID:8 | Açúcar | União | Apenas 8 unidades
```

---

### 📊 Relatório de Estoque Baixo

Geração de relatórios com produtos abaixo do limite definido pelo usuário.

Exemplo:

```text
Digite o limite: 10
```

O sistema retorna todos os produtos com quantidade inferior ou igual ao valor informado.

---

# 🗄️ Banco de Dados

Estrutura da tabela principal:

```sql
CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT NOT NULL,
    marca TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    preco REAL NOT NULL
);
```

---

# 🛠️ Tecnologias Utilizadas

- Python
- SQLite
- SQL
- Git
- GitHub

---

# 🧠 Conceitos Aplicados

Durante o desenvolvimento deste projeto foram utilizados:

- CRUD Completo
- Banco de Dados Relacional
- SQL
- SQLite
- Modularização
- Funções
- Tratamento de Exceções
- Estruturas de Repetição
- Estruturas Condicionais
- Busca Aproximada com `difflib`
- Validação de Entradas
- Persistência de Dados

---

# 📷 Demonstração

## Menu Principal

Sistema desenvolvido em interface de terminal para foco na lógica de negócio e manipulação de dados.

### Funcionalidades disponíveis

- Cadastro de Produtos
- Listagem de Produtos
- Busca Inteligente
- Entrada de Estoque
- Saída de Estoque
- Atualização de Produtos
- Remoção de Produtos
- Relatórios
- Alertas Automáticos

---

# ▶️ Como Executar

Clone o repositório:

```bash
git clone https://github.com/Neto-Helio/sistema_de_estoque.git
```

Entre na pasta:

```bash
cd sistema_de_estoque
```

Execute:

```bash
python main.py
```

---

# 🎯 Objetivo do Projeto

Este projeto foi desenvolvido para consolidar conhecimentos em:

- Python
- SQL
- SQLite
- Estruturas de Dados
- Desenvolvimento de Sistemas
- Boas Práticas de Programação

Além de servir como projeto de portfólio para demonstrar evolução prática no desenvolvimento de software.

---

# 👨‍💻 Autor

### Hélio Neto

Projeto desenvolvido para fins de estudo, prática e construção de portfólio.

GitHub:
https://github.com/Neto-Helio

---

⭐ Caso tenha gostado do projeto, considere deixar uma estrela no repositório.