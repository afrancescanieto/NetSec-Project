# SNMP Analysis

The Simple Network Management Protocol responsible for exchanging the management information between network devices. It resides as a part of TCP/IP. SNMP is widely accepted a network protocol that is able to monitor and manage network elements. Most network elements come with a SNMP agent. 

### SNMP Manager 

The manager is seperate to the network elements and typically communicates with the SNMP agent within the network devices. 

Key Functions: 

1. Queries agents
2. Recieves agent responses 
3. Sets the variable in agents 
4. Acknowleges the asynchronous events from agents

### SNMP Agent 

A program within a network device that allows for the collection of the management's database. 

Key Functions: 

1. Collecting management info about the local enviornment
2. Both stores and retrieves management info 
3. Signals an event ot the manager 
4. Can act as a proxy for some non-SNMP manageable network node

## onesixtyone 

Onesixtyone is an SNMP scanner that sends a wave SNMP requests as fast as it can. The pentester is able to configure the speed and find out the description of the software running on the device. 

*The explanation to this tool is more in depth in the Exploitation Phase.*


onesixtyone (options) <\host\> <\community\>


## snmp-check

This tool is the more user friendly of the two, as it displays the enumerated SNMP devices in a readable format. 

The enumerations it supports are: 

1. contact
2. description
3. detect write access (separate action by enumeration)
4. devices
5. domain
6. hardware and storage informations
7. hostname
8. IIS statistics
9. IP forwarding
10. listening UDP ports
11. location
12. motd
13. mountpoints
14. network interfaces
15. network services
16. processes
17. routing information
18. software components
19. system uptime
20. TCP connections
21. total memory
22. uptime
23. user accounts


 snmp-check <\IP_address\> -c public

