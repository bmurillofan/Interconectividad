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
array = [None] * 10  # El array para data
arrayTokens = [None] * 10  # El array para data
arrayCheckSum = [None] * 10  # El array para data

# Definimos el tipo de socket y el tipo de protocolo (En este caso AF_INET con TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
conn, addr = s.accept()  # Creamos un espacio para la conexion


def esperar():  # Vamos a definir la funcion de esperar a un Mensaje

    while True:
        data = conn.recv(1024)  # recibir datos desde el enlace
        recibido = data.decode("utf-8")  # Decodificar respuestas del cliente
        if (recibido == 'get'):
            print("Armando los datos...")
            time.sleep(1)
            for i in range(10):
                arrayTokens[i] = str(i + 1)
                array[i] = input(f"Ingrese el valor del datos {i+1} :")
                arrayCheckSum[i] = ' '.join(format(ord(x), 'b') for x in array[i])
            print("")
            print("Se ha Guardado toda la traza correctamente, se procedera a enviar")
            for i in range(10):
                data = conn.recv(1024)  # recibir datos desde el enlace
                recibido = data.decode("utf-8") # Decodificar respuestas del cliente
                while (recibido != 'ack'):
                    data2 = "X-Dato Rechazado-X"
                    response = data2.encode("utf-8")
                    conn.send(response)
                    print("Error en ack!!")
                    data = conn.recv(1024)  # recibir datos desde el enlace
                    recibido = data.decode("utf-8") # Decodificar respuestas del clientes
                cadena = "Token-" + arrayTokens[i] + " Palabra-" + array[i] + " CheckSum-" + arrayCheckSum[i]
                response = cadena.encode("utf-8") # Codificar Dato a enviar
                conn.send(response) # Enviar Dato al Server conectados
            print("")
            print("Traza enviada")

        else:
            if (recibido == 'salir'):
                print("Cerrando sesion...")
                time.sleep(2)
                conn.close()
                s.close()
            else:
                data2 = "X-Dato Rechazado-X"
                response = data2.encode("utf-8")
                conn.send(response)
                print("La peticion fue rechazada...")

        print('Conectado con: ' + addr[0] + '-' + str(addr[1]))

    conn.close()
    s.close()


def enviar():
    print("Ahora estan Conectados...")


hilo1 = threading.Thread(target=esperar)
hilo2 = threading.Thread(target=enviar)
hilo1.start()
hilo2.start()
