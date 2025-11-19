from app import app
from flask import render_template, request
from app.services.atributos_service import calcular_atributos
from flask import request, jsonify
from app.services.personagem_service import criar_personagem
import json
import os


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
        # Criar instância do objeto personagem
        personagem = criar_personagem(data['raca'], data['classe'], data['atributos'])
        
        # Converter o objeto para dicionário usando __dict__
        personagem_dict = personagem.__dict__.copy()
        
        # Converter enum para valor string para serialização JSON
        if hasattr(personagem_dict['raca'], 'value'):
            personagem_dict['raca'] = personagem_dict['raca'].value
        
        # Adicionar informações extras
        personagem_dict['classe'] = personagem.__class__.__name__
        
        # Definir o caminho do arquivo JSON
        arquivo_json = os.path.join(os.path.dirname(__file__), '..', 'personagem_salvo.json')
        
        # Salvar em arquivo JSON
        with open(arquivo_json, 'w', encoding='utf-8') as f:
            json.dump(personagem_dict, f, ensure_ascii=False, indent=2)
        
        info = personagem.mostrar_info()
        return jsonify({
            'message': f'Personagem salvo com sucesso no arquivo personagem_salvo.json!\n\n{info}',
            'arquivo': 'personagem_salvo.json',
            'dados_salvos': personagem_dict
        })
    
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Erro ao salvar arquivo: {str(e)}'}), 500

