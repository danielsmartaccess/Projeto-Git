# importar a base de dados
import pandas as pd
import win32com.client as win32
import os

# Verificar se o arquivo existe
arquivo_excel = 'Vendas.xlsx'
if not os.path.exists(arquivo_excel):
    raise FileNotFoundError(f"O arquivo {arquivo_excel} não foi encontrado!")

try:
    tabela_de_vendas = pd.read_excel(arquivo_excel)

    #visualizar a base de dados
    pd.set_option('display.max_columns', None)


    #faturamento por loja
    faturamento = tabela_de_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()


    #quantidade vendida por loja
    quantidade = tabela_de_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()


    # Tikect médio por produto em cada loja
    ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()


    # enviar email para as lojas

    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'danielsteinbruch@gmail.com'
    mail.Subject = 'Teste Python Outlook'
    mail.HTMLBody = '''
Prezado,

Segue o relatório de vendas por loja:

Faturamento por loja:
{}

Quantidade vendida por loja:
{}

Ticket médio por loja:
{}

Atenciosamente,
Sistema de Relatórios
'''.format(faturamento.to_html(), quantidade.to_html(), ticket_medio.to_html())
    mail.Send()
except Exception as e:
    print(f"Ocorreu um erro: {e}")