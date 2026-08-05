# Código 1: Robô de Proteção com Stop Loss
preco_compra = 50
preco_atual = 30  # O preço despencou no mercado!
quantidade_acoes = 1000000

# Trava de segurança automática
limite_stop_loss = 45

print("--- INICIANDO MONITORAMENTO DO ROBLOX ---")

if preco_atual <= limite_stop_loss:
    # O robô executa a trava sozinho aqui
    lucro_final = (limite_stop_loss - preco_compra) * quantidade_acoes
    print("ALERTA! O Roblox caiu demais e bateu no limite de:", limite_stop_loss)
    print("Executando trabalho automático para salvar o fundo...")
    print("Operação encerrada com sucesso!")
    print("Resultado final protegido: CHF", lucro_final)
else:
    lucro_final = (preco_atual - preco_compra) * quantidade_acoes
    print("Preço seguro. Robô continua monitorando o mercado...")
  
