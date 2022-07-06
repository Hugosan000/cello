from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By




browser = Firefox()

browser.get('https://selenium.dunossauro.live/aula_04_a.html')

lista_n_ordenada = browser.find_element(By.TAG_NAME, "ul")

lis = lista_n_ordenada.find_elements(By.TAG_NAME, "li")

browser.quit()




# LI > browser.find_element_by_id('li')
# A > browser.find_element_by_id('a')
# Atributos
# HREF, TEXT > >>> elemento.text
            #  >>> elemento.get_atribute('href')