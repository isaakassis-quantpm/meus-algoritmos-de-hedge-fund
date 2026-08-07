import time

print("💰 [SISTEMA]: Inicializando Simulador de Riqueza de Longo Prazo...")
time.sleep(1)

# Perguntas para o Diretor IsaaK configurar pelo teclado
dinheiro_inicial = float(input("Quanto o fundo vai investir hoje? CHF "))
taxa_rendimento = float(input("Qual a porcentagem de lucro por ano? (Ex: 10) ")) / 100
anos_investidos = int(input("Por quantos anos vamos deixar rendendo? "))

print("\n--- INICIANDO SIMULAÇÃO DA BOLA DE NEVE ---")
time.sleep(1)

# O comando 'for' vai calcular o rendimento ano por ano
for ano in range(1, anos_investidos + 1):
    # A mágica dos juros compostos acontece aqui:
    lucro_do_ano = dinheiro_inicial * taxa_rendimento
    dinheiro_inicial = dinheiro_inicial + lucro_do_ano
    
    print(f"📈 Ano {ano}: Seu saldo subiu para CHF {dinheiro_inicial:.2f}")
    time.sleep(0.5)

print("\n=============================================")
print(f"🎯 SIMULAÇÃO CONCLUÍDA, DIRETOR ISAAK!")
print(f"Sua fortuna final acumulada é de: CHF {dinheiro_inicial:.2f}")
print("=============================================")
