#importar 'os' para limpar o terminal 
import os
#cria lista vazia 
lista_compras = []

#cria função para adicionar itens na lista
def adicionar_item(item, lista):
    lista.append(item)
    print(f'\n{item} foi adicionado a lista.')

#cria função para remover itens da lista
def retirar_item(item, lista):
    if item in lista:
        lista.remove(item)
        print(f'\n{item} foi removido da lista.')
    else:
        print(
            f'\n{item} não está na lista,nenhum item foi retirado.')

#cria função que exibe os itens colocados na lista
def exibir_lista(lista):
    print('\nlista de compras:\n')
    i = 1
    for i, item in enumerate(lista):
        i += 1
        print(f'{i}- {item}')
    print()

#Menu de interação com o usuário 
while True:
    print("Opções:")
    print('1) Adicionar item à lista:')
    print('2) Remova um item da lista:')
    print('3) Exibir a lista:')
    print('4) Sair:')
#entrada para interagir com o menu
    escolha = input('Escolha uma das opções: ')
#condicionais para as funções criadas
    if escolha == '1':
        os.system('cls')
        adc_item = input(
            'Digite o nome do item que deseja adicionar: '
        )
        adicionar_item(adc_item, lista_compras)
        print()
    elif escolha == '2':
        os.system('cls')
        remove_item = input(
            'Digite o nome do item que deseja remover: '
        )
        retirar_item(remove_item, lista_compras)
        print()
    elif escolha == '3':
        os.system('cls')
        exibir_lista(lista_compras)
        print()
    elif escolha == '4':
        os.system('cls')
        print('\nsaindo da lista, sua lista é essa:')
        exibir_lista(lista_compras)
        break

    else:
        os.system('cls')
        print('\nOpção inválida, escolha uma das opções:')
        print()
