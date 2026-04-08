import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sua_senha"
    database = "nexus_db"
)

cursor = conexao.cursor()

