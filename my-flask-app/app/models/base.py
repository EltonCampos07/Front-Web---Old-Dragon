from abc import ABC, abstractmethod
import copy

class PersonagemPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def mostrar_info(self):
        pass


class Personagem(PersonagemPrototype):
    def __init__(self, raca, forca, destreza, constituicao, inteligencia, sabedoria, carisma):
        self.raca = raca
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma

    def clone(self):
        return copy.deepcopy(self)

    def mostrar_info(self):
        info = (
            f"Classe: {self.__class__.__name__}, Raça: {self.raca.value} "
            f"Força: {self.forca}, Destreza: {self.destreza}, Constituição: {self.constituicao}, "
            f"Inteligência: {self.inteligencia}, Sabedoria: {self.sabedoria}, Carisma: {self.carisma}"
        )
        return info
