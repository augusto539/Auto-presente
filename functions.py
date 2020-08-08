from selenium import webdriver
from tkinter import messagebox
from Time_Control import Time_Control
from Validaciones import validaciones

TC = Time_Control()
val = validaciones()

def send(name_box,message_box,hour_1_box,hour_2_box,filtro_box):
    name = name_box.get()
    message = message_box.get()
    s_hora_1 = hour_1_box.get()
    s_hora_2 = hour_2_box.get()
    filtro = filtro_box.get()

    filtro = val.filtros(filtro)

    hora_1 = TC.hora(s_hora_1)
    hora_2 = TC.hora(s_hora_2)

    main(name,message,hora_1,hora_2,filtro)

def main(name,message,hora_1,hora_2,filtro):
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get('https://web.whatsapp.com/')

    messagebox.showinfo(message="do not click in accept until scan de QR code", title="Auto messenger")

    TC.wait(1)

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_3uMse')

    ahora = TC.hora(horaParaConvertir=None)

    TC.timer(hora_1,ahora)

    val.main_validacion(msg_box,message,driver,hora_1,hora_2,ahora,filtro)


