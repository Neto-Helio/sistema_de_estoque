def leiaint(msg):
    while True:
        try:
            n = int(input(msg).strip())
        except (ValueError, TypeError):
            print('\033[31mERRO! Escreva apenas números.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuario não quis digitar este npumero\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def enter():
    input("Pressione ENTER para continuar!")

def real():
    while True:
        try:
            preco = float(input("Preço: R$ ").replace(",", "."))
            break
        except ValueError:
            print("Digite um valor válido!")
    return preco

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f"{c} - {i}")
        c += 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc

def menu_2(txt, lista):
    cabeçalho(txt)
    c = 1
    for i in lista:
        print(f"{c} - {i}")
        c += 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc

