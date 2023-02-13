
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import warnings
warnings.filterwarnings('ignore')
import os
import shutil
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Fazendo o Web Crawling
def crawling():
    servico = Service(ChromeDriverManager().install())
    time.sleep(2)
    navegador = webdriver.Chrome(service=servico)
    time.sleep(2)
    navegador.get("https://www.bcb.gov.br/publicacoes/focus")
    time.sleep(2)
    navegador.find_element('xpath','/html/body/app-root/bcb-cookies/div/div/div/div/button[2]').click()
    time.sleep(2)
    navegador.find_element('xpath','//*[@id="publicacao"]/div[1]/div/div/div[2]/div[1]/div[2]/download/div/div/a').click()
    time.sleep(2)

# Mudando o arquivo da pasta download para o diretorio do script
def mudar_diretorio():
    fileDir = r"!!!-- COLOQUE SEU DIRETORIO DE DOWNLOAD --!!!"
    fileExt = r".pdf"
    arquivos = [_ for _ in os.listdir(fileDir) if _.endswith(fileExt)]
    source = f"!!!-- COLOQUE SEU DIRETORIO DE DOWNLOAD --!!!{arquivos[-1]}"
    destination = "!!! -- COLOQUE O LOCAL PARA ONDE VOCE QUER MOVER O PDF --!!!"
    mover = shutil.move(source,destination)

# Enviado o e-mail
def enviar_email():
    remetente = '!!! -- COLOQUE O EMAIL REMETENTE --!!!'
    senha_unica_gmail = '!! -- COLOQUE A SENHA UNCIA DO GMAIL --!!!'
    destinatario = '!!! -- COLOQUE O DESTINATARIO --!!!'

    # iniciando a mensagem
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = 'Relatório Boletim Focus'

    # criando corpo da mensagem
    body = 'Prezado gestor,\n\n\
    Segue em anexo o relatório com o as projeções ecônomicas do Boletim Focus.\n\n\
    Atenciosamente;\n\n\n\
    Felipe Nogueira dos Santos'
    msg.attach(MIMEText(body, 'plain'))

    # configurando anexo
    filename = 'Boletim Focus.pdf'
    attach = open('COLOQUE O LOCAL ONDE ESTA O ARQUIVO E O NOME DO ARQUIVO', 'rb')
    # Exemplo: "C:\\Users\\felipe\\Boletim.pdf

    # criando arquivo e setando o carregamento
    file = MIMEBase('application', 'octet-stream')
    file.set_payload((attach).read())

    # codificando com base64
    encoders.encode_base64(file)

    # corpo de anexo exigido pelo email
    file.add_header('Content-Disposition', f'attachment; filename={filename}')

    # coloando o anexo na mensagem
    msg.attach(file)

    # servidor SMTP
    data_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    # iniciando conexão segura via ttls
    data_smtp.starttls()

    # realizando login no email de envio
    data_smtp.login(remetente, senha_unica_gmail)

    # convertendo a mensagem para string
    message = msg.as_string()

    # enviando email
    data_smtp.sendmail(remetente, destinatario, message)
    data_smtp.quit()

