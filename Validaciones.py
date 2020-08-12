from selenium.webdriver.common.by import By
from Time_Control import Time_Control
from Filtros import _filtro_

TC=Time_Control()

class validaciones():
    def main_validacion(self,msg_box,message,driver,ahora,hora_1,hora_2,filtro,tipo_filtro,_debug,CamelCase,exclucion_negativa):
        num = 0
        F = _filtro_(msg_box,driver,filtro,message,exclucion_negativa)

        while ahora < hora_2:

            TC.wait(2)
            ahora = TC.hora(horaParaConvertir=None)

            a = driver.find_elements_by_class_name('eRacY')
            b = a[-1].find_element(By.TAG_NAME, 'span')
            c = b.find_element(By.TAG_NAME, 'span')
            element = c.text

            num = num + 1
            print(f"( {element} ) buelta n*{num}")


            if _debug == True:
                if element == "EXIT":
                    break
                else:
                    if CamelCase == True:
                        if tipo_filtro == 1:
                            F.Validacion_Abdoluta_CamelCase(element)
                        else:
                            F.Validacion_Parcial_CamelCase(element)
                    else:
                        if tipo_filtro == 1:
                            F.validacion_Absoluta(element)  
                        else:
                            F.Validacion_Parcial(element)                 
            else:
                if CamelCase == True:
                    if tipo_filtro == 1:
                        _break = F.Validacion_Abdoluta_CamelCase(element)
                        if _break == True: break
                    else:
                        _break = F.Validacion_Parcial_CamelCase(element)
                        if _break == True: break
                else:
                    if tipo_filtro == 1:
                        _break = F.validacion_Absoluta(element)
                        if _break == True: break
                    else:
                        _break = F.Validacion_Parcial(element)
                        if _break == True: break

            

    def filtros(self,Palabra_Clave,CamelCase):
        if  CamelCase == True:
            filtro = Palabra_Clave
        else:
            filtro = [Palabra_Clave.upper(), Palabra_Clave.lower(), Palabra_Clave.capitalize()]

        return filtro

