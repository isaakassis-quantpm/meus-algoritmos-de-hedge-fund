import time

# Defina a sua senha secreta de Diretor aqui (pode mudar se quiser)
senha_correta = "1234"

print("🔒 [SEGURANÇA]: Terminal de Zurique Bloqueado.")
print("Apenas o Diretor IsaaK pode acessar este sistema.")
print("-" * 50)

# O loop vai rodar enquanto a senha digitada estiver errada
while True:
    tentativa_senha = input("Digite a senha secreta de 4 dígitos: ")
    
    if tentativa_senha == senha_correta:
        print("\n🔓 [ACESSO PERMITIDO]: Identidade confirmada!")
        print("Bem-vindo de volta, Diretor IsaaK.")
        time.sleep(1)
        print("💰 Seus CHF 30.000.000 estão seguros e disponíveis.")
        break  # Abre o cofre e desliga o alarme de segurança!
    else:
        print("❌ [ACESSO NEGADO]: Senha incorreta! Sistema continua travado.")
        print("Tente novamente...\n")
        time.sleep(1)
