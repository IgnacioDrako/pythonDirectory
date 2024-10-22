from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/api/lista1', methods=['GET'])
def obtener_lista1():
    datos = {
        "nombre": "Dummy",
        "Edad": "27",
        "residencia": "SomePlace"
        }
    return jsonify(datos)
@app.route('/api/lista2', methods=['GET'])
def obtener_lista2():
    lista_datos = [
        {"nombre": "Dummy", "edad": "27", "residencia": "SomePlace"},
        {"nombre":"Dummy0", "Edad": "27", "residencia": "SomePlace"},
        {"nombre":"Dummy1", "Edad": "27", "residencia": "SomePlace"}]
    return jsonify(lista_datos)
if __name__ =='__main__':
    app.run(debug=True)    