import pandas as pd
from datetime import datetime


def salvar_em_planilha(cotacoes, temperatura):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")

    if temperatura is not None:
        praticar_natacao = "Sim" if temperatura >= 15 else "Não"
        temp_formatada = f"{temperatura:.1f}".replace(".", ",")
    else:
        praticar_natacao = "Temperatura Indisponível"
        temp_formatada = "N/A"

    df = pd.DataFrame([{
        "Data e Hora": agora,
        "USD-BRL": cotacoes["USD-BRL"],
        "EUR-BRL": cotacoes["EUR-BRL"],
        "BTC-BRL": cotacoes["BTC-BRL"],
        "Temperatura Mínima BH (°C)": temp_formatada,
        "Praticar Natação?": praticar_natacao
    }])

    df.to_excel("dados.xlsx", index=False)
    print("Dados salvos em dados.xlsx")