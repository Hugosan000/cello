from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.common.by import By

browser = Firefox()
url = 'https://curso-python-selenium.netlify.app/aula_03.html'

browser.get(url)

sleep(1)

a = browser.find_element(By.ID, "ancora")


# print(f'texto de a: {a.text}')
# print(f'texto de p: {p.text}')

# Para poder achar mais de um elemento, so utilizar o find elements, e para achar apenas um elemento utilizar find element

for click in range(10):
    ps = browser.find_elements(By.TAG_NAME, "p")
    a.click
    print(f'Valor do ultimo p: {ps[-1].text}, valor do click: {click}')

    print(f'Os valores são iguais {ps[-1].text == str(click)}')
# Para que esse texto de certo, de conferir se os numeros estao iguais, é necessário transformar o valor em uma string, para conferir se a string = string.



browser.quit()

