from .base import Personagem
from .enums import Raca


class Ladrao(Personagem):
    def __init__(self, raca, forca, destreza, constituicao, inteligencia, sabedoria, carisma):
        print("Foi criado a instância da classe Ladrao")
        super().__init__(raca, forca, destreza, constituicao, inteligencia, sabedoria, carisma)

    def clone(self):
        return Ladrao(
            self.raca, self.forca, self.destreza, self.constituicao,
            self.inteligencia, self.sabedoria, self.carisma
        )
