# CÓDIGO DEFINITIVO: ROBÔ MESTRE QUANT PM
preco_compra_inicial = 50
preco_atual = 75  # Altere este número para testar os 3 cenários!
quantidade_inicial = 1000000

# Suas travas matemáticas automáticas
limite_stop_loss = 45
meta_take_profit = 80
gatilho_bola_de_neve = 65

print("--- SISTEMA CENTRAL QUANT PM ATIVADO ---")

# CENÁRIO 1: O mercado caiu demais (Stop Loss)
if preco_atual <= limite_stop_loss:
    lucro_final = (limite_stop_loss - preco_compra_inicial) * quantidade_inicial
    print("ALERTA! Stop Loss ativado em: CHF", limite_stop_loss)
    print("Prejuízo controlado com sucesso: CHF", lucro_final)

# CENÁRIO 2: O mercado bateu a nossa meta máxima (Take Profit)
elif preco_atual >= meta_take_profit:
    lucro_final = (meta_take_profit - preco_compra_inicial) * quantidade_inicial
    print("VITÓRIA! Meta máxima atingida em: CHF", meta_take_profit)
    print("Lucro embolsado e guardado no caixa: CHF", lucro_final)

# CENÁRIO 3: O mercado está subindo bem (Bola de Neve / Scaling In)
elif preco_atual >= gatilho_bola_de_neve:
    print("Tendência de alta confirmada! Ativando Bola de Neve...")
    quantidade_extra = 500000
    quantidade_total = quantidade_inicial + quantidade_extra
    lucro_turbinado = (preco_atual - preco_compra_inicial) * quantidade_total
    print("Novo lucro total acumulado: CHF", lucro_turbinado)

# CENÁRIO 4: Tudo está estável
else:
    lucro_normal = (preco_atual - preco_compra_inicial) * quantidade_inicial
    print("Mercado estável. Lucro atual: CHF", lucro_normal)
  
