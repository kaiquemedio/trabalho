
import smtplib

try:
    msgFrom = str(input("Informe o e-mail de origem: "))
    password = 't s c s g g n s j h d w d a bu'
    msgTo = str(input("Informe o e-mail de destino: "))
    
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    
    smtpObj.login(msgFrom, password)
    
    msg = '''Subject: Titulo do email

Hello lucas
    '''
    smtpObj.sendmail(msgFrom, msgTo, msg)
    smtpObj.quit()
    print("Email enviado com sucesso!")
except smtplib.SMTPException as e:
    print(f"Erro ao enviar e-mail: {e}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

