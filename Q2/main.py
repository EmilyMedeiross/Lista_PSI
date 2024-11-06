from models.cliente import Cliente
from models.produto import Produto

if __name__ == "__main__":
    

    q1 = input("Nome do cliente:")
    q2 = input("Rua de seu domicilio:")
    q3 = input('CPF:')
    cliente = Cliente(q1,q2,q3)

    q4 = input("Nome do produto:")
    q5 = input("Preço:")
    q6 = input('Código:')
    produto = Produto(q4,q5,q6)
    
    print(cliente.__dict__)
    print(produto.__dict__)

#-----------------------------------------

cliente = Cliente("Carlos", "Rua João augusto","985.304.234.67" )
produto = Produto("Sabao Omo", "8,00", "4365456")

print(cliente.__dict__)
print (produto.__dict__)
