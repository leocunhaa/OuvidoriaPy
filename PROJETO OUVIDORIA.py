# PROGRAMA DE OUVIDORIA

listManifest = []
tiposManifest = ['Reclamação','Sugestão','Elogio']
lista = [1 or 2 or 3]

###### Definindo funções DEF's #######

# MANIFESTAÇÕES
def opcaoUM():
    print('Lista de manifestação: ')
    for manifest in listManifest:
        manifestQuebrada = manifest.split('#')
        print('Protocolo: {}'.format(manifestQuebrada[0]))
        print('Nome: {}'.format(manifestQuebrada[1]))
        print('Tipo: {}'.format(manifestQuebrada[2]))
        print('Descrição: {}'.format(manifestQuebrada[3]))
        print('')

# SUGESTÃO
def opcaoDois():
    print('Lista de sugestões: ')
    for manifest in listManifest:
        manifestQuebrada = manifest.split('#')
        if manifestQuebrada[2] == 'Sugestão':
            print('Protocolo: {}'.format(manifestQuebrada[0]))
            print('Nome: {}'.format(manifestQuebrada[1]))
            print('Tipo: {}'.format(manifestQuebrada[2]))
            print('Descrição: {}'.format(manifestQuebrada[3]))
            print('')
        elif manifestQuebrada[2] != 'Sugestão':
            print('')

# RECLAMAÇÃO
def opcaoTres():
    print('Lista de reclamação: ')
    for manifest in listManifest:
        manifestQuebrada = manifest.split('#')
        if manifestQuebrada[2] == 'Reclamação':
            print('Protocolo: {}'.format(manifestQuebrada[0]))
            print('Nome: {}'.format(manifestQuebrada[1]))
            print('Tipo: {}'.format(manifestQuebrada[2]))
            print('Descrição: {}'.format(manifestQuebrada[3]))
            print('')
        elif manifestQuebrada[2] != 'Reclamação':
            print('')
        
# ELOGIOS    
def opcaoQuatro():
    print('Lista de Elogios: ')
    for manifest in listManifest:
        manifestQuebrada = manifest.split('#')
        if manifestQuebrada[2] == 'Elogio':
            print('Protocolo: {}'.format(manifestQuebrada[0]))
            print('Nome: {}'.format(manifestQuebrada[1]))
            print('Tipo: {}'.format(manifestQuebrada[2]))
            print('Descrição: {}'.format(manifestQuebrada[3]))
            print('')
        elif manifestQuebrada[2] != 'Elogio':
            print('')
        
# PROTOCOLOS 
def opcaoSeis():
    print('~ PROTOCOLOS ~ ')
    for manifest in listManifest:
        manifestQuebrada = manifest.split('#')
        protocol = str(input('Digite o seu protocolo: '))
        if manifestQuebrada[0] == protocol:
            print('Protocolo: {}'.format(manifestQuebrada[0]))
            print('Nome: {}'.format(manifestQuebrada[1]))
            print('Tipo: {}'.format(manifestQuebrada[2]))
            print('Descrição: {}'.format(manifestQuebrada[3]))
            print('')
       
# MENU
while True:
    print('''Ouvidoria Universidade ABC
    1) Listar todas as manifestações 
    2) Listar todas as sugestões
    3) Listar todas as reclamações
    4) Listar todos os elogios
    5) Enviar uma manifestação (criar uma nova)
    6) Pesquisar protocolo por número (ID)
    7) Sair''')
    opcao = int(input('Digite uma opção: '))

    if opcao == 1:
        opcaoUM()
    
    elif opcao == 2:
        opcaoDois()
     
    elif opcao == 3:
        opcaoTres()
     
    elif opcao == 4:
        opcaoQuatro()

    elif opcao == 5:
        print('Nova manifestação: ')
        nome = input('Digite seu nome: ')
        todasManifest = len(tiposManifest)
        for i in range(todasManifest):
            print(i + 1,')',tiposManifest[i])
        tipos = int(input('Digite o tipo de manifestação: '))
        while True:
            if tipos == 1 or tipos == 2 or tipos == 3:
                break
            tipos = int(input('Digite o tipo de manifestação: '))
        descricao = input('Digite a descrição: ')
        protocolo = str(len(listManifest) + 1)
        manifestacao = protocolo + '#' + nome + '#' + tiposManifest[tipos - 1] + '#' + descricao
        listManifest.append(manifestacao)

    elif opcao == 6:
        opcaoSeis()

    elif opcao == 7:
        print('Fim do programa!')
        break
    
    else:
        print('Opção inválida!')


    
    

