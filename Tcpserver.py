import socket, sys
errlvl=False
TcpServer=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("________  _____     ______ \n\___  __\ \  __\    \  __ \ \n    \ \    \ \       \ \_\ \ \n     \ \    \ \       \  ___\ \n      \ \    \ \___    \ \ \n       \_\    \____\    \_\   SERVER")
while(True):
    print("Escribe la ip en la que escuchar(Por defecto en localhost):\n --Si solo quieres que se conecte tu PC, localhost.\n --Si quieres que se puedan conectar los dispositivos de la red local, escribe tu IP local("+socket.gethostbyname(socket.gethostname())+").\n --Si quieres que se pueda conectar todo internet, escribe tu IP publica(http://miip.es/)")
    ipl=input(">>> ")
    if(ipl==""):
        ipl="localhost"
    print("Escribe el puerto por el que se va a escuchar(Por defecto es el 5555)")
    portl=input(">>> ")
    if(portl==""):
        portl=5555
    else:
        try:
            portl=int(portl)
        except Exception as e:
            errlvl=True
    if(not errlvl):
        try:
            TcpServer.bind((ipl, portl))
            break
        except Exception as e:
            print("Error: La IP o el Puerto no son validos")
    else:
        print("Error: La IP o el puerto no son validos")

TcpServer.listen(1)
while(True):
    connection, client_address=TcpServer.accept()
    try:
        print("Conexion TCP entrante de", client_address[0]+"\nRecibiendo datos:")
        while(True):
            TcpMsg=connection.recv(1024)
            TcpMsgt=bytes.decode(TcpMsg, 'utf-8')
            print(TcpMsgt)
            ans=input("Escribe una Respuesta: ")
            connection.sendall(bytes(ans, 'utf-8'))
    except Exception as e:
        connection.close()
    
