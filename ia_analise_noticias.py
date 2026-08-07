import time

print("🤖 [IA SATELLITE]: Conectando ao robô de buscas da internet...")
time.sleep(1)

# Simulação de 3 anúncios que a IA encontrou navegando na internet hoje
anuncio_1 = "Roblox bate recorde de jogadores e fecha parceria gigante com a Disney!"
anuncio_2 = "Jogadores reclamam de bugs e servidores do Roblox ficam fora do ar."
anuncio_3 = "Diretoria do Roblox anuncia nova atualização secreta de Inteligência Artificial."

# O Diretor escolhe qual anúncio a IA deve ler e processar agora
print("=============================================")
print("1 - Ler Anúncio da Disney")
print("2 - Ler Anúncio dos Bugs")
print("3 - Ler Anúncio da Atualização de IA")
print("=============================================")
opcao = input("Diretor IsaaK, qual anúncio a IA deve analisar? ")

if opcao == "1":
    texto_analisado = anuncio_1
elif opcao == "2":
    texto_analisado = anuncio_2
else:
    texto_analisado = anuncio_3

print(f"\n🔍 [PROCESSANDO]: Analisando palavras-chave no texto...")
time.sleep(1.5)

# A IA varre o texto procurando palavras de alta performance ou de perigo
palavras_subida = ["parceria", "recorde", "disney", "sucesso", "ia", "inteligência"]
palavras_queda = ["bugs", "reclamam", "fora do ar", "prejuízo", "queda", "ruim"]

pontos_subida = sum(1 for palavra in palavras_subida if palavra in texto_analisado.lower())
pontos_queda = sum(1 for palavra in palavras_queda if palavra in texto_analisado.lower())

print("-" * 55)
print(f"Anúncio Lido: '{texto_analisado}'")
print("-" * 55)

# A Inteligência Artificial toma a decisão com base nos pontos das palavras
if pontos_subida > pontos_queda:
    print("📈 PREVISÃO DA IA: O preço vai SUBIR! (Tendência Altamente Positiva)")
    print("🛒 AÇÃO: Comprar 1.000.000 de ações imediatamente!")
elif pontos_queda > pontos_subida:
    print("📉 PREVISÃO DA IA: O preço vai CAIR! (Tendência Negativa Detectada)")
    print("🚨 AÇÃO: Executar Short (Apostar na queda) para faturar no prejuízo deles!")
else:
    print("📊 PREVISÃO DA IA: Mercado Estável. Sem movimentos fortes detectados.")
