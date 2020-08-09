from selenium.webdriver.common.by import By
from Time_Control import Time_Control

TC=Time_Control()

class validaciones():
    def main_validacion(self,msg_box,message,driver,hora_1,hora_2,ahora,filtro,tipo_filtro,_debug):
        num = 0
        while ahora < hora_2:

            TC.wait(2)
            ahora = TC.hora(horaParaConvertir=None)

            a = driver.find_elements_by_class_name('eRacY')
            b = a[-1].find_element(By.TAG_NAME, 'span')
            c = b.find_element(By.TAG_NAME, 'span')
            element = c.text

            num = num + 1
            print(f"( {element} ) buelta n*{num}")

            if tipo_filtro == 1:
                _break = self.validacion_Absoluta(element,msg_box,message,driver,filtro,_debug)
                if _break == True: break
            else:
                _break = self.Validacion_Parcial(element,msg_box,message,driver,filtro,_debug)
                if _break == True: break



    def Validacion_Parcial(self,element,msg_box,message,driver,filtro,_debug):

        if filtro[0] in  element or filtro[1] in element or filtro[2] in element:
            if "no" in element:
                return self.debug(_debug,element)
            else:
                msg_box.send_keys(message)
                TC.wait(1)
                button = driver.find_element_by_class_name('_1U1xa')
                button.click()
                return self.debug(_debug,element)

    def validacion_Absoluta(self,element,msg_box,message,driver,filtro,_debug):

        if element == filtro[0] or element == filtro[1] or element == filtro[2]:
                msg_box.send_keys(message)
                TC.wait(1)
                button = driver.find_element_by_class_name('_1U1xa')
                button.click()
                return self.debug(_debug,element)

    def filtros(self,Palabra_Clave):

        filtro = [Palabra_Clave.upper(), Palabra_Clave.lower(), Palabra_Clave.capitalize()]

        return filtro

    def debug(self,_debug,element):
        if _debug == True:
            if element == "EXIT":
                return True
            else:
                return False
        else:
            return True

