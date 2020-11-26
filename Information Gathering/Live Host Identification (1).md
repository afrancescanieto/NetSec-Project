# Live Host Identification

As the name states, using the following tools will help identify the live hosts within a network for the information gathering stage. This goes for devices inside a network that have an IP Address assigned to them. 

**Remember that alot of these require root access**

## arping tool

When using the arping command, doing a live host identfication requires the IP Address of that network. This is a downside due to it's tediousness. Let's say you're doing a /24. You would have to do this process 255 times. A pro of this command is that it is straightforward and simple to do.
sudo arping -c 2 192.168.1.2
the -c 2 represent the number of requests being done against that host. 

## fping tool

Using this tool you can use different notations and has many options and ranges of the IP addresses. 
sudo fping -a -g 192.168.1.2
using -a to display targets that are alive

using -g to generate a list of ip addresses based on the CIDR notation 

## hping3

The special aspect of this tool is that it has the ability to spoof the source IP address. Meaning, that as the tester you can scan a host while hiding your own IP address. The downside, it only scans one host per command. As with the arping tool, you can always create a loop to automate this downside.
sudo hping3 -c 192.168.1.2 -a 8.8.8.8
Using -a enables the spoof

**Spoofing can sometimes create a 100% packet loss due to the spoofed IP not being in the network**

## thcping6 tool

This tool is similar to the hping3 tool but the difference being that it only scan IPv6 addresses. It can also be used to fragment packets and slow scans. 
sudo thcping6 eth0 <destination IPv6>