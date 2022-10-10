import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from dotenv import load_dotenv

load_dotenv(verbose=True)  # Throws error if no .env file is found

servidor_smtp = os.getenv("SERVIDOR_SMTP")
login = os.getenv("LOGIN")
senha = os.getenv("SENHA")
remetente = os.getenv("REMETENTE")
destinatario = os.getenv("DESTINATARIO")

def envia_email(pontuacoes):
    message = MIMEMultipart("alternative")
    if datetime.now().hour < 12:
        message["Subject"] = "Seleção - " + str(datetime.now().day) + "/" + str(datetime.now().month) + " - Manhã"
    else:
        message["Subject"] = "Seleção - " + str(datetime.now().day) + "/" + str(datetime.now().month) + " - Noite"
    print(message["Subject"])
    message["From"] = remetente
    message["To"] = destinatario
    # parte em <text/plain>
    texto = """
    Oi, Laura! Aqui está a última seleção!"""
    # parte em <HTML>
    html = """
    <html>
      <body>"""
    if datetime.now().hour < 18:
        html += """
        <div style="background-color:#1DA1F2; color:#fff; padding:15px; margin-bottom: 15px; text-align:center; border-radius: 5px;">
            <h1>Bom dia, Laura!</h1><h2>&#128140; Aqui está a seleção desta manhã:</h2></div>"""
    else:
        html += """
        <div style="background-color:#243447; color:#fff; padding:15px; margin-bottom: 15px; text-align:center; border-radius: 5px;">
            <h1>Ooi, Laura!</h1><h2>&#128140; Aqui está a seleção desta noite:</h2></div>"""

    for i in range(0, len(pontuacoes), 1):
        html += """
        <a href="https://twitter.com/"""
        html += pontuacoes[i].usuarie.arroba
        html += """
        "><div style="background-color: #E1E8ED; border: 1px solid """
        if pontuacoes[i].indesejados is True:
            html += "#FF9494"
        else:
            html += "rgba(0, 0, 0, 0.05)"
        html += """; margin: 5px 0 10px 5px; border-radius: 50vh 10vh 10vh 50vh;"><div style="display:inline-block; vertical-align:middle; width: 100%;"><img src="
        """
        html += str(pontuacoes[i].usuarie.foto)
        html += """
        " width="36" height="36" style="display:inline-block; vertical-align:middle; margin:10px; border-radius: 50%"><div style="display:inline-block; vertical-align:middle;"><div style="color:black; font-size:14px; font-weight: bold; margin:0;">"""
        tam_max = 24
        html += pontuacoes[i].usuarie.nome[:tam_max]
        if len(pontuacoes[i].usuarie.nome) > tam_max:
            html += """<span style="color:#888;">...</span>"""
        html += """
        </div><div style="font-size:10px; color: #555;">@"""
        html += pontuacoes[i].usuarie.arroba
        html += """
        </div></div><div style="display:inline; float: right; padding: 5px 20px; color: #555;"><p>"""
        html += str(i + 1)
        html += """
        </p></div></div></div></a>"""
    html += """
        <p> Qualquer <strong>coisa</strong> me avise! se tem instagram botar junto</p>
      </body>
    </html>"""

    # convert both parts to MIMEText objects and add them to the MIMEMultipart message
    part1 = MIMEText(texto, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    # send your email
    with smtplib.SMTP(servidor_smtp, 587) as server:
        server.starttls()
        server.login(login, senha)
        server.sendmail(
            remetente, destinatario, message.as_string()
        )
    print('✔ Mandei o email')