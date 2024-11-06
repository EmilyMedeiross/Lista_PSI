
# Modelo classe - Produto 
from database import get_connection

class Produto:
    def __init__ (self, nome:str, preco:float, codigo:int):
        self.nome = nome 
        self.preco = preco
        self.codigo = codigo
    
    def save(self):
        conn = get_connection()
        conn.execute("INSERT INTO produtos(nome, preco, codigo) values(?,?,?)", (self.nome, self.preco, self.codigo))
        conn.commit()
        conn.close()
        return True

    @classmethod
    def all(cls):
        conn = get_connection()
        produtos = conn.execute("SELECT * FROM produtos").fetchall()
        return produtos