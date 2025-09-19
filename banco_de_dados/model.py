from sqlite3 import Error
import conexao

class Model:
    def __init__(self):
        self.con = conexao.Conexao()

    def get(self, sql):
        #sql = "SELECT * FROM cliente;"
        try:
            con = self.con.get_conexao()
            cursor = con.cursor()
            result = cursor.execute(sql).fetchall()
            con.close()
            return result
        except Error as er:
            print(er)

    def insert(self, sql):
        #sql = "INSERT INTO cliente (nome, cpf, email) VALUES ('TESTE',
        # '00000000000', 'teste@ufac.br');"
        try:
            con = self.con.get_conexao()
            cursor = con.cursor()
            cursor.execute(sql)
            if cursor.rowcount == 1: #Quantidade de linhas afetadas
                con.commit()
            con.close()
        except Error as er:
            print(er)

model = Model()
sql = "SELECT * FROM cliente;"
for i in model.get(sql):
    print(i)