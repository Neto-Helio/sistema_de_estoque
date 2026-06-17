import sqlite3
from biblioteca.interface import *
from difflib import get_close_matches

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS produtos(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
produto TEXT NOT NULL,
marca TEXT NOT NULL,
quantidade INTEGER NOT NULL,
preco REAL NOT NULL
)""")

def cadastrar(n, m, q, p):
    cursor.execute(""" INSERT INTO produtos
    (produto, marca, quantidade, preco)
    VALUES (?, ?, ?, ?) """, (n, m, q, p))
    conexao.commit()
    print(f"O produto {n} foi cadastrado com sucesso!")

def listar():
    cursor.execute("""SELECT * FROM produtos""")
    dado = cursor.fetchall()
    print(f"{'ID':<5} {'Produto':<10} {'Marca':<10} {'Quantidade':<15} {'Preço':<5}")
    print(linha(55))
    for dados in dado:
        preco = f"{dados[4]:.2f}".replace(".", ",")
        print(f"{dados[0]:<5} {dados[1]:<10} {dados[2]:<10} {dados[3]:<15} R$ {preco}")

def buscar_produto():

    nome = input("Produto: ").strip()

    cursor.execute(
        "SELECT * FROM produtos WHERE LOWER(produto) = LOWER(?)",
        (nome,)
    )

    produto = cursor.fetchone()

    if produto:
        print("\nPRODUTO ENCONTRADO")
        print("-" * 50)
        print(f"ID: {produto[0]}")
        print(f"Produto: {produto[1]}")
        print(f"Marca: {produto[2]}")
        print(f"Quantidade: {produto[3]}")
        print(f"Preço: R$ {produto[4]:.2f}".replace(".", ","))
        return

    # Busca sugestões
    cursor.execute("SELECT produto FROM produtos")

    lista_produtos = [linha[0] for linha in cursor.fetchall()]

    sugestao = get_close_matches(
        nome,
        lista_produtos,
        n=1,
        cutoff=0.6
    )

    if sugestao:

        print(f"\nProduto não encontrado.")
        print(f"Você quis dizer '{sugestao[0]}'?")

        while True:

            resposta = input("(S/N): ").strip().upper()

            if resposta == "S":

                cursor.execute(
                    "SELECT * FROM produtos WHERE produto = ?",
                    (sugestao[0],)
                )

                produto = cursor.fetchone()

                print("\nPRODUTO ENCONTRADO")
                print("-" * 50)
                print(f"ID: {produto[0]}")
                print(f"Produto: {produto[1]}")
                print(f"Marca: {produto[2]}")
                print(f"Quantidade: {produto[3]}")
                print(f"Preço: R$ {produto[4]:.2f}".replace(".", ","))

                break

            elif resposta == "N":
                print("Busca cancelada.")
                break

            else:
                print("Digite apenas S ou N.")

    else:
        print("\nProduto não encontrado.")

def buscar_marca():

    nome_marca = input("Digite a marca: ").strip()

    cursor.execute(
        "SELECT * FROM produtos WHERE LOWER(marca) = LOWER(?)",
        (nome_marca,)
    )

    produtos = cursor.fetchall()

    if produtos:

        print("\nMARCA ENCONTRADA")
        print("-" * 70)

        for produto in produtos:
            print(
                f"{produto[0]:<5}"
                f"{produto[1]:<15}"
                f"{produto[2]:<15}"
                f"{produto[3]:<10}"
                f"R$ {produto[4]:.2f}".replace(".", ",")
            )

        return

    # Busca sugestões
    cursor.execute("SELECT DISTINCT marca FROM produtos")

    lista_marcas = [linha[0] for linha in cursor.fetchall()]

    sugestao = get_close_matches(
        nome_marca,
        lista_marcas,
        n=1,
        cutoff=0.6
    )

    if sugestao:

        print(f"\nMarca não encontrada.")
        print(f"Você quis dizer '{sugestao[0]}'?")

        while True:

            resposta = input("(S/N): ").strip().upper()

            if resposta == "S":

                cursor.execute(
                    "SELECT * FROM produtos WHERE marca = ?",
                    (sugestao[0],)
                )

                produtos = cursor.fetchall()

                print("\nPRODUTOS DA MARCA")
                print("-" * 70)

                for produto in produtos:
                    preco = f"{produto[4]:.2f}".replace(".", ",")

                    print(
                        f"{produto[0]:<5}"
                        f"{produto[1]:<15}"
                        f"{produto[2]:<15}"
                        f"{produto[3]:<10}"
                        f"R$ {preco}"
                    )

                break

            elif resposta == "N":
                print("Busca cancelada.")
                break

            else:
                print("Digite apenas S ou N.")

    else:
        print("\nMarca não encontrada.")

def buscar_id():

    try:
        id_produto = int(input("Digite o ID do produto: "))
    except ValueError:
        print("Digite apenas números.")
        return

    cursor.execute(
        "SELECT * FROM produtos WHERE id = ?",
        (id_produto,)
    )

    produto = cursor.fetchone()

    if produto:

        preco = f"{produto[4]:.2f}".replace(".", ",")

        print("\nPRODUTO ENCONTRADO")
        print("-" * 50)
        print(f"ID: {produto[0]}")
        print(f"Produto: {produto[1]}")
        print(f"Marca: {produto[2]}")
        print(f"Quantidade: {produto[3]}")
        print(f"Preço: R$ {preco}")

    else:
        print("ID não encontrado.")

def buscar():
    r = menu_2('Escolha como buscar', ['Produto', 'Marca', 'ID'])
    if r == 1:
        buscar_produto()
    elif r == 2:
        buscar_marca()
    elif r == 3:
        buscar_id()

def entrada():
    nq = leiaint('Adicionar: ')
    id = leiaint('ID: ')
    cursor.execute("""UPDATE produtos 
    SET quantidade = quantidade + ?
    WHERE id = ?""", (nq, id))
    conexao.commit()
    print("Adicionado com sucesso!")

def saida():
    nq = leiaint('Retirar: ')
    id = leiaint('ID: ')
    cursor.execute("""UPDATE produtos 
    SET quantidade = quantidade - ?
    WHERE id = ?""", (nq, id))
    conexao.commit()
    print("Retirado com sucesso!")

def atualizar():

    while True:

        id_produto = leiaint("ID: ")

        cursor.execute(
            "SELECT * FROM produtos WHERE id = ?",
            (id_produto,)
        )

        produto = cursor.fetchone()

        if not produto:
            print("Produto não encontrado.")
            return

        print("\nProduto encontrado:")
        print(f"ID: {produto[0]}")
        print(f"Produto: {produto[1]}")
        print(f"Marca: {produto[2]}")
        print(f"Quantidade: {produto[3]}")
        print(f"Preço: R$ {produto[4]:.2f}".replace(".", ","))

        confirmacao = input(
            "\nÉ este produto que deseja atualizar? (S/N): "
        ).strip().upper()

        if confirmacao == "S":
            break

        elif confirmacao == "N":
            print("\nDigite outro ID.")
            continue

        else:
            print("Digite apenas S ou N.")
            continue

    print("\nO que deseja atualizar?")
    print("1 - Produto")
    print("2 - Marca")
    print("3 - Quantidade")
    print("4 - Preço")

    opcao = input("Escolha: ")

    if opcao == "1":

        novo_produto = input("Novo nome do produto: ")

        cursor.execute(
            "UPDATE produtos SET produto = ? WHERE id = ?",
            (novo_produto, id_produto)
        )

    elif opcao == "2":

        nova_marca = input("Nova marca: ")

        cursor.execute(
            "UPDATE produtos SET marca = ? WHERE id = ?",
            (nova_marca, id_produto)
        )

    elif opcao == "3":

        try:
            nova_quantidade = int(input("Nova quantidade: "))
        except ValueError:
            print("Quantidade inválida.")
            return

        cursor.execute(
            "UPDATE produtos SET quantidade = ? WHERE id = ?",
            (nova_quantidade, id_produto)
        )

    elif opcao == "4":

        try:
            novo_preco = float(
                input("Novo preço: ").replace(",", ".")
            )
        except ValueError:
            print("Preço inválido.")
            return

        cursor.execute(
            "UPDATE produtos SET preco = ? WHERE id = ?",
            (novo_preco, id_produto)
        )

    else:
        print("Opção inválida.")
        return

    conexao.commit()

    print("\nProduto atualizado com sucesso!")

def remover():

    while True:

        id_produto = leiaint("ID: ")

        cursor.execute(
            "SELECT * FROM produtos WHERE id = ?",
            (id_produto,)
        )

        produto = cursor.fetchone()

        if not produto:
            print("Produto não encontrado.")
            return

        print("\nProduto encontrado:")
        print(f"ID: {produto[0]}")
        print(f"Produto: {produto[1]}")
        print(f"Marca: {produto[2]}")
        print(f"Quantidade: {produto[3]}")
        print(f"Preço: R$ {produto[4]:.2f}".replace(".", ","))

        confirmacao = input(
            "\nÉ este produto que deseja remover? (S/N): "
        ).strip().upper()

        if confirmacao == "S":
            break

        elif confirmacao == "N":
            print("\nDigite outro ID.")
            continue

        else:
            print("Digite apenas S ou N.")
            continue

    confirmacao_final = input(
        "\nTem certeza que deseja remover este produto? (S/N): "
    ).strip().upper()

    if confirmacao_final != "S":
        print("Remoção cancelada.")
        return

    cursor.execute(
        "DELETE FROM produtos WHERE id = ?",
        (id_produto,)
    )

    conexao.commit()

    print("\nProduto removido com sucesso!")

def relatorio_baixo_estoque():

    limite = leiaint(
        "Mostrar produtos com quantidade menor ou igual a: "
    )

    cursor.execute(
        "SELECT * FROM produtos WHERE quantidade <= ? ORDER BY quantidade",
        (limite,)
    )

    produtos = cursor.fetchall()

    if not produtos:
        print("\nNenhum produto com estoque baixo.")
        return

    print("\nRELATÓRIO DE BAIXO ESTOQUE")
    print("-" * 70)

    print(
        f"{'ID':<5}"
        f"{'PRODUTO':<15}"
        f"{'MARCA':<15}"
        f"{'QTD':<10}"
        f"{'PREÇO'}"
    )

    print("-" * 70)

    for produto in produtos:

        preco = f"{produto[4]:.2f}".replace(".", ",")

        print(
            f"{produto[0]:<5}"
            f"{produto[1]:<15}"
            f"{produto[2]:<15}"
            f"{produto[3]:<10}"
            f"R$ {preco}"
        )

    print("-" * 70)

def alerta_estoque():
    cursor.execute(
        "SELECT id, produto, marca, quantidade "
        "FROM produtos "
        "WHERE quantidade < 10 "
        "ORDER BY quantidade ASC"
    )

    produtos = cursor.fetchall()

    if not produtos:
        return

    print("=" * 70)
    print("⚠ ALERTA DE ESTOQUE")
    print("=" * 70)

    for id_produto, produto, marca, quantidade in produtos:

        if quantidade == 0:
            print(
                f"🚨 ID:{id_produto} | "
                f"{produto} | "
                f"{marca} | "
                f"SEM ESTOQUE"
            )

        elif quantidade <= 5:
            print(
                f"🔴 ID:{id_produto} | "
                f"{produto} | "
                f"{marca} | "
                f"Apenas {quantidade} unidades"
            )

        else:
            print(
                f"🟡 ID:{id_produto} | "
                f"{produto} | "
                f"{marca} | "
                f"Apenas {quantidade} unidades"
            )

    print("=" * 70)