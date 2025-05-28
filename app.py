from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []

@app.route('/')
def index():
    return jsonify({"mensaje": "BIENVENIDO A MI APP"})

@app.route('/usuarios', methods=["POST"])
def crear_usuarios():
    nuevo_usuario = request.get_json()
    nuevo_usuario['id'] = len(usuarios) + 1  # Corregido aquí
    usuarios.append(nuevo_usuario)
    return jsonify({"mensaje": "Usuario creado exitosamente", "usuario": nuevo_usuario}), 201

@app.route('/usuarios', methods=["GET"])
def obtener_usuarios():
    return jsonify({"usuarios": usuarios})

@app.route('/usuarios/<int:id>', methods=["GET"])
def obtener_usuario(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

@app.route('/usuarios/<int:id>', methods=["PUT"])    
def actualizar_usuario(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if usuario:
        datos = request.get_json()
        usuario.update(datos)
        return jsonify({"mensaje": "Usuario actualizado exitosamente", "usuario": usuario})
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

@app.route("/usuarios/<int:id>", methods=["DELETE"])
def eliminar_usuario(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if usuario:
        usuarios.remove(usuario)
        return jsonify({"mensaje": "Usuario eliminado exitosamente"})
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
