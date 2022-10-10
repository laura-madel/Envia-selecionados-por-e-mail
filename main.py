from seleciona import *
from bd_baixa_usuaries import *
from make_contact import envia_email
from bd_listagem import *

if __name__ == '__main__':
    quantidade = 36

    conexao_bd = conectar_bd()
    pontuacoes = seleciona(baixa_usuaries_bd(conexao_bd), quantidade)
    envia_email(pontuacoes)
    for pontuação in pontuacoes:
        insere_listades_bd(pontuação, conexao_bd)
    del pontuacoes

    desconectar_bd(conexao_bd)
