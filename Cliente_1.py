import socket  # Importo Libreria Socket
import sys  # Importo Libreria para Shell
import threading  # Importo Hilos
import time # Importo Timer

print("Bienvenido al Cliente")
client = socket.socket()
print("Esperando respuesta del Host")
time.sleep(1)
client.connect(("192.168.1.2", 8888))
print("Conectado")


def key():
	while True:
		print("")
		mensaje = input("Solicita con get, ack o salir..")
		dato = mensaje.encode('utf-8')
		client.send(dato)


def recibir():

    while True:
        print("")
        data = client.recv(1024)
        recibido = data.decode("utf-8")
        if (recibido == 'salir'):
            break;
        elif (recibido == '..Dato Rechazado..'):
            print("Recibido: " + recibido)
        else:
            print("***********************************************************")
            from functools import reduce
            for x in data:
                print(x)
            # check = reduce(lambda x,y:x+y, map(ord, recibido)) 
            # print(recibido[0])  # borrar "Token-" " Palabra-" " CheckSum-" 
            # print("Recibido: " + recibido + " ACK DEL PROTOCOLO CLIENTE: " + check)
            print("***********************************************************")
    print("Desconectado..")


hilo1 = threading.Thread(target=key)
hilo2 = threading.Thread(target=recibir)
hilo1.start()
hilo2.start()