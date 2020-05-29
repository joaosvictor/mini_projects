#Desenvolvido por João Victor;
#Linkedin: https://www.linkedin.com/in/jo%C3%A3o-victor-santos-do-nascimento-0821861a1/

from time import sleep
from decimal import *
import datetime
#Inicio do programa: pedir nome;

nome = str(input('Informe seu nome: '))
print(' ')

#criando as opções de banco e fazendo o processo;
opcao = 0
while opcao != 9:
    print('''     1- Bradesco
     2- Itaú
     3- Santander
     4- Caixa
     5- Banco Do Brasil
     6- Banrisul
     7- Banco Safra
     8- Sicoob
     9- Encerrar o programa''')
    
    opcao = int(input(   'Qual das opções de 1 à 8 acima é o seu banco, {} ? Se quiser encerrar o processo aperte 9'.format(nome)))
    print(' ')
    if opcao == 1:
        print('{}, o Bradesco gera mensalmente 0,26% na poupança com a taxa selic maior de 8,5%!'.format(nome))
        a = 1000 * 0.026
        print('Se você tiver 1000 reais na conta você vai ter um lucro de: R${} reais'.format(a))
        
    elif opcao == 2:
        z = 1000 * 0.026
        print('{}, o Itaú gera mensalmente 0,26% na poupança com a taxa selic maior de 8,5%!'.format(nome)) 
        print('Se você tiver 1000 reais na conta você vai ter um lucro de: R${} reais'.format(z))
        
    elif opcao == 3:
        u = 1000 * 0.026
        print('{}, o Santander gera mensalmente 0,26% na poupança com a taxa selic maior de 8,5%!'.format(nome))   
        print('Se você tiver 1000 reais na conta você vai ter um lucro de: R${} reais'.format(u))
        
    elif opcao == 4:
        print('{}, a caixa gera mensalmente 0,5% na poupança com a taxa selic maior de 8,5%!'.format(nome)) 
        print('Se você tiver 1000 reais na conta você vai ter um lucro de: R$5.00 reais')
        
    elif opcao == 5:
        p = 1000 * 0.026
        print('{}, o Banco do Brasil gera mensalmente 0,26% na poupança com a taxa selic maior de 8,5%!'.format(nome))
        print('Se você tiver 1000 reais na conta você vai ter um lucro de: R${} reais'.format(p))
        
    elif opcao == 6:
        print('{}, o Banrisul gera mensalmente 0,5% na poupança com a taxa selic maior de 8,5%!'.format(nome))  
        print('Se você tiver 1000 reais na conta você vai ter um lucro de: $5.00 reais')
        
    elif opcao == 7:
        print('{}, o Banco Safra gera mensalmente 0,5% na poupança com a taxa selic maior de 8,5%!'.format(nome))
        print('Se você tiver 1000 reais na conta você vai ter um lucro de: R$5.00 reais')
        
    elif opcao == 8: 
        print('{}, o Banco Sicoob gera mensalmente 0,5% na poupança com a taxa selic maior de 8,5%!'.format(nome))
        print('Se você tiver 1000 reais na conta você vai ter um lucro de: R$5.00 reais')
        
    elif opcao == 9:
        print('Finalizando...')
    else:
        print('Ops... Essa não é uma opção válida! Tente novamente.')
        continue
        
    print(' ')
    print('-' * 90)
    break
    #finalinando a primeira parte do programa;
sleep(2.4)
#criando a segunda parte
print(' ')

#Parte 2 do processo
#criando o sistema de P.A para fazer o cálculo do imaginável
print('Agora vamos ver quanto você iria ganhar se investisse em ações. ?')
print(' ')
term = float(input("Digite o valor que você iria investir: " + '$' ))
razao = int(input("Por quantos meses você investiria: "))
decimo = term+ (10 - 1) * razao

c = term
'%.2f' % c
while(c < decimo+razao):
    c = c + razao

print("Nesses meses os seus {} ia virar, R${} reais.".format(term,c))
print(' ')

print('Acho que vale mais apena do que deixar o seu dinheiro na poupança em.')
#finalizando o processo da pa
sleep(2.4)
#Iniciando o processo de invesntimento de bolsa
print(' ')
print('Agora vou te ensinar o processo de investimento.')

choose = 0
while choose != 2:
    print('''     1- Longo prazo
     2- Curto prazo''')
    choose =int(input(   'Qual das opções acima é a sua preferência, {} ? '.format(nome)))
    print(' ')
    sleep(2.2)
    if choose == 1:
        print('''Vou te dar três ações para investir pelos próximos 20 anos:
Taesa - TAEE11
Itaúsa S.A – ITSA4
Ambev S.A – ABEV3
Por mês essas ações geram 0.38% com a taxa selic maior que 8.5%. Já é muito mais que a poupança do seu banco, não ?''')
    else:
        print('''Vou te dar três ações para investir no curto prazo:
Vivara - VIVA3
Copel - CPLE6
Lojas Renner - LREN3
Se você investir em qualquer uma dessas ações você já tera um lucro de 1.2% a mais do que na poupançã.''')
    print(' ')
    sleep(2.2)
    break
print('Uma ótima corretora para investir é a Clear Corretora.')
              
####
