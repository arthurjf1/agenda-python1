import os
agenda=[]
sair=False
while(sair==False):
    print("lista de opçoes")
    print("1-novo contato")
    print("2-listar contatos")
    print("3-editar contato")
    print("4-excluir contato\n")
    opcao=int(input("digite a opção escolhida....."))
    
    if(opcao==1):#add novo contato
        novo_contato=[]
        nome=input("\nDigite o nome do contato:")
        novo_contato.append(nome)
        telefone=input("Digite o telefone do contato:")
        novo_contato.append(telefone)
        agenda.append(novo_contato)
        os.system('cls')

    if(opcao==2):
        for contato in agenda:
            print("\nNome:",contato[0],"telefone:",contato[1],"\n")
           
