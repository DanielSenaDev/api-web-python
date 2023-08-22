from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask('api-bd')


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API-WEB"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

usuarios_db = []

@app.route("/", methods=["GET"])
def get():
    return jsonify(usuarios_db)

@app.route("/user/<int:cpf>", methods=["GET"])
def get_by_cpf(cpf):
    for user in usuarios_db:
        if(user['cpf'] == cpf):
            return jsonify(user)
    return jsonify({"message": "Usuario nao encontrado pelo CPF"}), 404

@app.route("/", methods=["POST"])
def post():
    req = request.json
    for users in usuarios_db:
        if(users['cpf'] == req['cpf']):
            return jsonify({"message": "CPF já existente. Não é possivel cadastrar novo usuario com mesmo CPF"}), 400
        
    usuarios_db.append(req)
    return jsonify({"message": "Cadastro realizado com SUCESSO"}), 200

app.run()