from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)


usuarios = []

# Página HTML para mostrar los usuarios
@app.route('/')
def index():
    plantilla_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Usuarios</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
            h1 { color: #333; }
            h2 { color: #333; }
            .container { max-width: 800px; margin: auto; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Bienvenidos a la API</h1>
            <h2>Lista de Usuarios</h2>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nombre</th>
                        <th>Correo</th>
                    </tr>
                </thead>
                <tbody>
                    {% for usuario in usuarios %}
                    <tr>
                        <td>{{ usuario.id }}</td>
                        <td>{{ usuario.nombre }}</td>
                        <td>{{ usuario.email }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </body>
    </html>
    """
    return render_template_string(plantilla_html, usuarios=usuarios)

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
