import socket

print("=" * 40)
print("      SCANNER DE PORTAS")
print("=" * 40)

# Pedir o IP
alvo = input("Digite o IP do alvo: ")

# Tentar descobrir o hostname
try:
    nome = socket.gethostbyaddr(alvo)
    print(f"Host encontrado: {nome[0]}")
except:
    print("Hostname não encontrado.")

# Portas comuns
portas = [21, 22, 23, 25, 80, 443, 8080]

abertas = []
fechadas = []

print("\nA escanear...")
print("-" * 40)

for porta in portas:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    resultado = s.connect_ex((alvo, porta))

    if resultado == 0:
        print(f"[+] Porta {porta}: ABERTA")
        abertas.append(porta)
    else:
        print(f"[-] Porta {porta}: FECHADA")
        fechadas.append(porta)

    s.close()

# Criar relatório
with open("relatorio.txt", "w") as ficheiro:
    ficheiro.write("RELATÓRIO DE SCAN\n")
    ficheiro.write("=" * 30 + "\n")
    ficheiro.write(f"Alvo: {alvo}\n\n")

    ficheiro.write("Portas abertas:\n")
    for porta in abertas:
        ficheiro.write(f"{porta}\n")

    ficheiro.write("\nPortas fechadas:\n")
    for porta in fechadas:
        ficheiro.write(f"{porta}\n")

print("\n" + "=" * 40)
print("SCAN CONCLUÍDO")
print(f"Portas abertas: {len(abertas)}")
print(f"Portas fechadas: {len(fechadas)}")
print("Relatório salvo em relatorio.txt")
print("=" * 40)
