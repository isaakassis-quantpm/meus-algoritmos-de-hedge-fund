import time

print("📝 [SISTEMA]: Preparando impressora de relatórios de Zurique...")
time.sleep(1)

# Informações que vão para o documento oficial
nome_arquivo = "relatorio_mensal.txt"
lucro_obtido = "CHF 30.000.000,00"
status_fundo = "PROTEGIDO COM STOP LOSS"

print(f"✍️ Escrevendo dados no arquivo {nome_arquivo}...")

# O comando 'with open' cria o arquivo físico de texto sozinho!
with open(nome_arquivo, "w") as arquivo:
    arquivo.write("=============================================\n")
    arquivo.write("       RELATÓRIO OFICIAL DE PERFORMANCE      \n")
    arquivo.write("=============================================\n")
    arquivo.write(f"DIRETOR RESPONSÁVEL: ISAAK ASSIS\n")
    arquivo.write(f"LUCRO LÍQUIDO DO MÊS: {lucro_obtido}\n")
    arquivo.write(f"STATUS DO CAIXA: {status_fundo}\n")
    arquivo.write("=============================================\n")
    arquivo.write("Documento assinado digitalmente via satélite.\n")

time.sleep(1.5)
print("✅ [SUCESSO]: Arquivo gerado com sucesso!")
print(f"O documento '{nome_arquivo}' foi guardado na memória do sistema.")
