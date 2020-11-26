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

sudo netdiscover -r 192.168.1.2/24 

In the command above, we are specifying a range for the CIDR number 24. The output contains the devices' IP and MAC addresses, and MAC vendor in that subnet.

## netmask Tool

A simple tool that can swing between converting the IP range, subnet mask, CIDR, etc. It's useful small tool that aids in further gathering information of the submask and network that the Pentesting is occuring in.

The general pseudocode for the netmask command is as follows:
sudo netmask -f <start IP>:<end IP>