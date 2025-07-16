from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os
import time


def obter_temperatura_minima():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    chromedriver_name = "chromedriver.exe"
    chromedriver_path = os.path.join(current_dir, chromedriver_name)

    if not os.path.exists(chromedriver_path):
        print(f"Erro: ChromeDriver não encontrado em {chromedriver_path}")
        print("Por favor, baixe a versão correta do ChromeDriver para o seu Chrome e coloque-o nesta pasta.")
        print("Link para download: https://chromedriver.chromium.org/downloads")
        return None

    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service)

    temperatura_encontrada = None

    try:
        url = "https://www.google.com/search?q=temperatura+belo+horizonte"
        print(f"Navegando para: {url}")
        driver.get(url)

        time.sleep(3)

        wait = WebDriverWait(driver, 15)


        element_to_wait_for = wait.until(EC.presence_of_element_located((By.ID, "wob_tm")))
        print("Elemento 'wob_tm' encontrado com Selenium.")
        html_content = driver.page_source

        soup = BeautifulSoup(html_content, 'html.parser')

        temperatura_element = soup.find('span', id='wob_tm')

        if temperatura_element:
            temperatura_str = temperatura_element.get_text().strip()
            print(f"Texto da temperatura bruta encontrada com BeautifulSoup: '{temperatura_str}'")

            try:
                temperatura_encontrada = float(temperatura_str)
                print(f"Temperatura parseada com sucesso: {temperatura_encontrada}°C")
            except ValueError:
                print(f"Erro: Não foi possível converter '{temperatura_str}' para um número.")
        else:
            print("Erro: Elemento com id='wob_tm' não encontrado no HTML processado pelo BeautifulSoup.")

    except Exception as e:
        print(f"Ocorreu um erro ao obter a temperatura: {e}")

    finally:
        print("Fechando o navegador.")
        driver.quit()
        return temperatura_encontrada