import time

print("⚡ [SISTEMA]: Inicializando Monitor de Ativos Digitais...")
time.sleep(1)

# Isto é um DICIONÁRIO. Ele guarda o nome e o preço real juntos!
precos_cripto = {
    "Bitcoin": 95000,
    "Ethereum": 3400,
    "Solana": 180
}

print("--- EXIBINDO PREÇOS EM TEMPO REAL ---")

# O comando .items() faz o robô ler a dupla (o nome e o preço) de uma vez só
for moeda, preco in precos_cripto.items():
    print(f"💰 Moeda: {moeda} | Preço Atual: CHF {preco}")
    time.sleep(0.5)

print("-" * 45)
# Você pode buscar o preço de uma moeda direto pelo nome dela!
busca = "Bitcoin"
print(f"🔍 Consulta rápida ativada para: {busca}")
print(f"O preço do {busca} na carteira é de: CHF {precos_cripto[busca]}")
