# Bradley Ward
# ECE 4325.001 - Telecommunication Networks
# Project 1 Server Side
# 10/08/19

# Adapted from example code from RealPython Socket Programming Guide
# https://realpython.com/python-sockets/

# Server program connects to client program by initializing with the current computer's IP address and a specific port
# number. The server will then listen for a single client connection and will accept a connection as soon as a client
# attempts to connect to the server. The server will then parse any client commands and return the proper command based
# on the client input. If the client sends a QUIT command, the server will echo the command back to the client and both
# will close their connections but the server will remain running waiting for another client to connect.

from datetime import datetime
import socket
import sys

HOST = ''  # left blank to assign current IP address as HOST
PORT = 23456  # Port to listen on (non-privileged ports are > 1023)
keepRunning = 1  # Boolean value to keep the server running in case of any additional connections


def ConnEnabled():  # Function for handling client commands if a client is currently connected
    with conn:
        print('Connected by', ipAddress)
        while True:
            data = conn.recv(1024)  # receive encoded data from client
            clientStr = data.decode()  # decode the data and place into string
            if clientStr == "TIME":  # check to see if client wants current date and time of server
                now = datetime.now()  # get date/time
                sendStr = now.strftime("%d/%m/%Y %H:%M:%S")  # format date/time into string
                print(sendStr)
                conn.send(sendStr.encode())  # encode and send string that holds the formatted date/time
            elif clientStr == "QUIT":  # check to see if client closed the connection
                sendStr = clientStr.encode()
                conn.send(sendStr)  # encode and echo the command back to the client to initiate the shutdown
                print("Terminated connection with ", ipAddress)
                s.close()  # close the socket
                return 1  # keep the server program running for more potential client connections

            else:
                sendStr = "Invalid Command"
                conn.send(sendStr.encode())  # if no command is matched, encode and send the client an error message


while keepRunning:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # open s as a socket
        try:
            s.bind((HOST, PORT))  # try to bind the host IP and preset port value
        except Exception as e:
            print(e)  # if we can't, display error message and exit the program
            sys.exit()

        s.listen(1)  # listen for at least 1 connection

        try:
            conn, ipAddress = s.accept()  # try to accept incoming connection from client
        except Exception as e:
            print(e)  # if accept() fails, then display an error message and exit the program
            sys.exit()

        keepRunning = ConnEnabled()  # go to the function and start receiving client commands
