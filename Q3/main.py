from models.cliente import Cliente
from models.produto import Produto

if __name__ == "__main__":
     

   cliente = Cliente("Carlos", "Rua João augusto","985.304.234.67" )
   cliente.save()

   produto = Produto("Sabao Omo", "8,00", "4365456")
   produto.save()
