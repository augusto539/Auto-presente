from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time 

def hora_actual():
    current_time = datetime.strftime(datetime.now(),"%H:%M:%S") #output: hora actual del pc

    ahora = current_time.split(':')
    a = int(ahora[0] + ahora[1])

    return a
def HORA_1(s_hora_1):
    mytime = s_hora_1

    hora = mytime.split(':')
    b = int(hora[0] + hora[1])

    return b
def HORA_2(s_hora_2):
    mytime = s_hora_2

    hora = mytime.split(':')
    b = int(hora[0] + hora[1])

    return b



def send(name_box,message_box,hour_1_box,hour_2_box):
    name = name_box.get()
    message = message_box.get()
    s_hora_1 = hour_1_box.get()
    s_hora_2 = hour_2_box.get()

    hora_1 = HORA_1(s_hora_1)
    hora_2 = HORA_2(s_hora_2)

    main(name,message,hora_1,hora_2)

def main(name,message,hora_1,hora_2):
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get('https://web.whatsapp.com/')

    time.sleep(15)

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_3uMse')

    ahora = hora_actual()

    timer(hora_1,ahora)

    validacion(msg_box,message,driver,hora_1,hora_2,ahora)


def timer(hora_1,ahora):
    
    while ahora < hora_1:
        time.sleep(1800)
        ahora = hora_actual()
        
def validacion(msg_box,message,driver,hora_1,hora_2,ahora):
    num = 0
    while ahora < hora_2:
        time.sleep(1)
        ahora = hora_actual()

        a = driver.find_elements_by_class_name('eRacY')
        b = a[-1].find_element(By.TAG_NAME, 'span')
        c = b.find_element(By.TAG_NAME, 'span')
        element = c.text

        num = num + 1

        print(f"( {element} ) buelta n*{num}")

        if "presente" in element or "Presente" in element or "PRESENTE":
            if "no" in element:
                break
            msg_box.send_keys(message)
            button = driver.find_element_by_class_name('_1U1xa')
            button.click()
            #break

        #time.sleep(180)

