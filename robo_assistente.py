import time

print("🤖 [SISTEMA]: Inicializando inteligência artificial...")
time.sleep(1)

# O comando input() faz o computador esperar você digitar e apertar Enter!
nome_acao = input("Diretor, qual ação vamos operar hoje? ")
preco_desejado = int(input("Qual o preço máximo que aceita pagar? CHF "))

print("-" * 50)
print(f"🎯 CONFIGURAÇÃO SALVA: Operando {nome_acao}")
print(f"🔒 TRAVA OPERACIONAL: Monitorando teto de CHF {preco_desejado}")
print("-" * 50)

preco_mercado = preco_desejado - 5

# O robô faz a checagem com base no que você digitou
if preco_mercado < preco_desejado:
    print(f"📈 Sucesso! Preço real da {nome_acao} está em CHF {preco_mercado}.")
    print("Ordem executada dentro do limite do fundo. Lucro garantido!")
else:
    print("🚨 Alerta! Preço fora do limite operacional.")
