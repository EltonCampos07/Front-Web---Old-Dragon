
from app.models.enums import Raca
from app.models.mago import Mago
from app.models.ladrao import Ladrao
from app.models.guerreiro import Guerreiro


def criar_personagem(raca_str, classe_str, atributos):
    try:
        raca = Raca[raca_str.upper()]
    except KeyError:
        raise ValueError("Raça inválida!")

    classe = classe_str.lower()
    atributos = list(map(int, atributos))

    if classe == 'mago':
        personagem = Mago(raca, *atributos)
    elif classe == 'ladrao':
        personagem = Ladrao(raca, *atributos)
    elif classe == 'guerreiro':
        personagem = Guerreiro(raca, *atributos)
    else:
        raise ValueError("Classe inválida!")

    return personagem
