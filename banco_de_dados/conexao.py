import sqlite3
from sqlite3 import Error

class Conexao:
    def get_conexao(self):
        caminho = '/home/limeira/Universidade/Disciplinas/TESI-I/2025/src-tesi-1-2025/banco_de_dados/banco_tesi1.db'
        try:
            con = sqlite3.connect(caminho)
            return con
        except Error as er:
            print(er)

# obj = Conexao()
# conexao = obj.get_conexao()
# if conexao:
#     sql = 'SELECT * FROM cliente;'
#     try:
#         cursor = conexao.cursor()
#         resultado = cursor.execute(sql).fetchall()
#         for item in resultado:
#             print(item[1])
#     except Error as er:
#         print(er)