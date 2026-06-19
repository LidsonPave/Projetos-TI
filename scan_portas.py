import socket

alvo = "127.0.0.1"
portas = [21, 22, 80, 443]

print(f"A escanear o alvo: {alvo}")
for porta in portas:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    resultado = s.connect_ex((alvo, porta))
    if resultado == 0:
        print(f"-> Porta {porta}: ABERTA")
    s.close()
