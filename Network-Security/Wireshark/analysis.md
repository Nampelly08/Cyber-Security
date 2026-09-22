## DNS Analysis

During packet capture, I generated DNS traffic by accessing websites and performing domain name lookups. The Wireshark capture shows DNS queries and responses between my system and the DNS server.

The client system (10.0.2.15) sent a DNS query to the DNS server (10.83.84.116) requesting the IP address of **google.com**. The DNS server processed the request and returned the corresponding IP address in its response.

I also observed both IPv4 (A record) and IPv6 (AAAA record) queries. This indicates that the system was attempting to obtain both IPv4 and IPv6 addresses for the requested domain.

**Observations:**

* Source IP: 10.0.2.15
* DNS Server: 10.83.84.116
* Query Type: A Record (IPv4)
* Query Type: AAAA Record (IPv6)
* Domain Queried: google.com
* Protocol: DNS over UDP Port 53

**Result:**
The DNS server successfully resolved the domain name and returned the required IP addresses. This allowed the system to establish further communication with the destination website.


## ARP Analysis

During the packet capture, I observed ARP (Address Resolution Protocol) traffic on the local network. ARP is used to find the MAC address associated with a specific IP address before communication can take place.

The capture shows that the system with IP address **10.0.2.15** sent an ARP request asking for the MAC address of **10.0.2.2**. This request was broadcast on the network because the sender did not know the destination MAC address.

The device with IP address **10.0.2.2** replied with its MAC address **52:54:00:12:35:00**, allowing the sender to update its ARP table and continue communication.

**Observations:**

* Source IP: 10.0.2.15
* Destination IP: 10.0.2.2
* ARP Request: "Who has 10.0.2.2? Tell 10.0.2.15"
* ARP Reply: "10.0.2.2 is at 52:54:00:12:35:00"

**Result:**
The MAC address of the destination host was successfully resolved through the ARP process.


## HTTP Analysis

During the packet capture, I observed HTTP traffic generated while accessing a web resource. HTTP (Hypertext Transfer Protocol) is used for communication between web browsers and web servers.

The capture shows an HTTP GET request sent from my system to the web server. The client requested the file **/success.txt**, and the server responded with a **200 OK** status code, indicating that the request was successful and the resource was available.

The exchange demonstrates the basic client-server communication process used in web browsing. The client sends a request for a resource, and the server processes the request and returns the requested content.

**Observations:**

* Client IP: 10.0.2.15
* Server IP: 34.107.221.82
* Protocol: HTTP
* Request Method: GET
* Requested Resource: /success.txt
* Server Response: HTTP/1.1 200 OK

**Result:**
The requested resource was successfully retrieved from the web server without any errors.

**Conclusion:**
The captured HTTP packets demonstrate a successful web communication session between the client and the server. The server received the request, processed it correctly, and returned the requested content. This confirms normal HTTP communication and proper connectivity between the client and the web server.

## ICMP Analysis

During the packet capture, I generated ICMP traffic using the ping command to test network connectivity. ICMP (Internet Control Message Protocol) is commonly used for diagnostics and troubleshooting.

The capture shows ICMP Echo Request packets being sent from my system (**10.0.2.15**) to the destination host (**142.251.223.238**). The destination host responded with ICMP Echo Reply packets, indicating that it was reachable and responding correctly.

The request and reply packets were exchanged successfully without any packet loss, confirming proper network connectivity between the two hosts.

**Observations:**

* Source IP: 10.0.2.15
* Destination IP: 142.251.223.238
* Protocol: ICMP
* Packet Type: Echo Request and Echo Reply
* TTL Value: 64

**Result:**
The destination host responded successfully to all ping requests, confirming that the network path was functioning properly.

**Conclusion:**
The ICMP packets captured during this session were used to verify connectivity between the client and the destination host. The successful exchange of Echo Request and Echo Reply packets indicates a stable network connection and proper communication between the devices.

## TCP Analysis

During network traffic analysis, I observed TCP communication between the client and server. TCP (Transmission Control Protocol) is a reliable transport layer protocol that ensures data is delivered correctly and in the proper order.

Before data transfer begins, TCP establishes a connection using a three-way handshake. The client sends a SYN packet, the server responds with SYN-ACK, and the client replies with ACK. After the connection is established, data is exchanged between both devices.

TCP provides error checking, packet sequencing, and retransmission of lost packets, making it suitable for applications where reliability is important.

**Observations:**

* Connection established using the three-way handshake.
* SYN, SYN-ACK, and ACK packets were captured.
* Data was transferred successfully between the client and server.
* No packet loss was observed during the session.

**Result:**
The TCP connection was established successfully and data was exchanged reliably between the communicating devices.


## UDP Analysis

During packet capture, I observed UDP (User Datagram Protocol) traffic generated by DNS requests. Unlike TCP, UDP does not establish a connection before sending data and does not provide acknowledgments or retransmissions.

UDP is designed for fast communication where speed is more important than reliability. Because there is no connection setup process, UDP packets can be transmitted with lower overhead.

In the captured traffic, DNS queries were sent from the client to the DNS server using UDP port 53. The server responded with the requested domain information.

**Observations:**

* UDP packets were observed during DNS communication.
* No connection establishment process was required.
* Communication occurred through port 53.
* DNS queries and responses were exchanged successfully.

**Result:**
The DNS server successfully processed the UDP requests and returned the required information.

