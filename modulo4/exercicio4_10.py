import mysql.connector 
bd = mysql.connector.connect( 
    host="localhost", 
    user="root", 
    password=""
) 
bd_cursor = bd.cursor()
bd_cursor.execute("CREATE DATABASE empregados")
bd_cursor.execute("USE empregados")
bd_cursor.execute("CREATE TABLE alunos \
    (id INT AUTO_INCREMENT PRIMARY KEY, \
    nome VARCHAR(255), \
    endereco VARCHAR(255))") 