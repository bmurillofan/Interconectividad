import socket  # Importo Libreria Socket
import sys  # Importo Libreria para Shell
import threading  # Importo Hilos
import time  # Importo Timer
from functools import reduce


print("Bienvenido al Cliente")
client = socket.socket()
print("Esperando respuesta del Host")
time.sleep(1)
client.connect(("192.168.1.11", 8888))
print("Conectado")


def key():
    while True:
        print("")
        time.sleep(1)
        mensaje = input("Solicita con get, ack o salir..")
        dato = mensaje.encode('utf-8')
        client.send(dato)


def recibir():

    while True:
        print("")
        data = client.recv(1024)
        recibido = data.decode("utf-8")
        if (recibido == 'salir'):
            break
        elif (recibido == '..Dato Rechazado..'):
            print("Recibido: " + recibido)
        else:
            print("")
            a, b, c = recibido.split(",")
            print('Palabra #:' + a)
            print('Palabra: ' + b)
            print('Check Sum: ' + c)
            tmpValid = reduce(
                lambda x, y: x + y, map(ord, b))
            if (str(tmpValid) == c):
                print('Check Validado, la palabra no ha sufrido cambios')
            else:
                print('Check Invalido, la palabra ha sido modificada')
            # check = reduce(lambda x,y:x+y, map(ord, recibido))
            print("***********************************************************")
    print("Desconectado..")


hilo1 = threading.Thread(target=key)
hilo2 = threading.Thread(target=recibir)
hilo1.start()
hilo2.start()
