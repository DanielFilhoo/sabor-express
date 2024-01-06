import os

restaurantes = [
    {'nome': 'BK', 'categoria': 'Fast Food', 'ativo': False},
    {'nome': 'MAC', 'categoria': 'Fast Food', 'ativo': True},
    {'nome': 'BOBS', 'categoria': 'Fast Food', 'ativo': False}
]

def exibir_nome_programa():
    print('🇸🇦🇧🇴🇷 🇪🇽🇵🇷🇪🇸🇸\n')

def exibir_opcoes():
    print('1. Cadastrar restaurantes')
    print('2. Listar restaurantes')
    print('3. Alternar estado dos restaurantes')
    print('4. Sair')

def finalizar_app():
    exibir_subtitulo_menu('Encerrando o APP')

def voltar_menu_principal():
    input('Digite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_menu_principal()

def exibir_subtitulo_menu(texto):
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_restaurantes():
    exibir_subtitulo_menu('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado!')
    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo_menu('Listando os restaurantes')

    print(f'{"Nome do Restaurante".ljust(20)} | {"Categoria".ljust(20)} | Status')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo_menu('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    print(f'{"Nome do Restaurante".ljust(20)} | {"Categoria".ljust(20)} | Status')
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            estado_anterior = 'Ativado' if restaurante['ativo'] else 'Desativado'
            restaurante['ativo'] = not restaurante['ativo']
            estado_novo = 'Ativado' if restaurante['ativo'] else 'Desativado'
            mensagem = f'O restaurante {nome_restaurante} foi {estado_anterior} para {estado_novo}'
            print(mensagem)

    if not restaurante_encontrado:
        print('Restaurante não encontrado')

    voltar_menu_principal()

def escolher_opcoes():
    
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_restaurantes()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    
    except ValueError:
        opcao_invalida()

def main():
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
