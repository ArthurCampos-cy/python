from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def obter_temperatura_minima():
    driver = webdriver.Chrome()  # Usa chromedriver da mesma pasta

    try:
        driver.get("https://www.tempo.com/belo-horizonte.htm")
        time.sleep(5)

        elementos = driver.find_elements(By.CLASS_NAME, "dato-temperatura")

        if not elementos or len(elementos) < 2:
            raise Exception("Temperatura mínima não encontrada na página.")

        atributo = elementos[1].get_attribute("data-weather")
        temperatura = float(atributo.split("|")[0])
        return temperatura

    except Exception as e:
        print("Erro ao obter a temperatura:", e)
        return None

    finally:
        driver.quit()
