from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time 

def main(name,message,hour):
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get('https://web.whatsapp.com/')

    time.sleep(15)

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_3uMse')

    timer(hour)

    a = driver.find_elements_by_class_name('eRacY')

    comprobacion(a,msg_box,message,driver)


def timer(hour):
    hora_actual = datetime.now().time()
    hora = datetime.strptime(f"{hour}:00:00", "%X").time() 

    if hora_actual < hora:
        while hora_actual < hora:
            hora_actual = datetime.now().time()
            time.sleep(1800)


def comprobacion(a,msg_box,message,driver):
    for e in a:
        b = e.find_element(By.TAG_NAME, 'span')
        element = b.find_element(By.TAG_NAME, 'span')
        if "presente" in element.text or "Presente" in element.text:
            if "no" in element.text:
                break
            msg_box.send_keys(message)
            button = driver.find_element_by_class_name('_1U1xa')
            button.click()
            break