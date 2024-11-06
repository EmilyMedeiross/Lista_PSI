
# Modelo classe - Cliente 
from database import get_connection

class Cliente:
    def __init__(self, nome:str, endereco:str, cpf:str):
        self.nome = nome 
        self.endereco = endereco
        self.cpf = cpf 

    def save(self):
        conn = get_connection()
        conn.execute("INSERT INTO clientes(nome, endereco, cpf) values(?,?,?)", (self.nome, self.endereco, self.cpf))
        conn.commit()
        conn.close()
        return True
    
    @classmethod
    def all(cls):
        conn = get_connection()
        clientes = conn.execute("SELECT * FROM clientes").fetchall()
        return clientes
    