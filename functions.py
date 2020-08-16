from selenium import webdriver
from tkinter import messagebox
from Time_Control import Time_Control
from Validaciones import validaciones

TC = Time_Control()
val = validaciones()

class functions():
    def __init__(self):
        self.debug = False
        self._debug_ = 2

        self.CamelCase = False
        self._CamelCase_ = 2

        self.exn = False
        self._Negative_ = 2

    def send(self,name_box,message_box,hour_1_box,hour_2_box,filtro_box,T_filtro):
        self.name = name_box.get()
        self.message = message_box.get()
        _hora_1 = hour_1_box.get()
        _hora_2 = hour_2_box.get()
        self._filtro = filtro_box.get()
        self.tipo_filtro = T_filtro


        self.filtro = val.filtros(self._filtro,self.CamelCase)

        self.hora_1 = TC.hora(_hora_1)
        self.hora_2 = TC.hora(_hora_2)

        self.main()

    def main(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)

        driver.get('https://web.whatsapp.com/')

        messagebox.showinfo(message="do not click in accept until scan de QR code", title="Auto Presente")

        TC.wait(1)

        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(self.name))
        user.click()

        msg_box = driver.find_element_by_class_name('_3uMse')
        
        ahora = TC.hora(horaParaConvertir=None)
        
        TC.timer(self.hora_1,ahora)
        
        val.main_validacion(msg_box,self.message,driver,ahora,self.hora_1,self.hora_2,self.filtro,self.tipo_filtro,self.debug,self.CamelCase,self.exn)


    def _debug(self,debug):
        self.debug = debug.get()

        if self.debug == False:
            messagebox.showinfo(message="Debug mode disabled", title="Auto Presente")
        else:
            messagebox.showinfo(message="""Debug mode enabled. 
To exit send an "EXIT" message""", title="Auto Presente")

    def _CamelCase(self,CamelCase):
        self.CamelCase = CamelCase.get()

        if self.debug == False:
            messagebox.showinfo(message="CamelCase mode disabled", title="Auto Presente")
        else:
            messagebox.showinfo(message="CamelCase mode enabled.", title="Auto Presente")

    def _Negative(self,negativo):
        self.exn = negativo.get() 

        if self.debug == False:
            messagebox.showinfo(message="Negative mode disabled", title="Auto Presente")
        else:
            messagebox.showinfo(message="Negative mode enabled.", title="Auto Presente")


