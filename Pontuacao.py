from Usuarie import *

class Pontuacao:
    def __init__(self, usuarie:Usuarie, pontos=0, coerencia = 0, indesejados = False):
        self.usuarie = usuarie
        self.pontos = pontos
        self.coerencia = coerencia
        self.indesejados = indesejados

    def __lt__(self, other):
        eu = 2.0*self.pontos + self.coerencia
        if self.indesejados:
            eu -= 0.25
        outro = 2.0*other.pontos + other.coerencia
        if other.indesejados:
            outro -= 0.25
        return eu < outro