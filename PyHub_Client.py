#!/usr/bin/python

## COMMANDS ##
# init [optional directory] -- initializes the directory as a repo
# sync [optional repo name] -- synchronizes files and folders in the repo (a repo name can be specified to download a repo from the server not on the local machine)
# add [file or directory (* adds all objects in the cwd)] -- adds file or directory to the current sync pool
# push -- pushes the current sync pool
# lock -- locks the current repo from making future synchs
# list_repos -- lists the repos avalible on the source control server

import time
import os.path
import socket

server_ip = input('Enter the IP address of the source control server: ')
host = socket.gethostname() # The name of the local machine, used when the server has to update the local machine's repo

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Set up a TCP socket
sock.connect((server_ip, 5024))

def _init(directory=os.getcwd()):
# If the folder isn't initialized for source control, add a source control init file
if os.path.isfile('.source-control-init'):
    # Run the source control system
    walk_cwd()
else:
    # Make the init file and then run the source control system
    open('.source-control-init', 'w')
    walk_cwd()

def walk_cwd():
    walk_folder('.')
    folders = [f for f in os.listdir('.') if not os.path.isfile(f)] # Walk for the folders
    for f in folders:
        walk_folder(f)
def walk_folder(f):
    os.cwd(f)
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        send_file(f)
def send_file(f):
    sock.send(f) # Send the file name
    line = f.read(1024)
    while (line):
        sock.send(line)
        line = f.read(1024)
    sock.send('TRANSFER_COMPLETE') # Send an indicatior so the server knows when to stop writing to a file and start another one

sock.shutdown(socket.SHUT_WR)
sock.close()

