import socket  # Importo Libreria Socket
import sys  # Importo Libreria para Shell
import threading  # Importo Hilos
import time

print("Bienvenido al Cliente")
client = socket.socket()
client.connect(("10.111.19.232", 8888))
print("Conectado")


def key():
	while True:
		print("")
		mensaje = input("Ingrese get, ack o salir..")
		dato = mensaje.encode('utf-8')
		client.send(dato)


def recibir():
    print("Escuchando...")

    while True:
        print("")
        data = client.recv(1024)
        recibido = data.decode("utf-8")
        print("Recibido: " + recibido)

hilo1 = threading.Thread(target=key)
hilo2 = threading.Thread(target=recibir)
hilo1.start()
hilo2.start()
