import funcoes
from funcoes import *

#Teste - VIA CMD 

"""
         Funções 

"""

if __name__ == "__main__":
    print( 'Seja bem vindo, usuário!')
    print(""" [TABELA DE OPERAÇÕES]        
          - Adição
          - Subtração 
          - Multiplicação 
          - Divisão 
         """)
    
    operacao = input('Digite a operação que deseja realizar:').upper()
    
    lchave = operacao[0]


    if lchave == "A":
        x = input("Digite um valor:")
        y = input("Digite outro valor: ") 
        resultado = somar(x,y)
        print(f"Seu resultado é {resultado}")
    
    elif lchave == "S":
        x = input("Digite um valor:")
        y = input("Digite outro valor: ") 
        resultado = subtracao(x,y)
        print(f"Seu resultado é {resultado}")

    elif lchave == "M":
        x = input("Digite um valor:")
        y = input("Digite outro valor: ") 
        resultado = multiplicar(x,y)
        print(f"Seu resultado é {resultado}")
    

    elif lchave == "D":
        x = input("Digite um valor:")
        y = input("Digite outro valor: ") 
        resultado = dividir(x,y)
        print(f"Seu resultado é {resultado}")
    
    else:
        print('Operação inexistente na tabela, FIM!')



    
           

     