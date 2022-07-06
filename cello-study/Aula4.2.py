from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium import webdriver

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

#função para pegar o elemento pelo link
def find_by_href(browser, link):
    """Encontrar o elemento 'a' com o link 'link'.
        
    Argumentos:
       - browser = Instancia do browser [firefox,chrome, ...] 
       - link = link que será procurado em todos as tags 'a'
    """
    elementos = browser.find_elements(By.TAG_NAME, 'a')
    
    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento

browser = Firefox()

browser.get('https://selenium.dunossauro.live/aula_04_a.html')

# Função para conseguir o texto DDG em uma List Itens de HTML com mais de um item.
elemento_ddg = find_by_text(browser, 'li', 'DuckDuckGo')

# Função para conseguir o link DDG em uma List Itens de HTML com mais de um link/item.
elemento_ddg = find_by_href(browser, 'ddg')
