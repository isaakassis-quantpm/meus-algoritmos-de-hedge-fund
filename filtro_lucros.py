import time

print("🎯 [SISTEMA]: Inicializando Varredura de Mercado de Elite...")
time.sleep(1)

# Uma lista com os resultados de várias operações do fundo (valores em milhões de francos)
# Números positivos são lucros, números negativos são perdas!
resultados_do_dia = [30, -5, 12, -4, 50, -2, 85, -15]

print("📊 Analisando todas as operações abertas em Zurique...")
time.sleep(1)

# Esta linha mágica filtra a lista inteira e só deixa os números maiores que 0!
apenas_lucros = [lucro for lucro in resultados_do_dia if lucro > 0]

print("=" * 55)
print("💰 [RELATÓRIO DE VITÓRIAS]:")
print(f"Todas as operações encontradas: {resultados_do_dia}")
print(f"Ações com LUCRO PURO extraídas pela IA: {apenas_lucros}")
print("=" * 55)

# Faz a soma automática de todos os lucros filtrados
lucro_total = sum(apenas_lucros)
print(f"💵 Faturamento total das ações vencedoras: CHF {lucro_total} MILHÕES!")
