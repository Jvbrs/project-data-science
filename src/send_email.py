import smtplib
import email.message
from src.analysis_code import faturamento, quantidade, ticket_medio


def send_email(subject, from_address, to_address, password):
    corpo_email = f'''
    <p>Prezados,</p>
    
    <p>Segue o Relatório de Vendas por cada Loja</p>
    
    <p>Faturamento:</p>
    {faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}
    
    <p>Quatidade Vendida:</p>
    {quantidade.to_html()}
    
    <p>Ticket Médio dos Produtos em cada Loja:</p>
    {ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}
    
    <p>Qualquer dúvida estou à disposição</p>
    '''

    msg = email.message.Message()
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address
    password = password
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


