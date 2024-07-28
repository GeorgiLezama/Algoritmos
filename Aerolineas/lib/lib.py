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
                j[i]["Pasajeros"] = p.toJson()
        file = open("Data/data.json","w")
        json.dump(j,file,ensure_ascii=False,indent=4)
        file.close()
        
