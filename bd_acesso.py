import os
import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv

load_dotenv(verbose=True)  # Throws error if no .env file is found

servidor = os.getenv("SERVIDOR")
usuarie = os.getenv("USUARIE")
senha = os.getenv("SENHA")
banco_de_dados = os.getenv("BANCO_DE_DADOS")

def conectar_bd():
	try:
		conexao_bd = mysql.connector.connect(host=servidor, user=usuarie, password=senha, database=banco_de_dados)
		print("Banco de dados conectado!")
	except mysql.connector.Error as error:
		if error.errno == errorcode.ER_BAD_DB_ERROR:
			print("Banco de Dados não existe!")
		elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Nome de suárie ou senha incorretes")
		else:
			print(error)
		return

	return conexao_bd

def desconectar_bd(conexao_bd):
	conexao_bd.commit()
	conexao_bd.close()
	print("Banco de dados desconectado!")