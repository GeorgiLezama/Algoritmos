import json
class lib:
    def agregar_vuelo(self,v):
        file = open("Data/data.json","r")
        j = json.load(file)
        j = j+[v.toJson()]
        file = open("Data/data.json","w")
        json.dump(j,file,ensure_ascii=False,indent=4)
        file.close()

    def registrar_pasajeros(self,p,v):
        file = open("Data/data.json","r")
        j = json.load(file)
        for i in range(0,len(j)):
            if j[i]["Id"] == v.id:
                if "Pasajeros" not in j[i]:
                    j[i]["Pasajeros"] = []
                j[i]["Pasajeros"].append(p.toJson())
        file = open("Data/data.json","w")
        json.dump(j,file,ensure_ascii=False,indent=4)
        file.close()

# Tope de la pila en N
    def registrar_carga(self,c,v):
        file = open("Data/data.json","r")
        j = json.load(file)
        for i in range(0,len(j)):
            if j[i]["Id"] == v.id:
                if "Carga" not in j[i]:
                    j[i]["Carga"] = []
                j[i]["Carga"].append(c.toJson())
        file = open("Data/data.json","w")
        json.dump(j,file,ensure_ascii=False,indent=4)
        file.close()

    def descargar_en_carga(self,v):
        file = open("Data/data.json","r")
        j = json.load(file)
        for i in range(0,len(j)):
            if j[i]["Id"] == v.id:
                j[i]["Carga"] = j[i]["Carga"][:-1]
        file = open("Data/data.json","w")
        json.dump(j,file,ensure_ascii=False,indent=4)
        file.close()

