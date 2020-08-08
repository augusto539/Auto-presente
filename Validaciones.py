from selenium.webdriver.common.by import By
from Time_Control import Time_Control

TC=Time_Control()

class validaciones():
    def main_validacion(self,msg_box,message,driver,hora_1,hora_2,ahora,filtro):
        num = 0
        while ahora < hora_2:

            TC.wait(1)
            ahora = TC.hora(horaParaConvertir=None)

            a = driver.find_elements_by_class_name('eRacY')
            b = a[-1].find_element(By.TAG_NAME, 'span')
            c = b.find_element(By.TAG_NAME, 'span')
            element = c.text

            num = num + 1
            print(f"( {element} ) buelta n*{num}")

            #_break = self.validacion_Absoluta(element,msg_box,message,driver,filtro)
            #if _break == True: break


            _break = self.Validacion_Parcial(element,msg_box,message,driver,filtro)
            if _break == True: break


    def Validacion_Parcial(self,element,msg_box,message,driver,filtro):

        if element in filtro[0] or element in filtro[1] or element in filtro[2]:
            if "no" in element:
                return True
            else:
                msg_box.send_keys(message)
                button = driver.find_element_by_class_name('_1U1xa')
                button.click()
                return True

    def validacion_Absoluta(self,element,msg_box,message,driver,filtro):

        if element == filtro[0] or element == filtro[1] or element == filtro[2]:
                msg_box.send_keys(message)
                button = driver.find_element_by_class_name('_1U1xa')
                button.click()
                return True

    def filtros(self,Palabra_Clave):

        filtro = [Palabra_Clave.upper(), Palabra_Clave.lower(), Palabra_Clave.capitalize()]

        return filtro

