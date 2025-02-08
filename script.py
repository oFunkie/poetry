import random
import socket
import shutil  # Pour obtenir la largeur du terminal

# Charger les poèmes
with open("poemes.txt", "r", encoding="utf-8") as f:
    poemes = f.read().strip().split("\n---\n")

def get_random_poem():
    """Sélectionne un poème et centre les lignes."""
    poeme = random.choice(poemes).split("\n")

    # Obtenir la largeur du terminal (par défaut 80 si inconnu)
    width = shutil.get_terminal_size((80, 20)).columns

    # Centrer chaque ligne
    return "\n".join(line.center(width) for line in poeme)

# Configuration du serveur
HOST = "0.0.0.0"
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Serveur en écoute sur le port {PORT}...")

    while True:
        client, addr = server.accept()
        with client:
            print(f"Connexion reçue de {addr}")
            message = "\033c" + get_random_poem() + "\n"
            client.sendall(message.encode("utf-8"))
            client.close()
