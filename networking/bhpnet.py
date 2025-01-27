import sys
import socket
import getopt
import threading
import subprocess

# global variables
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

def usage():
    print("BHP Net Tool\n") # This tool is from Justin Seitz's Black Hat Python book
    print("Usage: bhpnet.py -t target_host -p port")
    print("-l --listen              - listen on [host]:[port] for incoming connections")
    print("-e --execute=file_to_run - execute the given file upon receiving a connection")
    print("-c --command             - initialise a command shell")
    print("-u --upload=destination  - upon receiving connection upload a file and write to [destination]")
    print("\n\nExamples:\n")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -c")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\"")
    print("echo 'ABCDEFG' | ./bhpnet.py -t 192.168.11.12 -p 135")
    sys.exit()

def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target
