import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def enviar_email():
    remetente = "cyrakxo@gmail.com"
    senha = "abvn wjzx tqml frip"
    destinatario = "cyrakxo@gmail.com"

    msg = MIMEMultipart()
    msg["Subject"] = "Relatório Zeki"
    msg["From"] = remetente
    msg["To"] = destinatario

    with open("dados.xlsx", "rb") as f:
        parte = MIMEBase("application", "octet-stream")
        parte.set_payload(f.read())
        encoders.encode_base64(parte)
        parte.add_header("Content-Disposition", "attachment; filename=dados.xlsx")
        msg.attach(parte)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(remetente, senha)
        smtp.send_message(msg)
