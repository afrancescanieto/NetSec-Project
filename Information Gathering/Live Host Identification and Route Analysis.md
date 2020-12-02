# Live Host Identification

Live Host Identification is used to help identify the live hosts within a network.

##### Why is this important?

If a host is live, then it means they have an IP address that can be used.

While **nmap** is usually preferred to identify live hosts, the following are more specific to live host identification and expand the variety of tools that can be used. 

**Remember that alot of these require root access**

## arping tool

Arping's greatest advantage is that it is straightforward and simple to do.

However disadvantages can include, 

1. Overt tediousness. 
    - If a /24 were to be used in this command, it would be iterated the full 255 times

2. Waiting for a response
    - It has no time limit so if a response is not given arping will not move to the next iteration




sudo arping -c <count> -i <interface> <Host/IP> # count parameter specifies the amount of count packets being sent


 **-c** represents the number of requests being done against that host

## fping tool

The main features that makes fping stand out is the flexible configuration of the command line. Since fping meant to be used in scripts, the output is designed to be easier to parse. 

An advantage of the fping tool is it's ability to iterate the packets without the present host needing to respond before going to the next one. The default has a time limit before deemed unreachable. 


sudo fping -a -g <ip_address> # shows the hosts that are alive and generates a live host target list


using **-a** to display targets that are alive

using **-g** to generate a list of ip addresses based on the CIDR notation 

## hping3

The special aspect of this tool is that it has the ability to spoof the source IP address. Meaning, that as the tester you can scan a host while hiding your own IP address. 

Other features of hping3: 

1. Firewall testing
2. Advanced port scanning
3. Network testing, using different protocols, TOS, fragmentation
4. Manual path MTU discovery
5. Advanced traceroute, under all the supported protocols
6. Remote OS fingerprinting
7. Remote uptime guessing
8. TCP/IP stacks auditing



sudo hping3 <host IP> -a <custom_IP>


**-a**  enables the spoof

**Spoofing can sometimes create a 100% packet loss due to the spoofed IP not being in the network**

## thcping6 tool

Thcping6 is similar to the hping3 tool. The only difference being that it only scan IPv6 addresses. It can also be used to fragment packets and slow scans. 


sudo thcping6 <interface> <destination IPv6>
# Route Analysis

## netdiscover Tool

This tool is essential in finding all the important network information about connected clients and the router. 
For clients that are connected information that can be found include, 

1. IP Addresses
2. MAC Addresses
3. Operating Systems
4. Open Ports

For the router, the information that can be found includes the manufacturer of the router. 
Although netdiscover is a simple and quick program for investigating this information, it doesn't provide detailed responses. 

It also can perform both active and passive reconnaissance. 



sudo netdiscover -r <IP_Address>/24 



In the command above, we are specifying a range for the CIDR number 24. The output contains the devices' IP and MAC addresses, and MAC vendor in that subnet.


sudo netdiscover -i <interface> -p # passive scan 


## netmask Tool

A simple tool that can swing between converting the IP range, subnet mask, CIDR, etc. It's useful small tool that aids in further gathering information of the submask and network that the Pentesting is occuring in.

The general pseudocode for the netmask command is as follows:


sudo netmask -f <<start IP>> : <<end IP>>
