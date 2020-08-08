from datetime import datetime
import time

class Time_Control():

    def hora(self ,horaParaConvertir):
        if horaParaConvertir == None:
            current_time = datetime.strftime(datetime.now(),"%H:%M:%S") #output: hora actual del pc

            ahora = current_time.split(':')

            if ahora[0] == "00":
                ahora[0] = "24"

            a = int(ahora[0] + ahora[1])

            return a
        else:
            hora = horaParaConvertir.split(':')
            b = int(hora[0] + hora[1])

            return b

    def timer(self,hora_1,ahora):
    
        while ahora < hora_1:
            print(ahora,hora_1)
            print("esperando...")
            self.wait(1800)
            ahora = self.hora(horaParaConvertir=None)

    def wait(self,tiempo_segundos):
        time.sleep(tiempo_segundos)
