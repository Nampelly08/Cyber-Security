# Nmap Network Scanning

## What is Nmap?

Nmap (Network Mapper) is an open-source network scanning tool used to discover devices connected to a network and gather information about them. It helps identify active hosts, open ports, running services, and operating system details.

In this lab, I used Nmap from Kali Linux to scan devices on my local network. This helped me understand how network reconnaissance is performed before security testing.



## How Nmap Works

Nmap works by sending specially crafted packets to a target system and analyzing the responses. Based on the received packets, it determines whether a host is online, which ports are open, and what services are running.

### Step 1: Select a Target

The first step is to specify the IP address or hostname of the target system.

Example:

bash nmap 192.168.1.10


### Step 2: Check if the Host is Online

Nmap first checks whether the target device is reachable on the network.

If the host responds, Nmap continues the scan.



### Step 3: Scan Open Ports

Nmap sends packets to different TCP or UDP ports to determine whether they are:

* Open
* Closed
* Filtered

Open ports indicate that a service is available on the target machine.



### Step 4: Identify Running Services

Nmap can detect the services running on open ports and sometimes their versions.

Example:

* Port 22 – SSH
* Port 80 – HTTP
* Port 443 – HTTPS



### Step 5: Display Scan Results

After completing the scan, Nmap displays information such as:

* Target IP Address
* Host Status
* Open Ports
* Running Services
* Service Versions (if detected)



## Nmap Working


+----------------------+
| Enter Target IP      |
+----------------------+
          |
          v
+----------------------+
| Check Host Status    |
+----------------------+
          |
          v
+----------------------+
| Scan TCP/UDP Ports   |
+----------------------+
          |
          v
+----------------------+
| Detect Services      |
+----------------------+
          |
          v
+----------------------+
| Display Scan Result  |
+----------------------+


# Commands Used During the Lab

### Basic Scan

bash nmap 192.168.1.10

Scans the most common ports on the target host.

### Scan a Specific Port

bash nmap -p 22 192.168.1.10

Scans only port 22.

### Scan Multiple Ports

bash nmap -p 22,80,443 192.168.1.10


Scans ports 22, 80, and 443.

### Service Version Detection

bash nmap -sV 192.168.1.10

Detects services and their versions running on open ports.

### Operating System Detection

bash nmap -O 192.168.1.10

Attempts to identify the target operating system.

### Aggressive Scan

bash nmap -A 192.168.1.10

Performs OS detection, version detection, script scanning, and traceroute.


### Ping Scan

bash nmap -sn 192.168.1.0/24

Checks which devices are active on the network without scanning ports.

### Scan an Entire Network

bash nmap 192.168.1.0/24


Scans all devices within the specified subnet.

