from datetime import datetime
import time

class Time_Control():

    def hora(self ,horaParaConvertir):
        if horaParaConvertir == None:
            current_time = datetime.strftime(datetime.now(),"%H:%M") #output: hora actual del pc
            current_time = datetime.strptime(current_time, "%H:%M")

            return current_time
        else:
            ahora = datetime.strptime(horaParaConvertir, "%H:%M")

            return ahora

    def timer(self,hora_1,ahora):
    
        while ahora < hora_1:
            resta = hora_1 - ahora
            print(f"esperando {resta} segundos")
            self.wait(resta.total_seconds())
            ahora = self.hora(horaParaConvertir=None)

    def wait(self,tiempo_segundos):
        time.sleep(tiempo_segundos)
