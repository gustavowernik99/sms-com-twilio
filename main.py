import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC69de13a12daea5195e0677c1db6xxxxx"
# Your Auth Token from twilio.com/console
auth_token  = "ce22bccc40955b9085112c7xxxxxxxx"
client = Client(account_sid, auth_token)

# Passo a passo de solução

# Abrir os 6 arquivos em excel
lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    if (tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"].values[0]
        print(f"No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}")
        message = client.messages.create(
            to="+5561xxxxxxxxx",
            from_="xxxxxxxxxx",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)



# Para cada arquivo

# Verificar se algum arquivo na coluna Vendas daquele arquivo é maior do que 55k

# Se for maior do que 55k a gente envia um sms com Nome, o Mes e as vendas do vendedor


