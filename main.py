import math
conjunto_de_numeros=[]

def operação_sem_ordem(escolha_menu,conjunto_de_numeros):
    try:
        if int(escolha_menu)==(1):
            return (f"resultado da soma: {sum(conjunto_de_numeros)}")
        else:
            return (f"resultado da multiplicação: {math.prod(conjunto_de_numeros)}")
    except Exception as apelido_do_erro:
        return (f'Um erro foi encontrado: {apelido_do_erro}')


def operação_com_ordem(NumA,NumB,sinal):
    try:
        NumA=int(NumA) 
        NumB=int(NumB)
    except ValueError:
        return ('Um ou mais valores não são numeros.')

    if sinal==('-'):
        resultado=NumA-NumB
    else:
        try:
            resultado=NumA//NumB
            resto=NumA%NumB
        except:
            return "não é possivel dividir por zero."

    if sinal==('-'):
        return (f"resultado da subtração: {resultado}.")
    else:
        return (f"resultado da divisão: {resultado} com resto {resto}.")

while True:
    escolha_menu=input ('\n\n\n\nMenu da Calculadora\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Sair\nEscolha a operação: ')
    try:
        if int(escolha_menu)>0 and int(escolha_menu)<5:

            #faz soma
            if int(escolha_menu)==1:
                while True:
                    try:
                        numeros=input('Escolha um numero para somar ou escreva uma letra para finalizar: ')
                        numeros=int(numeros)
                        conjunto_de_numeros.append(numeros)
                    except:
                        resultado=operação_sem_ordem(escolha_menu,conjunto_de_numeros)
                        print (resultado)
                        conjunto_de_numeros=[]
                        break


            #faz subtração
            elif int(escolha_menu)==2:
                try:
                    NumA=input('Escolha o primeiro numero: ')
                    NumB=input('Escolha o segundo numero: ')
                    sinal=('-')
                    resultado=operação_com_ordem(NumA,NumB,sinal)
                    print (resultado)
                except Exception as apelido_do_erro:
                    print (f'Um erro foi encontrado: {apelido_do_erro}')


            #faz multiplicação
            elif int(escolha_menu)==3:
                while True:
                    try:
                        numeros=input('Escolha um numero para Multiplicar ou escreva uma letra para finalizar: ')
                        numeros=int(numeros)
                        conjunto_de_numeros.append(numeros)
                    except:
                        resultado=operação_sem_ordem(escolha_menu,conjunto_de_numeros)
                        print (resultado)
                        conjunto_de_numeros=[]
                        break


            #faz divisão
            elif int(escolha_menu)==4:
                try:
                    NumA=input('Escolha o primeiro numero: ')
                    NumB=input('Escolha o segundo numero: ')
                    sinal=('/')
                    resultado=operação_com_ordem(NumA,NumB,sinal)
                    print (resultado)
                except Exception as apelido_do_erro:
                    print (f'Um erro foi encontrado: {apelido_do_erro}')



        #fecha programa se opção for 5, ou printa que não faz parte.
        elif int(escolha_menu)==5:
            break
        else:
            print ('Opção não faz parte do menu.')

        #Fecha o programa caso receba "sair" e Continua se for inesistente.
    except Exception as apelido_do_erro:
        print (f'opção inesistente, ou um erro foi encontrado: {apelido_do_erro}')