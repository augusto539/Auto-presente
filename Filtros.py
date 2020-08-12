from Time_Control import Time_Control

TC = Time_Control()


class _filtro_():
    def __init__(self,msg_box,driver,filtro,message,exclucion_negativa):
        self.msg_box = msg_box
        self.driver = driver
        self.F = filtro
        self.message = message
        self.ExN = exclucion_negativa


    def Validacion_Parcial(self,element):
        if self.F[0] in element or self.F[1] in element or self.F[2] in element:
            a = self.Exclucion_Negativa(element)
            return a

    def Validacion_Parcial_CamelCase(self,element):
        if self.F in element:
            a = self.Exclucion_Negativa(element)
            return a

    def Validacion_Abdoluta_CamelCase(self,element):
        if self.F == element:
            a = self.Exclucion_Negativa(element)
            return a

    def validacion_Absoluta(self,element):
        if self.F[0] == element or self.F[1] == element or self.F[2] == element:
            a = self.Exclucion_Negativa(element)
            return a

    


    

    def Exclucion_Negativa(self,element):
        if self.ExN == True:
            if "no" in element or "NO" in element or "No" in element:
                return True
            else:
                self.send_message(element)
                return True
        else:
            self.send_message(element)
            return True

    def send_message(self,element):
        self.msg_box.send_keys(self.message)
        TC.wait(1)
        button = self.driver.find_element_by_class_name('_1U1xa')
        button.click()
