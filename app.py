from flask import Flask, jsonify, request
from base import db

app = Flask(__name__)

@app.route("/")
@app.route("/city/")
@app.route("/state/")
def index():
    return jsonify({"Mesaje":"Usted esta conectado al index","db":db})

@app.route("/city/<string:city>")
def buscarcity(city):
    ListaCiudades = []
    for ciudades in db:
        if ciudades["city"]==city:
            ListaCiudades.append(ciudades)
    if(len(ListaCiudades)>0):
        salida = ListaCiudades
        return jsonify({"Ciudad encontrada":salida})
    return jsonify({"Mensaje":"No encontramos tu solicitud"})

@app.route("/state/<string:state>")
def buscarstate(state):
    ListaEstados = []
    for states in db:
        if states["state"]==state:
            ListaEstados.append(states)
    if (len(ListaEstados)>0):
        salida = ListaEstados
        return jsonify({"Estados":salida})
    return jsonify({"Mensaje":"No encontramos su solicitud"})

@app.route("/addcity/", methods = ['POST'])
def add():
    new_city = {
    "state": request.json["state"],
    "city": request.json["city"],
    "longitud":request.json["longitud"],
    "latitude":request.json["latitude"]
    }
    db.append(new_city)
    return jsonify({"City Addes":new_city['city'],"Messege":"City Added Succesfally","City":db})

if __name__=='__main__':
    app.run(debug=True, port=4000)