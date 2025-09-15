from .base import Personagem
from .enums import Raca


class Mago(Personagem):
    def __init__(self, raca, forca, destreza, constituicao, inteligencia, sabedoria, carisma):
        print("Foi criado a instância da classe Mago")
        super().__init__(raca, forca, destreza, constituicao, inteligencia, sabedoria, carisma)

    def clone(self):
        return Mago(
            self.raca, self.forca, self.destreza, self.constituicao,
            self.inteligencia, self.sabedoria, self.carisma
        )
