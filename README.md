# PyHub
PyHub is a source control system meant to be installed and usede on local servers.

Installation:
 * Open a terminal and type `git clone https://github.com/siliconincorporated/PyHub.git`
 * `cd PyHub`
 * To set up the server, type `python PyHub_Server.py`
 * To set up a client, type `python PyHub_Client localhost:5024` and replace localhost with the server's IP address
 * See the instructions below for setting up a repo
 
Setting Up a Repository:
 * Change to the directory that your project is located in
 * Initialize the directory with `init`
 * Add all of the files in the directory with `add *` or just specific files with `add [filename]`
 * Push the files to the source control server with `push [repo name]`
 * Keep the repo updated with `sync [repo name]`
