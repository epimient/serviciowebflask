from flask import Flask, request, jsonify

app = Flask(__name__)


usuarios = []

@app.route('/')
def index():
    return "Bienvenido a la API de usuarios"

#Operación CREATE
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    nuevo_usuario = request.get_json()
    nuevo_usuario['id'] = len(usuarios) + 1
    usuarios.append(nuevo_usuario)
    return jsonify({"usuario": nuevo_usuario}), 201

#Operación READ
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify({"usuarios": usuarios})

@app.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    for usuario in usuarios:
        if usuario['id'] == id:
            return jsonify({"usuario": usuario})
    return jsonify({"error": "Usuario no encontrado"}), 404

#Operación UPDATE
@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    for usuario in usuarios:
        if usuario['id'] == id:
            nuevo_usuario = request.get_json()
            usuario.update(nuevo_usuario)
            return jsonify({"usuario": usuario})
    return jsonify({"error": "Usuario no encontrado"}), 404

#Operación DELETE
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):    
    for usuario in usuarios:
        if usuario['id'] == id:
            usuarios.remove(usuario)
            return jsonify({"mensaje": "Usuario eliminado"})
    return jsonify({"error": "Usuario no encontrado"}), 404


if __name__ == '__main__':
    app.run(debug=True)
