# Wireshark Network Packet Analysis

## What is Wireshark?

Wireshark is a free and open-source network packet analyzer used to capture and examine network traffic in real time. It helps users understand how devices communicate over a network by displaying every packet that is sent and received.

In this lab, I used Wireshark to capture network packets generated between my Windows host and Kali Linux virtual machine. This helped me understand different network protocols and how data travels across a network.


# How Wireshark Works

Wireshark captures packets that pass through a selected network interface and displays detailed information about each packet.

Step 1: Select a Network Interface

The first step is to choose the network interface to monitor, such as Ethernet, Wi-Fi, or a VirtualBox adapter.

Step 2: Start Packet Capture

After selecting the interface, Wireshark begins capturing all incoming and outgoing network packets in real time.

Step 3: Generate Network Traffic

To capture useful packets, network activity is generated. This can be done by:

* Opening a website
* Using the ping command
* Connecting through SSH
* Accessing another device on the network

Step 4: Analyze Packets

Each captured packet contains useful information such as:

* Source IP Address
* Destination IP Address
* Protocol Used
* Packet Length
* Time of Capture

Wireshark allows these details to be viewed for troubleshooting and network analysis.

### Step 5: Apply Filters

Filters help display only the packets related to a specific protocol or address.

Some commonly used filters are:

text icmp

Shows only ping packets.

text tcp

Shows TCP packets.

text udp

Shows UDP packets.

text ssh

Shows SSH communication.

text ip.addr == 192.168.1.10

Shows packets sent to or received from a specific IP address.



# Wireshark Working

+-------------------+
| Select Interface  |
+-------------------+
          |
          v
+-------------------+
| Start Capture     |
+-------------------+
          |
          v
+-------------------+
| Generate Traffic  |
| (Ping, SSH, Web)  |
+-------------------+
          |
          v
+-------------------+
| Capture Packets   |
+-------------------+
          |
          v
+-------------------+
| Analyze Protocols |
| IP, TCP, UDP etc. |
+-------------------+
          |
          v
+-------------------+
| Apply Filters     |
+-------------------+


