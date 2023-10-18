# Projeto 1 - Automação de tarefas

import pyautogui #para instalar o pyautogui: pip install autogui (no prompt de comando)
import time

# pyautogui.click -> clicar com o mouse
# pyatogui.write -> escrever um texto
# pyautogui.press -> apertar um tecla
# pyautogui.hotkey -> atalho (combinação de teclas)

# Passo a passo do projeto:
  # 1. Entrar no sistema da empresa

pyautogui.PAUSE = 1.0
#  - Abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")  
time.sleep(5)
pyautogui.click(x=493, y=463, clicks = 1)

#  - Entrar no link
link = ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.write(link)
pyautogui.press("enter")

#  - Esperar o site carregar
time.sleep(5)

  # 2. Fazer login
pyautogui.click(x=557, y=365, clicks = 1)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") #passar para o campo de senha
pyautogui.write("suasenhaaqui")
pyautogui.press("tab") #passar para o botão de login
pyautogui.press("enter")
time.sleep(3)

  # 3. Importar a base de dados de produtos
import pandas # para instalar pandas: pip install pandas numpy openpyxl

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index: # Para cada linha da minha tabela, executar os comandos abaixo.

    # 4. Cadastrar 1 produto
  pyautogui.click(x=496, y=249)
   
  codigo = tabela.loc[linha, "codigo"]
  marca = tabela.loc[linha, "marca"]
  tipo = tabela.loc[linha, "tipo"]
  categoria = tabela.loc[linha, "categoria"]
  preco = tabela.loc[linha, "preco_unitario"]
  custo = tabela.loc[linha, "custo"]
  
  
    # - Preencher os campos
  pyautogui.write(str(codigo)) # pode vim direto pro código : tabela.loc[linha, "codigo"]
  pyautogui.press("tab")
  pyautogui.write(str(marca))
  pyautogui.press("tab")
  pyautogui.write(str(tipo))  
  pyautogui.press("tab")
  pyautogui.write(str(categoria))
  pyautogui.press("tab")
  pyautogui.write(str(preco))
  pyautogui.press("tab")
  pyautogui.write(str(custo))
  pyautogui.press("tab")

  obs = tabela.loc[linha, "obs"]
  if not pandas.isna(obs): # Se o pandas.isna(obs) não for vazio, executar código abaixo
   pyautogui.write(str(obs))

  # - Apertar para enviar
  pyautogui.press("tab")
  pyautogui.press("enter")

  pyautogui.scroll(50000) #scroll positvo = rola pra cima. negativo = rola pra baixo

  # 5. Repetir o cadastro para todos os produtos



