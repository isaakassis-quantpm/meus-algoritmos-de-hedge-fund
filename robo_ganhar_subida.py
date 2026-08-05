# Código 3: Robô de Ganhar na Subida (Estratégia Long)
preco_compra = 50
preco_atual = 80  # O Roblox subiu muito por causa da Disney!
quantidade_acoes = 1000000

print("--- MONITORANDO ESTRATÉGIA DE ALTA (LONG) ---")

# Se o preço atual for maior que o preço de compra, o fundo ganhou dinheiro!
if preco_atual > preco_compra:
    lucro_liquido = (preco_atual - preco_compra) * quantidade_acoes
    print("O mercado subiu como prevíamos!")
    print("Executando venda no topo para realizar os ganhos...")
    print("Operação concluída! Lucro puro no caixa: CHF", lucro_liquido)
else:
    print("Preço abaixo do valor de compra. Robô aguardando recuperação...")
  
