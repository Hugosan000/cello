from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

# Conseguir utilizar o browser back e browser forward.

#função para pegar o elemento pelo texto
def find_by_text(browser, tag, text):
    """Encontrar o elemento com o texto 'text'.
        
    Argumentos:
       - browser = Instancia do browser [firefox,chrome, ...] 
       - text = conteúdo que deve estar na tag
       - tag = tag onde o texto será procurado   
    """
    elementos = browser.find_elements(By.TAG_NAME, tag) #lista
    
    for elemento in elementos:
         if elemento.text == text:
            return elemento

browser = Firefox()

browser.get('https://selenium.dunossauro.live/aula_04_b.html')

nome_das_caixas = ['um', 'dois', 'tres', 'quatro']

for nome in nome_das_caixas:
   find_by_text(browser, 'div', nome).click()
   
for nome in nome_das_caixas:
   sleep(1)
   browser.back()
   
for nome in nome_das_caixas:
   sleep(1)
   browser.forward()