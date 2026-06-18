from biblioteca.db import *

while True:
    limpar_tela()
    alerta_estoque()
    r = menu(['Cadastrar Produto', 'Listar Produtos', 'Buscar Produto', 'Entrada de Estoque', 'Saída de Estoque', 'Atualizar Produto', 'Remover Produto', 'Relatório de Estoque Baixo', 'Sair'])
    if r == 1:
        cabeçalho('Cadastrar produto')
        n = input("Produto: ")
        m = input("Marca: ")
        q = int(input("Quantidade: "))
        p = real()
        cadastrar(n, m, q, p)
        enter()
    elif r == 2:
        cabeçalho('Listar Produtos')
        listar()
        enter()
    elif r == 3:
        buscar()
        enter()
    elif r == 4:
        cabeçalho('Entrada de Estoque')
        entrada()
        enter()
    elif r == 5:
        cabeçalho('Saida de Estoque')
        saida()
        enter()
    elif r == 6:
        cabeçalho('Atualizar Produto')
        atualizar()
        enter()
    elif r == 7:
        cabeçalho('Remover Produto')
        remover()
        enter()
    elif r == 8:
        cabeçalho('Relatório de Estoque Baixo')
        relatorio_baixo_estoque()
        enter()
    if r == 9:
        break
print("Programa encerrado!")

