import time

preco_atual = 40
preco_alvo_oportunidade = 60  # Você quer saber quando o Roblox subir muito!

print("--- SISTEMA DE ALERTA DE OPORTUNIDADES LIGADO ---")

while preco_atual < preco_alvo_oportunidade:
    print(f"Preço atual: CHF {preco_atual}. Nenhuma oportunidade ainda...")
    print("🔄 Robô aguardando o mercado se mover...")
    print("-" * 45)
    
    # Simula o preço do Roblox subindo de 5 em 5 francos
    preco_atual = preco_atual + 5
    
    time.sleep(2)  # Espera 2 segundos

# Quando o 'while' termina porque o preço subiu, o robô dispara o alerta!
print("🚨 🚨 🚨 ALERTA MÁXIMO, DIRETOR! 🚨 🚨 🚨")
print(f"O Roblox disparou e bateu CHF {preco_atual}!")
print("Abra os computadores do fundo! Hora de operar e faturar milhões!")
