
def exibir_menu():
    print("\n=== Sistema de Controle de Estoque ===")
    print('1 - Adicionar um Produto')
    print('2 - Remover um Produto')
    print('3 - Atualizar a Quantidade')
    print('4 - Listar Produtos')
    print('5 - Sair do Programa')

def adicionar_produto(estoque):
    nome_produto = input("Digite o nome do produto: ").strip()
    quantidade = int(input(f"Digite a quantidade de {nome_produto}: "))
    if quantidade < 0:
        print("Quantidade Inválida! Deve ser maior que zero!")
        return
    if nome_produto in estoque:
        estoque[nome_produto] += quantidade
    else:
        estoque[nome_produto] = quantidade
    print(f"Quantidade adicionada com sucesso!")

def remover_produto(estoque):
    nome_produto = input("Digite o nome do produto a remover: ").strip()
    if nome_produto in estoque:
        del estoque[nome_produto]
        print(f"{nome_produto} removida com sucesso!")
    else:
        print('produto não encontrado no estoque!')

def atualizar_quantidade(estoque):
    nome_produto = input("Digite o nome do produto: ").strip()
    if nome_produto in estoque:
        nova_quantidade = int(input(f"Digite a quantidade de {nome_produto}: "))
        if nova_quantidade < 0:
            print('Quantidade inválida! Deve ser maior que zero!')
            return
        estoque[nome_produto] = nova_quantidade
        print(f"Quantidade de {nome_produto} atualizada para {nova_quantidade}.")
    else:
        print("Produto não encontrado no estoque!")


def listar_produtos(estoque):
    if not estoque:
        print('Nenhum produto encontrado no estoque!')
    else:
        print('\nProdutos no estoque:')
        for produto, quantidade in estoque.items():
            print(f'{produto}: {quantidade} unidades')

def sistema_de_estoque():
    estoque = {}
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção:").strip()
        if opcao == '1':
            adicionar_produto(estoque)
        elif opcao == '2':
            remover_produto(estoque)
        elif opcao == '3':
            atualizar_quantidade(estoque)
        elif opcao == '4':
            listar_produtos(estoque)
        elif opcao == '5':
            print("Encerrando o programa... Até logo!")
            break
        else:
            print("Opção Inválida! Tente novamente!")


# Iniciar o sistema
sistema_de_estoque()