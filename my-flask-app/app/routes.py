from app import app
from flask import render_template, request
from app.services.atributos_service import calcular_atributos
from flask import request, jsonify
from app.services.personagem_service import criar_personagem


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/modo", methods=["POST"])
def modo():
    modo_escolhido = request.form.get("modo")
    atributos = calcular_atributos(modo_escolhido)
    return render_template(
        "distruibuicao_pontos.html",
        modo=modo_escolhido,
        atributos=atributos
    )

@app.route("/finalizar_personagem", methods=["POST"])
def finalizar_personagem():
    atributos = [request.form.get(f"atributo{i}") for i in range(6)]
    modo = request.form.get("modo")
    raca = request.form.get("raca")
    classe = request.form.get("classe")
    return render_template(
        "finalizar_personagem.html",
        atributos=atributos,
        modo=modo,
        raca=raca,
        classe=classe
    )

@app.route('/salvar_personagem', methods=['POST'])
def salvar_personagem():
    data = request.get_json()
    try:
        personagem = criar_personagem(data['raca'], data['classe'], data['atributos'])
        info = personagem.mostrar_info()
        return jsonify({'message': info})
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
