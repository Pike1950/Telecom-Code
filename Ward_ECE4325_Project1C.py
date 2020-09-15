# Bradley Ward
# ECE 4325.001 - Telecommunication Networks
# Project 1 Client Side
# 10/08/19

# Adapted from example code from RealPython Socket Programming Guide
# https://realpython.com/python-sockets/

# Client program connects to server program via calling the script in the command line with the IP of the server. The
# can then send commands TIME, which gets the current date/time from the server, and QUIT, which will close the socket
# and exit the program.


import socket
import sys
import ipaddress

sys.argv.pop(0)  # get rid of the first element in the argument values which is the file path for the python script
if len(sys.argv) != 2:  # check if there is enough arguments i
    print('Invalid number of arguments')
    sys.exit()
else:
    try:
        ipaddress.ip_address(sys.argv[0])  # check to see if the ip address is proper
    except Exception as e:
        print(e)  # if ip address is bad then display error message and exit program
        sys.exit()


HOST = sys.argv[0]  # The server's hostname or IP address
PORT = int(sys.argv[1])  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))  # try to connect to the host server
    except Exception as e:
        print(e)  # if connect fails, display error and quit program
        sys.exit()
    print("Successful connection to %s on port %i" % (HOST, PORT))

    while 1:
        userInput = input('Client> ')
        s.send(userInput.encode())  # get an input, encode it, and send it to the server
        serverStr = s.recv(1024).decode()  # receive resultant string based on available client commands

        if serverStr == "QUIT":  # check to see if server echoed the QUIT command
            print("Terminated connection with %s" % HOST)
            s.close()  # close the socket
            sys.exit()  # exit the program

        print("Server>", serverStr, "\n")  # print resultant string from server based on client input






