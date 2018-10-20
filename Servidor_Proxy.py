import socket  # Importo Libreria Socket
import sys  # Importo Libreria para Shell
import threading  # Importo Hilos
import time
import binascii

print("*****************************************")
print("Bienvenido al Proxy")
print("*****************************************")
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
c.connect(("192.168.1.13", 8888))

conn, addr = s.accept()  # Creamos un espacio para la conexion


def esperar():  # Vamos a definir la funcion de esperar a un Mensaje

    while True:
        data = conn.recv(1024)  # recibir datos desde el enlace
        cliData = data.decode("utf-8")
        serData = str(cliData)
        data2 = serData.encode("utf-8")
        c.send(data2)  # Enviar Dato al Server conectados
    print('Enviado a : ' + addr[0])


def enviar():
    print("Conectados..")

    while True:
        data3 = c.recv(1024)
        serData2 = data3.decode("utf-8")
        if (serData2 != '..Dato Rechazado..' and serData2 != 'salir'):
            onCircle = True
            while onCircle:
                print('------------------')
                print(' Menu En Pantalla')
                print('------------------')
                print('Ingrese')
                print('1.Ver Palabra en Memoria')
                print('2.Modificar Palabra en Memoria')
                print('3.Enviar Palabra al Cliente')
                opt = input("Digite el numero correspondiente a la acción: ")
                onCircle = True
                while True:
                    if (opt != '1' and opt != '2' and opt != '3'):
                        opt = input(
                            "Digite un numero dentro del rango de las acciones: ")
                    else:
                        break

                if (opt == '1'):
                    print('Dato en Memoria: ' + serData2)
                elif (opt == '2'):
                    onCircle2 = True
                    while onCircle2:
                        print(
                            ' Seleccione la vocal a remplazar, nota: solo se remplazan las a por la vocal seleccionada')
                        print('------------------')
                        print('Ingrese')
                        print('1.e')
                        print('2.i')
                        print('3.o')
                        print('4.u')
                        opt2 = input(
                            "Digite el numero correspondiente a la acción: ")
                        while True:
                            if (opt2 != '1' and opt2 != '2' and opt2 != '3' and opt2 != '4'):
                                opt2 = input(
                                    "Digite un numero dentro del rango de las acciones: ")
                            else:
                                break
                        if (opt2 == '1'):
                            serData2 = str(serData2.replace("a", "e"))
                            onCircle2 = False
                        elif (opt2 == '2'):
                            serData2 = str(serData2.replace("a", "i"))
                            onCircle2 = False
                        elif (opt2 == '3'):
                            serData2 = str(serData2.replace("a", "o"))
                            onCircle2 = False
                        else:
                            serData2 = str(serData2.replace("a", "u"))
                            onCircle2 = False

                else:
                    onCircle = False
        cliData2 = str(serData2)
        data4 = cliData2.encode("utf-8")
        conn.send(data4)  # Enviar Dato al Server conectados
    print('Enviado a : ' + addr[0])


hilo1 = threading.Thread(target=esperar)
hilo2 = threading.Thread(target=enviar)
hilo1.start()
hilo2.start()
