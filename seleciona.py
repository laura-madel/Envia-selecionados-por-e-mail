from Pontuacao import *

PONTOS_TRANS = 5.0
PONTOS_PRONOMES = 1.0
PONTOS_ARCO_IRIS = 1.0
PONTOS_ESTUDANTE = 1.5

QUANT_IDEAL_SEGUIDORES = 500
QUANT_IDEAL_SEGUIDES = 400

def seleciona(usuaries, quantidade):

    pontuacoes = []
    pontuacoes_aux = []
    interesses = [("⚧","trans","trava","travest",PONTOS_TRANS),
                  ("🌈",PONTOS_ARCO_IRIS),
                  ("ele","ela","elu","pronome",PONTOS_PRONOMES),
                  ("direito","⚖","UFPR","stud",PONTOS_ESTUDANTE)]

    for usuarie in usuaries:

        pontos = 0

        for interesse in interesses:
            i = 0
            achou_interesse = False
            while i < len(interesse) - 1:
                #TODO: RegEx Module
                #TODO: pesquisar no arroba também (no bd?)
                #FALHAS TODO
                # where all kinds of elemental powers
                # e, Transparente & Pure
                # see also @translatedcats
                if interesse[i] in usuarie.bio or interesse[i] in usuarie.nome or interesse[i] in usuarie.local:
                    achou_interesse = True
                i += 1
            if achou_interesse:
                pontos += interesse[-1]

        pontos_max = PONTOS_TRANS + PONTOS_PRONOMES + PONTOS_ARCO_IRIS + PONTOS_ESTUDANTE
        pontos = pontos/pontos_max

        coerencia = 0.0
        coerencia += verifica_proporcao_seguidores(usuarie.cont_seguides, usuarie.cont_seguidores)
        coerencia += verifica_quantidade_seguidores(usuarie.cont_seguidores)
        coerencia += verifica_quantidade_seguidos(usuarie.cont_seguides)
        coerencia = coerencia / 3

        indesejados = verifica_indesejados(usuarie)

        pontuacoes.append(Pontuacao(usuarie, pontos=pontos, coerencia=coerencia, indesejados=indesejados))
    usuaries.clear()
    pontuacoes.sort(reverse=True)
    for i in range(0, quantidade, 1):
        pontuacoes_aux.append(pontuacoes[i])
    del pontuacoes
    return pontuacoes_aux

def verifica_indesejados(usuarie):
    indesejados = ["porn",
                   "+18",
                   "NSFW",
                   "safad",
                   "tesao",
                   "pack",
                   "🔞",
                   "😈",
                   "🍆",
                   "🍑",
                   "卐",
                   "nazi",
                   "fandom",
                   "army",
                   "potter",
                   "otak",
                   "kpop",
                   "fandom",
                   "femboy",
                   " rad ",
                   "TERF",
                   "transmed",
                   "transcum",
                   "sex",
                   "only",
                   "📚",
                   "📖",
                   "book",
                   "otak",
                   "anime",
                   "game",
                   "play",
                   "🎮",
                   "jog"]

    for indesejado in indesejados:
        if indesejado in usuarie.bio or indesejado in usuarie.nome or indesejado in usuarie.local:
            return True
    return False

# Quanto maior esse índice maior a diferença entre seguidos e seguidores
def verifica_proporcao_seguidores(elu_segue : int, elu_eh_seguide : int):
    if elu_segue is not None and elu_eh_seguide is not None:
        diferença = abs(elu_segue - elu_eh_seguide)
        if diferença < 128:
            return 1.0
        return 128.0/diferença
    return 0.0

# pontua de 0 a 5
def verifica_quantidade_seguidores(elu_eh_seguide):
    if elu_eh_seguide is not None:
        diferença = abs(elu_eh_seguide - QUANT_IDEAL_SEGUIDORES)
        if diferença < 128:
            return 1.0
        return 128.0/diferença
    return 0

# Quanto maior mais longe do ideal
def verifica_quantidade_seguidos(elu_segue):
    if elu_segue is not None:
        diferença = abs(elu_segue - QUANT_IDEAL_SEGUIDES)
        if diferença < 128:
            return 1.0
        return 128.0/diferença
    return 0

# separar Direitos humanos / genero / nb / não binária/e/o
# nb em regesp!
# VEG
# Curitiba
