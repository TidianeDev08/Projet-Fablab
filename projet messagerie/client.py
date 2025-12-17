import socket
import threading    

host = "localhost"
port = 3004

def receive_message(client):
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if not message:
                break
            print(message)
        except:
            break

try:
    print("Avant connexion")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    print("Connecté au serveur")

    name = input("Ton nom ou pseudo : ")
    client.send(name.encode("utf-8"))

    thread = threading.Thread(target=receive_message, args=(client,))
    thread.start()

    while True:
        data = input("")
        if data == "/quit":
            break
        client.send(data.encode("utf-8"))

except ConnectionRefusedError:
    print("Le serveur n'est pas disponible")

finally:
    client.close()
