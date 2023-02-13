import time
from datetime import datetime
from operations import crawling, mudar_diretorio, enviar_email

hoje = datetime.today()
hoje = hoje.isoweekday()
# Condicional de segunda feira
if hoje == 1:
    crawling()
    time.sleep(2)
    mudar_diretorio()
    time.sleep(2)
    enviar_email()
    time.sleep(2)
    print('E-mail enviado com sucesso')
else:
    pass