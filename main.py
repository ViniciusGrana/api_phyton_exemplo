from flask import Flask, jsonify, make_response, request
from bd import Carros

app = Flask('carros')


#PRIMEIRO METODO: VISUALIZAR DADOS (GET)
#app.route  -> é para definir a rota para que o flask entanda que aquilo é um metodo que deve ser executado
@app.route('/carros', methods = ['GET'])
def get_carros():
    return Carros

#PRIMEIRO METODO PARTE 2 - VISUALIZAR DADOS POR ID (GET/ID)
@app.route("/carros/<int:id>", methods =['GET'])
def get_carros_id(id):
    for carros in Carros:
        if carros.get("id") == id:
            return jsonify(carros)

#SEGUNDO MÉTODO - CRIAR NOVOS DADOS (POST)
@app.route("/carros", methods =["POST"])
def criar_carros():
    carros=request.json
    Carros.append(carros)
    return make_response(
        jsonify(mensagem ='Carro cadastrado com sucesso',
                carros = carros)
    )

#TERCEIRO METODO - EDITAR DADOS (PUT)
@app.route('/carros/<int:id>', methods("PUT"))
def editar_carro_id(id):
    carro_alterado = request.get_json()
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            Carros[indice].update(carro_alterado)
            return jsonify(Carros[indice])

#QUARTO METODO - DELETAR OS DADOS (DELETE)
@app.route('/carros/<int:id>', methods =["DELETE"])
def excluir_carro(id):
    for indice, carro in enumerate(Carros):
        if carro.get("id") == id:
            del Carros[indice]
            return jsonify({"Mensagem:": "Carro excluido com sucesso"})

app.run(port=5000, host="localhost")