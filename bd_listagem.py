# Registra a data e horário de início da pesquisa, usa o id dê usuárie
def insere_listades_bd(pontuação, conexao_bd):
	cursor = conexao_bd.cursor()

	sql = "INSERT INTO listades (id_usuarie, listagem) VALUES (%s, NOW()) ON DUPLICATE KEY UPDATE listagem=NOW()"
	cursor.execute(sql, (pontuação.usuarie.id,))
	conexao_bd.commit()

	cursor.close()