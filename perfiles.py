from io import open

class perfiles():
    def __init__(self):
        self.list_of_profiles = []
        self.nombres = ['---vacío---','---vacío---','---vacío---','---vacío---','---vacío---']
        self.ips = ['---vacío---','---vacío---','---vacío---','---vacío---','---vacío---']

    def gurdar(self,nombre_de_guardado,nombre,mensaje,h1,h2,filtro):
        perfiles = open("perfiles.txt","r")
        entrys = perfiles.readlines()

        ip = len(entrys)

        perfiles = open("perfiles.txt","a")
        perfiles.write(f"{ip}|{nombre_de_guardado};{nombre};{mensaje};{h1};{h2};{filtro}|\n")
        perfiles.close()

        self.inicio()

    def _cargar(self,ip):
        perfiles = open("perfiles.txt","r")
        entrys = perfiles.readlines()

        for i in entrys:
            if ip == i[0]:
                list_a = i.split("|")
                list_b = list_a[1].split(";")
                
                return list_b

        perfiles.close()

    def eliminar(self,ip):
        perfiles = open("perfiles.txt","r")
        entrys = perfiles.readlines()
        perfiles.close()

        perfiles = open("perfiles.txt","w+")
        for i in entrys:
            if ip == i[0]:
                entrys.remove(i)
                perfiles.seek(0)
                break
        
        string = ""
        b=0

        for line in entrys:
            list_of_line = line.split("|")
            string = f"{b}|{list_of_line[1]}|\n"
            
            perfiles.write(string)
            b += 1
        perfiles.close()

    def inicio(self):
        perfiles = open("perfiles.txt","r")
        entrys = perfiles.readlines()

        for a in range(0,len(entrys)):
            list_of_line = entrys[a].split("|")
            _entrys_ = list_of_line[1].split(";")

            self.nombres[a] = _entrys_[0]
            self.ips[a] = list_of_line[0]
        perfiles.close()
        