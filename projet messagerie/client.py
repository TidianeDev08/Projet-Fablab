import socket
import threading   
import tkinter as tk 

host = "localhost"
port = 3004

fenetre = tk.Tk()
fenetre.title("Les messages")
fenetre.geometry("400x400")

zones_messages = tk.Text(fenetre)
zones_messages.pack(padx=10, pady=10, fill="both", expand=True)

def receive_message(client):
    while True:
        try:  
            message = client.recv(1024).decode("utf-8")
            if not message:
                break
            print(message)
        except:
            break

def afficher_message():
    data = ecrire_message.get()
    if data !="":
        try:
            client.send(data.encode("utf-8"))
            ecrire_message.delete(0, "fin")

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
