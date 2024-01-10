import smtplib
import email.message

def send_email():
    corpo_email = """
    <p>Olá João</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'joaovitorbastosborges@gmail.com'
    msg['To'] = 'joaovitorbastosborges@gmail.com'
    password = 'qiwchzwboszyakpc'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    try:
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('Email enviado')
    except Exception as e:
        print(f"Erro ao enviar o email: {e}")
    finally:
        s.quit()

# Chame a função
send_email()
