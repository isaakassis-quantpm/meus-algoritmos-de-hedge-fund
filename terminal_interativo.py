import time

print("💻 [SISTEMA]: Inicializando Terminal Quant de Nova York...")
time.sleep(1)

# Loop infinito para manter o painel aberto na tela
while True:
    print("\n=============================================")
    print("      MENU DO DIRETOR ISAAK - HEDGE FUND     ")
    print("=============================================")
    print("1 - Simular Lucro da Carteira")
    print("2 - Mudar Alerta de Stop Loss")
    print("3 - Desligar Terminal e Ir Ver o Filme")
    print("=============================================")
    
    opcao = input("Diretor, escolha uma opção (1, 2 ou 3): ")
    
    if opcao == "1":
        print("\n📈 [PROCESSANDO]: Calculando lucros do Roblox...")
        time.sleep(1.5)
        print("💰 Resultado atual da carteira: + CHF 30.000.000!")
        
    elif opcao == "2":
        novo_stop = input("\n🚨 Digite o novo valor seguro para o Stop Loss: CHF ")
        print(f"🔒 [SUCESSO]: Trava de segurança atualizada para CHF {novo_stop}!")
        
    elif opcao == "3":
        print("\n🛑 Desligando computadores de Zurique...")
        print("Bônus salvos na nuvem. Até logo, Diretor IsaaK!")
        break  # Quebra o loop infinito e fecha o programa!
        
    else:
        print("\n❌ Opção inválida! Digite apenas 1, 2 ou 3.")
        
    print("\nRetornando ao menu principal...")
    time.sleep(2)
