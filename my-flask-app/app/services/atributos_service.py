import random


def rolar_dados(qtd_dados, lados, vezes, descartar_menor=False):
    resultados = []
    for _ in range(vezes):
        rolagem = [random.randint(1, lados) for _ in range(qtd_dados)]
        if descartar_menor:
            rolagem.remove(min(rolagem))
        resultados.append(sum(rolagem))
    return resultados


def calcular_atributos(modo):
    if modo == "classico":
        return rolar_dados(3, 6, 6)
    elif modo == "aventureiro":
        return sorted(rolar_dados(3, 6, 6), reverse=True)
    elif modo == "heroico":
        return sorted(rolar_dados(4, 6, 6, descartar_menor=True), reverse=True)
    else:
        return []
