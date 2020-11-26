# Network and Port Scanners

This part of the information gathering phase of PenTesting a network is crucial to understanding and maping out a network. For an attacker, it creates a blueprint of the information needed to launch an attack. 

**Using the sudo command ensures that all permissions are allowed with these commands**

## masscan tool 

This tool is popular and alot of opinions lean toward it being the fastest port scan tool. You can technically scan the entire internet with this tool, but only if you're interested in getting a no-so-fun call from the ISP. 
sudo masscan 192.168.1.0/24 -p80,443
In this example, we are scanning ports 80 and 443 for open ports in a particular network. 

## nmap

Network Mapper is used for creating a network map, find remote IP addresses of any hosts, identify the OS system and software details, the services a host is using, finding open ports on both local and remote systems, and finding vulnerablities on remote and local hosts.

### Basics

The basic nmap command:
sudo nmap 192.168.1.2 sudo nmap instagram.com
Using nmap to scan an entire subnet:
sudo nmap 192.168.1.2/24
## nmap Scanning Techniques 

#### TCP SYN Scan (-sS)

While this is the same as a basic scan, it allows nmap to get the remote host's information without having to do the TCP Handshake. This method sends packets to its destination without creating sessions, thus not allowing the target computer to create any log of this communication due to no session being initiated. 

nmap -sS 192.168.1.2

#### TCP connect() scan (-sT)

This technique is the default, and is the same as the -sS scan but it does go through the threeway handshake process, thus creating a session and logging the interaction. 
sudo nmap -sT 192.168.1.1 
#### UDP Scan (-sU)

This technique doesn't require any SYN Packets to be sent because it targets the UDP ports. It sends the UDP packets to the remote host, the response can either be that the ICMP is unreachable meaning the port is closed or that the port is open. 
sudo nmap -sU 192.168.1.1
#### FIN Scan (-sF ) 

When a network has a firewall SYN packet will be blocked. To avoid this from happening, a FIN scan can send a packet set only with a FIN flag, which doesn't require it to go through the TCP Handshaking. Since the FIN packets don't have to TCP handshake the host isn't able to create a log of this scan. 
sudo nmap -sF 192.168.1.2
#### Ping Scan (-sP)

Used to find out whether or not a host is alive or not. Better used in the Live Host Identification stage of information gathering. 
sudo nmap -sP 192.168.1.2
#### Idle Scan(-sI) 

This scanning technique creates complete anonymity during scanning by not sending the packets from the source IP address. It sends packets from another host from the TARGET network. The scan pseudcode is as follows:
sudo nmap -sI <zombie_host> <target_host>sudo nmap -sI 192.168.1.6 192.168.1.2
### Version Detection (-sV)

Used for finding the software version that the target host is running on it's open ports. It can't be used to detect open ports, but it needs them to have the information of the what software version is being used. It uses the TCP SYN scan to find the open ports to execute.
sudo nmap -sV 192.168.1.2
### OS Detection nmap

The ability to detect what operating system the remote host is using is one of the more useful features in the nmap tool. By knowing the OS certain vulnerabilities can be inferred and narrowed down. TCP and UDP packets are sent to the target host and the response is analyzed by nmap and compared to its database of operating systems. This process also includes the detection of open ports, thus making it slower.
sudo nmap -O 192.168.1.2
The output of this command includes:

1. Device Type
2. The Operating System its running on
3. OS details
4. Network Distance
5. The Open Ports

It can also be ensured that ping is disabled in order to bypass the blockage of the firewall. 
sudo nmap -O -PN 192.168.1.2/24
If there aren't any ports open, nmap gives an error and the results become unreliable. 
