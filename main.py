conjunto_de_numeros=[]
import math


def operação_com_ordem(NumA,NumB,sinal):
    NumA=int(NumA) 
    NumB=int(NumB)
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
                        somando=input('Escolha um numero para somar ou escreva uma letra para finalizar: ')
                        try: 
                            somando=int(somando)
                            conjunto_de_numeros.append(somando)
                        except:
                            print (f"resultado da soma: {sum(conjunto_de_numeros)}")
                            conjunto_de_numeros=[]
                            break
                    except Exception as apelido_do_erro:
                        print (f'Um erro foi encontrado: {apelido_do_erro}')
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
                            multiplicando=input('Escolha um numero para multiplicar ou escreva uma letra para finalizar: ')
                            try: 
                                multiplicando=int(multiplicando)
                                conjunto_de_numeros.append(multiplicando)
                            except:
                                print (f"resultado da multiplicação: {math.prod(conjunto_de_numeros)}")
                                conjunto_de_numeros=[]
                                break
                        except Exception as apelido_do_erro:
                            print (f'Um erro foi encontrado: {apelido_do_erro}')
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