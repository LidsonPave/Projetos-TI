import socket

# Agora o utilizador digita o IP que quer escanear
alvo = input("Digite o IP do alvo (ex: 192.168.1.1): ")

# Lista expandida com as portas mais comuns em auditorias de TI
portas = [21, 22, 23, 25, 80, 443, 8080]

print(f"\nA escanear o alvo: {alvo}")
print("-" * 30)

for porta in portas:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    resultado = s.connect_ex((alvo, porta))
    if resultado == 0:
        print(f"-> Porta {porta}: ABERTA")
    s.close()

print("-" * 30)
print("Scan concluído.")
