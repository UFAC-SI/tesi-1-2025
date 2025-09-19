from sqlite3 import Error
import conexao

class Model:
    def __init__(self):
        self.con = conexao.Conexao()

    def get(self, sql):
        try:
            con = self.con.get_conexao()
            cursor = con.cursor()
            result = cursor.execute(sql).fetchall()
            con.close()
            return result
        except Error as er:
            print(er)

    def insert(self, sql):
        try:
            con = self.con.get_conexao()
            cursor = con.cursor()
            cursor.execute(sql)
            if cursor.rowcount == 1: #Quantidade de linhas afetadas
                con.commit()
            con.close()
            return cursor.rowcount
        except Error as er:
            print(er)

    def delete(self, sql):
        try:
            con = self.con.get_conexao()
            cursor = con.cursor()
            cursor.execute(sql)
            if cursor.rowcount == 1:
                con.commit()
            con.close()
            return cursor.rowcount
        except Error as er:
            print(er)

# model = Model()
# sql = "SELECT * FROM cliente;"
# for i in model.get(sql):
#     print(i)