import json
import csv


with open("BD.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    
    lista_datos = []
    
    for row in reader:
        lista_datos.append({"state":row[0],"city":row[1],"longitud":row[2],"latitude":row[3]})
        
with open("BD.json","w") as f:
    json.dump(lista_datos,f,indent=4)