# What is SSH?

SSH (Secure Shell) is a secure network protocol used to connect one computer to another over a network. It allows users to remotely access and manage another system using a command-line interface. SSH encrypts all communication between the client and the server, making it much safer than older remote login methods like Telnet.

In my lab, I used SSH to connect my Windows system with a Kali Linux virtual machine. This helped me understand how remote administration works in a secure environment.

# How SSH Works

# SSH communication follows a simple process:

Step 1: SSH Server Starts

The target machine (server) runs an SSH service and listens for incoming connection requests on port 22, which is the default SSH port.

Step 2: Client Sends a Connection Request

The client system uses the SSH command to connect to the server by providing the server's IP address and username.

Example:

ssh kali@192.168.1.10

Step 3: Authentication

The server verifies the identity of the user. Authentication can be done using:

Username and password
SSH key pair (public and private keys)

Only authenticated users are allowed to access the system.

Step 4: Secure Connection

After successful authentication, an encrypted communication channel is created between the client and the server. All commands and data exchanged are protected from eavesdropping.

Step 5: Remote Administration

The user can now execute Linux commands, transfer files, manage services, or configure the remote system securely.


+------------------+         Encrypted Connection         +------------------+
|  Client Machine  |  ------------------------------->    |  SSH Server      |
| (Windows CMD)    |                                      | (Kali Linux)     |
+------------------+                                      +------------------+
        |                                                        |
        |---- Connection Request -------------------------------> |
        |<--- Authentication Required --------------------------- |
        |---- Username / Password or SSH Key -------------------> |
        |<--- Authentication Successful ------------------------- |
        |========== Secure Encrypted Session Established ========|
        |                                                        |
        |---- Execute Linux Commands ---------------------------> |
        |<--- Receive Command Output ---------------------------- |
