import pandas as pd 

tabela_vendas = pd.read_excel('data/Vendas.xlsx')

pd.set_option('display.max_columns', None)
print(tabela_vendas)

faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)

quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()

print('-' * 50)

ticket_medio = (faturamento['Valor Final'] / quantidade ['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
print(ticket_medio)

