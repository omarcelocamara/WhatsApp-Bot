from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://web.whatsapp.com/")
time.sleep(15)
#escanear o QR Code para entrar no WhatsApp Web
grupo1 = driver.find_element_by_xpath("//span[@title='NOME DO GRUPO1']")
grupo1.click()
time.sleep(2)
input = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")
input.send_keys("DIGITE A MENSAGEM QUE VOCÊ QUER ENVIAR")
input.send_keys(Keys.RETURN)
############################################################################
grupo2 = driver.find_element_by_xpath("//span[@title='NOME DO GRUPO2']")
grupo2.click()
time.sleep(2)
input = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")
input.send_keys("DIGITE A MENSAGEM QUE VOCÊ QUER ENVIAR")
input.send_keys(Keys.RETURN)

#Se tiverem mais grupos/ mais mensagens é só replicar esse mesmo código