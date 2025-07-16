# main.py
from cotacoes import obter_cotacoes
from temperatura import obter_temperatura_minima
from Excel import salvar_em_planilha
from email_sender import enviar_email

def main():
    cotacoes = obter_cotacoes()
    temperatura = obter_temperatura_minima()
    salvar_em_planilha(cotacoes, temperatura)
    enviar_email()

if __name__ == "__main__":
    main()
