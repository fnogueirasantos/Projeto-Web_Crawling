
# Web Crawling e Automatização de Envio de E-mail - Boletim Focus

Projeto desenvolvido para automatização da captura do boletim focus no site do banco central do brasil e enviar por e-mail para o gestor solicitante.

Problema de negócio: O gestor da área de finanças deseja receber automaticamente toda segunda-feira o Boletim Focus mais atualizado por e-mail.


## Rodando localmente

Abra o terminal e acesse a pasta com os arquivos:

```bash
  cd home/crwaling
```

Instale os pacotes necessários:
```bash
  pip install selenium
  pip install time
  pip install webdriver-manager
  pip install PyMails
  pip install shutil
  pip install smtplib
```

Inicie o programa no terminal:

```bash
  python crawling.py
```




## Modificações Necessárias

Modificações necessárias para o script rodar localmente.

```python
    fileDir = r"COLOQUE O SEU CAMINHO DE DOWNLOAD"
    source = f"COLOQUE O SEU CAMINHO DE DOWNLOAD{arquivos[-1]}"
    destination = "COLOQUE O CAMINHO DA PASTA ONDE O SCRIPT FOI SALVO/Boletim.pdf"

    remetente = 'COLOQUE O E-MAIL DE REMETENTE'
    senha_unica_gmail = 'COLOQUE SUA SENHA ÚNICA DO GMAIL'
    destinatario = 'COLOQUE O E-MAIL DESTINATÁRIO'
    body = 'ALTERE O TEXTO DE EMAIL'

    attach = open('COLOQUE O CAMINHO DO ARQUIVO PDF COM O NOME DO ARQUIVO', 'rb')
```


