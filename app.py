from flask import Flask, jsonify, request
from base import db

app = Flask(__name__)

#Rutas raiz
@app.route("/")
@app.route("/city/")
@app.route("/state/")
def index():
    return jsonify({"Mesaje":"Usted esta conectado al index","db":db})

#Ruta para busqueda de ciudades (city)
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

#Ruta para busquedas por estados (state)
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

#Ruta para ingresar una nueva ciudad
#En insomnia se requiere un JSON para el envio de datos
@app.route("/addcity/", methods = ['POST'])
def add():
    new_city = {
    "state": request.json["state"],
    "city": request.json["city"],
    "longitud":request.json["longitud"],
    "latitude":request.json["latitude"]
    }
    db.append(new_city)
    print(new_city)
    return jsonify({"City Addes":new_city['city'],"Messege":"City Added Succesfally","City":db})


#Ruta para la actualizacion de ciudad existente
#En insomnia se requiere un JSON para el envio de datos
@app.route("/editar/<string:city>", methods =['PUT'])
def editarCity(city):
    buscarCity = []
    for citys in db:
        if citys['city']==city:
            buscarCity.append(citys)
    if(len(buscarCity)>0):
        buscarCity[0]['state'] = request.json['state']
        buscarCity[0]['city'] = request.json['city']
        buscarCity[0]['longitud'] = request.json['longitud']
        buscarCity[0]['latitude'] = request.json['latitude']
        return jsonify({"Mensaje":"Ciudad actualizada","Dato":buscarCity[0]})
    return jsonify({"Mensaje":"No pudimos encontrar el producto"})


#Ruta para eleminar ciudad
@app.route("/eliminar/<string:city>", methods = ['DELETE'])
def eliminarCity(city):
    buscarCity = []
    for citys in db:
        if citys ["city"] == city:
            buscarCity.append(citys)
    if(len(buscarCity)>0):
        db.remove(buscarCity[0])
        return jsonify({"Ciudad eliminada":db})
    return jsonify({"ERROR":"El producto solicitado no se encuentra"})
            
    
        

if __name__=='__main__':
    app.run(debug=True, port=4000)