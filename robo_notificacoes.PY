import time

# Dados do Diretor
nome_diretor = "IsaaK"
numero_celular = "+55 (48) 99999-9999"  # Simulando seu celular de Santa Catarina

preco_atual = 52
limite_stop_loss = 45

print("📱 CONFIGURANDO SISTEMA DE NOTIFICAÇÕES VIA SATELLITE 📱")
time.sleep(1)

while preco_atual > limite_stop_loss:
    # O robô cria o texto da mensagem sozinho juntando as informações!
    mensagem = f"CHEFÃO {nome_diretor.upper()}: O preço do Roblox está em CHF {preco_atual}. Tudo seguro na Suíça!"
    
    print(f"✉️ Enviando para {numero_celular}...")
    print(f"[NOTIFICAÇÃO]: {mensagem}")
    print("-" * 55)
    
    # Preço caindo de 2 em 2 francos
    preco_atual = preco_atual - 2
    time.sleep(2)

# Se sair do loop é porque bateu no limite de perda!
mensagem_urgente = f"🚨 ALERTA MÁXIMO, DIRETOR {nome_diretor.upper()}! O preço desabou para CHF {preco_atual}! Stop Loss acionado automaticamente. Seu bônus está protegido!"

print(f"💥 ENVIANDO MENSAGEM DE EMERGÊNCIA PARA {numero_celular}...")
print(f"[WHATSAPP URGENTE]: {mensagem_urgente}")
