from .base import Personagem
from .enums import Raca


class Guerreiro(Personagem):
    def __init__(self, raca, forca, destreza, constituicao, inteligencia, sabedoria, carisma):
        print("Foi criado a instância da classe Guerreiro")
        super().__init__(raca, forca, destreza, constituicao, inteligencia, sabedoria, carisma)

    def clone(self):
        return Guerreiro(
            self.raca, self.forca, self.destreza, self.constituicao,
            self.inteligencia, self.sabedoria, self.carisma
        )
