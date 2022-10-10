from Usuarie import *
from bd_acesso import *

# TODO: Continuar testes no BD
# TODO: Falhas: pronomes depois de pular linha; n-b, b/b
# TODO: fracionar função
def escreve_sql_select_usuaries(variaveis, interesses, proibidos, pronomes):

	interesses_aux = []
	proibidos_aux = []
	pronomes_aux = []

	sql = "SELECT " + ', '.join(variaveis) + " FROM usuaries WHERE id NOT IN (SELECT id_usuarie FROM listades) AND eu_sigo LIKE FALSE AND me_segue LIKE FALSE"

	if proibidos:
		sql += " AND "
		for proibido in proibidos:
			proibidos_aux.append("nome NOT LIKE '%" + proibido + "%' AND bio NOT LIKE '%" + proibido + "%'")

		sql += ' AND '.join(proibidos_aux)

	sql += " AND ("

	for interesse in interesses:
		interesses_aux.append("nome LIKE '%" + interesse + "%' OR bio LIKE '%" + interesse + "%'")

	sql += ' OR '.join(interesses_aux)

	if pronomes:
		for pronome in pronomes:
			pronomes_aux.append("bio REGEXP '[0-9🏳️‍⚧️\
 °:(){}&.,?!''/|<>-]" + pronome + "' OR bio REGEXP '^" + pronome + "' OR nome REGEXP '[0-9🏳️‍⚧️\
 °:(){}&.,?!''/|<>-]" + pronome + "'")
		sql += " OR " + ' OR '.join(pronomes_aux)

	sql += ");"

	# Limpa, limpa, limpa
	variaveis.clear()
	proibidos.clear()
	interesses.clear()
	pronomes.clear()
	proibidos_aux.clear()
	interesses_aux.clear()
	pronomes_aux.clear()

	print(sql)
	return sql

def baixa_usuaries_bd(conexao_bd):
	cursor = conexao_bd.cursor()
	usuaries : Usuarie = []

	variaveis = ["id", "nome", "bio", "arroba", "foto", "local", "cont_seguides", "cont_seguidores"]
	interesses = ["🌈", "⚧", "gênero", "pronome", "UFPR", "trans", "travest", "trava", "ativis", "LGBT"]
	pronomes = ["ela", "ele", "elu"]
	proibidos = []

	cursor.execute(escreve_sql_select_usuaries(variaveis, interesses, proibidos, pronomes))

	resultado = cursor.fetchall()

	for usuarie in resultado:
		usuaries.append(Usuarie(id=usuarie[0],
								nome=usuarie[1],
								bio=usuarie[2],
								arroba=usuarie[3],
								foto=usuarie[4],
								local=usuarie[5],
								cont_seguides=usuarie[6],
								cont_seguidores=usuarie[7]))

	cursor.close()

	return usuaries