import yfinance as yf
import pyautogui
import pyperclip

ticker = input('Digite o código da ação')

dados = yf.Ticker(ticker)
tabela = dados.history("6mo")
fechamento = tabela['Close']

fechamento.plot()
cot_max = fechamento.max()
cot_min = fechamento.min()
cot_atual = fechamento[-1]
print(cot_max)
print(cot_min)
print(cot_atual)

print(f'Cotação máxima: R${cot_max}')
print(f'Cotação minima: R${cot_min}')
print(f'Cotação atual: R${cot_atual}')

destinatario = "giselehorii@gmail.com"
assunto = "Analise de cotas"


mensagem = f""" 
Prezado Gestor

Seguem as analises dos ultimos seis meses da ação {ticker}:

Cotação máxima: R$ {round(cot_max,2)}
Cotação minima: R$ {round(cot_min,2)}
cotação Atual: R$ {round(cot_atual,2)}

Qualquer dúvida, estou a disposção

Att.
"""

pyautogui.PAUSE = 2

pyautogui.hotkey("command", "t")
pyperclip.copy("www.exemplo.com")

pyautogui.hotkey("command", "t")
pyautogui.press("enter")

pyautogui.click(x=2034, y=210)

pyperclip.copy(destinatario)
pyautogui.hotkey("command", "t")
pyautogui.press("tab")

pyperclip.copy(assunto)
pyautogui.hotkey("command", "t")
pyautogui.press("tab")


pyperclip.copy(mensagem)
pyautogui.hotkey("command", "t")

pyperclip.click(x=3107, y=975)
pyautogui.hotkey("command", "f4")

print('Email enviado com sucesso!')


print('Análise gerada com Sucesso!')
