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
    print("BHP Net Tool\n") # This tool is from Justin Seitz's Black Hat Python book. I have converted it from Python 2 syntax to Python 3
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

    if not len(sys.argv[1:]):
        usage()
    
    # read the commandline options
    try:
        opts,args = getopt.getopt(sys.argv[1:],"hle:t:p:cu", ["help","listen","execute","target","port","command","upload"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
    
    for o,a in opts:
        if o in ("-h","--help"):
            usage()
        elif o in ("-l","--listen"):
            listen = True
        elif o in ("-e","--execute"):
            execute = a
        elif o in ("-c","--commandshell"):
            command = True
        elif o in ("-u","--upload"):
            upload_destination = a
        elif o in ("-t","--target"):
            target = a
        elif o in ("-p","--port"):
            port = int (a)
        else:
            assert False,"Unhandled option"

    # listen to or just send data from stdin? if not, listen and len(target) and port > 0:

        # read the buffer from commandline
        # this will block, so send  ctrl-d if not sending input to stdin
        buffer = sys.stdin.read()

        # send data off
        client_sender(buffer)

    # listen and potentially upload things, exec commands, and drop a shell back depending on commandline options above
    if listen:
        server_loop()

main()
