import socket  # Importo Libreria Socket
import sys  # Importo Libreria para Shell
import threading  # Importo Hilos
import time
import binascii

print("Bienvenido al Server")
print("Estableciendo HOST, PORT y Array de datos")
time.sleep(2)
HOST = ''   # Nombre para el enlace
PORT = 8888  # Puerto Libre

# Definimos el tipo de socket y el tipo de protocolo (En este caso AF_INET con TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c = socket.socket()
print('Socket created / Socket Creado')  # Socket Creado
time.sleep(1)

try:  # Hacemos el enlace local y el puerto
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Error al enlazar')
    time.sleep(3)
    sys.exit()  # Forzamos la detencion del Script

# Finalmente quedamos enlazados
print('Socket bind complete / Socket Enlazado')
time.sleep(1)

s.listen(10)  # Modo de escucha del Server (Solo necesario desde el servidor)

print('Socket now listening / Ahora el Socket este en modo de espera')
time.sleep(1)

print('El server esta listo para recibir peticiones')
print('')
print("Por favor encienda el Servidor Central")
time.sleep(3)
c.connect(("10.0.2.15", 8888))

conn, addr = s.accept()  # Creamos un espacio para la conexion


def esperar():  # Vamos a definir la funcion de esperar a un Mensaje

    while True:
        data = conn.recv(1024)  # recibir datos desde el enlace
        response = cadena.encode("utf-8") # Codificar Dato a enviar
        conn.send(response) # Enviar Dato al Server conectados

    print('Enviado a : ' + addr[0] + '-' + str(addr[1]))


def enviar():
    print("Conectados..")
    # while True:
    #     data = conn.recv(1024)  # recibir datos desde el enlace
    #     recibido = data.decode("utf-8")  # Decodificar respuestas del cliente
    #     print("")  # Espaciador
    #     if (recibido == 'get'):
    #         print("Procesando el dato...")
    #         if(recibido == "salir"):
    #             print("cerrando sesión...")
    #             break
    #         else:
    #             for i in range(10):
    #                 array[i] = input(f"Ingrese el valor del datos {i+1} :")
    #             print("Se ha Guardado toda la traza correctamente, se procedera a enviar")
    #             for i in range(10):
    #                 data = conn.recv(1024)  # recibir datos desde el enlace
    #                 recibido = data.decode("utf-8")  # Decodificar respuestas del cliente
    #             print("Traza enviada")
    #     else:
    #         if (recibido == 'salir'):
    #             data = "salir"
    #             response = data.encode("utf-8")
    #             conn.send(response)
    #             conn.close()
    #             s.close()
    #         else:
    #             data2 = "Rechazado"
    #             response = data2.encode("utf-8")
    #             conn.send(response)
    #             print("Peticion Rechazada...")
    #
    #     print('Sigues Conectado con: ' + addr[0] + '-' + str(addr[1]))
    #
    # conn.close()
    # s.close()


hilo1 = threading.Thread(target=esperar)
hilo2 = threading.Thread(target=enviar)
hilo1.start()
hilo2.start()
