"""
1. Pegar todos os links de aulas
    {'nome da aula': 'link da aula'}
2. Navegar até o exercício 3
    achar a url do exercício 3 e ir até lá
"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from pprint import pprint


browser = Firefox()

browser.get('https://selenium.dunossauro.live/aula_04.html')

def get_links(browser, elemento):
    """
    Pega todos os links dentro de um elemento
    
    - browser = a instancia do navegador 
    - element = webelement [aside, main, body, ul]

    """
    resultado = {}
    element = browser.find_element(By.TAG_NAME, elemento)
    ancoras = element.find_elements(By.TAG_NAME, 'a')
    for ancora in ancoras:
        resultado[ancora.text] = ancora.get_attribute('href')
        
    return resultado


"""
1. Pegar todos os links de aulas

"""
sleep(2)

aulas = get_links(browser, 'aside')
pprint(aulas)

    
"""
2. Navegar até o exercício 3

"""

exercicios = get_links(browser, 'main')

pprint(exercicios)

browser.get(exercicios['Exercício 3'])