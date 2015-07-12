#!/usr/bin/python3

## COMMANDS ##
# init [optional directory] -- initializes the directory as a repo
# repo [repo name] [optional comma seperated branches] -- Create a new repo on the source control server and if provided, initialize it with the specified branches (master is always created)
# branch [repo name] [branch name] -- Create a new branch in the specified repo
# sync [optional repo name] -- synchronizes files and folders in the repo (a repo name can be specified to download a repo from the server not on the local machine)
# add [file or directory (* adds all objects in the cwd)] -- adds file or directory to the current sync pool
# push -- pushes the current sync pool
# pull -- updates the local machine's files with the changes on the source control server
# lock -- locks the current repo from making future synchs
# list_repos -- lists the repos avalible on the source control server

# Run the Python file in the repo directory with the argument init
# Add files to the repo with the argument add [file name]
# Push the files to the repo
# Make changes on the local machine and update the repo with the argument sync
# Client can make automatic syncs to the repo based on a schedule
# Lock the local machine's files and server's repo with the lock argument (typically used with repos on sync schedules)

import time
import sys, os.path
import socket

server_ip = 'localhost'
host = socket.gethostname() # The name of the local machine, used when the server has to update the local machine's repo

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Set up a TCP socket
sock.connect((server_ip, 5024))

file_queue = []

def _init(directory=os.getcwd()):
    # If the folder isn't initialized for source control, add a source control init file
    if not os.path.isfile('.source-control-props'):
        source_control_props = open('.source-control-props', 'w')
        # TODO: Write hash value
        source_control_props.write('server_ip:' + server_ip + '\n')
        source_control_props.write('lock:False') # Used for locking repo syncs, by default, this is disabled
    else: print('This folder has already been initialized, skipping...')
def _repo(repo_name, *args):
    pass
def _branch(repo, branch_name):
    pass
def _sync(repo):
    pass
def _add(f):
    file_queue.append(f)
def _push(repo, branch='master'):
    for l in open('.source-control-props', 'r').readlines():
        if l is 'lock:True':
            print('This repo has been locked, please run \'ulock ' + repo + '\'to enable syncs.')
        else:
            for f in file_queue:
                send_file(f)
def _pull(repo, branch='master'):
    pass
def _lock(repo):
    open('.source-control-props', 'w').write('lock:True')
def _list_repos():
    pass

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
    if '/' or '\\' in f:
         filename = os.path.split(f)[1]
    else:
        filename = f
    s.send(filename)
    line = f.read(1024)
    while (line):
        sock.send(line)
        line = f.read(1024)

sock.close()

if __name__ == '__main__':
    # Open a shell-like prompt
    while True:
        prompt = input('[PyHub@' + socket.gethostname() + ']$ ')
        command = prompt.split()[0]
        arguments = prompt.split()[1:]
        
        # The command cases
        if command == 'init': _init()
        elif command == 'repo':
            if arguments > 1:
                _repo(arguments[0], arguments[1:])
            else:
                _repo(arguments[0])
        elif command == 'branch': _branch(arguments[0], arguments[1])
        elif command == 'sync': _sync(arguments[0])
        elif command == 'add': _add(arguments[0])
        elif command == 'push': 
            if len(arguments) > 1:
                _push(arguments[0], arguments[1])
            else:
                _push(arguments[0])
        elif command == 'pull':
            if len(arguments) > 1:
                _pull(arguments[0], arguments[1])
            else:
                _pull(arguments[0])
        elif command == 'lock': _lock(arguments[0])
        elif command == 'list_repos': _list_repos()
        else: print('Command ' + command + ' not recognized.')