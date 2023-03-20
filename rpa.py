from selenium.webdriver.chrome.options import Options # Para não ficar fechando
from selenium import webdriver as op_Selenium
from selenium.webdriver.common.by import By
import pyautogui as funcoesTeclado

from time import sleep


'''PARA NÂO FECHAR'''
options = Options()
options.add_experimental_option("detach", True)
'''FIM'''


# Preparando site
navegador = op_Selenium.Chrome(options=options)

navegador.get('https://www.magazineluiza.com.br')

# Pesquisando produto e digitando o nome do produto
navegador.find_element(By.ID, 'input-search').send_keys('S22')

# Esperando o carregamento
sleep(3)

# Press Enter para realizar a pesquisa
funcoesTeclado.press('enter')

# Esperando o carregamento
sleep(6)

listaProdutos = navegador.find_elements(By.CLASS_NAME, 'fwviCj')

for i in listaProdutos:

    nomeProduto = ''
    precoProduto = ''
    urlProduto = ''

    if nomeProduto == '':

        try:
            nomeProduto = i.find_element(By.CLASS_NAME, 'hQYVAI').text
        
        except Exception:
            pass

    elif nomeProduto == '':

        try:
             nomeProduto = i.find_element(By.CLASS_NAME, 'sc-hFVsQR').text

        except Exception:
            pass


    # Preço do produto
    # Class 1
    if precoProduto == '':

        try:
            precoProduto = i.find_element(By.CLASS_NAME, 'bQqJoc').text
        
        except Exception:
            pass

    # Class 2
    elif precoProduto == '':

        try:
            precoProduto = i.find_element(By.CLASS_NAME, 'sc-hGglLj').text

        except Exception:
            pass


    # Class 3
    elif precoProduto == '':

        try:
            precoProduto = i.find_element(By.CLASS_NAME, 'sc-hGglLj').text

        except Exception:
            pass

    
    # Class 4
    elif precoProduto == '':

        try:
            precoProduto = i.find_element(By.CLASS_NAME, 'jDmBNY').text

        except Exception:
            pass


    # Class 5
    elif precoProduto == '':

        try:
            precoProduto = i.find_element(By.CLASS_NAME, 'sc-kDvujY').text

        except Exception:
            pass


    else:
        precoProduto = '0'


    # URL Produto
    if urlProduto == '':

        try:
            urlProduto = i.find_element(By.TAG_NAME, 'a').get_attribute('href')
        
        except Exception:
            pass

    else:

        urlProduto = '-'


    print('=-'*35)
    print('PRODUTO: ', nomeProduto)
    print('PREÇO: ', precoProduto )
    print('LINK: ', urlProduto)
    print('=-'*35)

# Add comentário