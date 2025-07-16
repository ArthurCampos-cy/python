import requests

def obter_cotacoes():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"
    response = requests.get(url)
    dados = response.json()

    cotacoes = {
        "USD-BRL": round(float(dados["USDBRL"]["bid"]), 2),
        "EUR-BRL": round(float(dados["EURBRL"]["bid"]), 2),
        "BTC-BRL": round(float(dados["BTCBRL"]["bid"]), 2)
    }
    return {k: f"{v:.2f}".replace(".", ",") for k, v in cotacoes.items()}
