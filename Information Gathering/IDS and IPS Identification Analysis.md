# IDS/IPS Identification

 First question that comes up is what's the difference between the two and what do they do?

## The Intrusion Detection Systems ( IDS ) 

The job of an IDS is to be the network traffic analyzer. They analyze network packets and find signatures of a known cyberattack and alerts when any of that suspicious activity is discovered. Any violation is then reported to the systema admin or to a security information and event management system (SIEM), which then essentially filters the actual threats from the false alarms by comparing it to different outputs. This is especially important because a great flaw in these systems are that they are susceptible to false alarms. Organizations need to set up these systems correctly to be able to differeciate from normal traffic to malicious activity. 

### Classifying the 5 types of IDS 

#### Network Intrusion Detection System (NIDS)

These systems are setup into a network to examine traffic from all the devices connected. An observation of traffic is preformed in the entire subnet and is then compared to the traffic that is then passed on the subnets victim to the known previous attacks. If an attack is identified, the alert is then sent to an Admin.


A good place to install it is on the subnet that has a firewall, to monitor if someone were attempting to break it.

#### Host Intrusion Detection System (HIDS) 

In the hosts or devices in a network, the HIDS monitors the packets going in and out of the device. It alerts the admin after it detects malicious activity from the comparison of a snapshot of the system files that are existing and the previous snapshot.  If system files were found to be edited or deleted, the alert is sent. 


HIDS are typically used in mission critical machines that do not expect to change the layout of their files

#### Protocol-based Intrusion Detection System( PIDS ):

A PIDS could be a system or agent that lives and protects the front end of a server. It controls and investigates protocols sent between users or devices and the server. Specifically if an interface is un-encrypted. 


A good example is the protection of the web server through the monitoring of the HTTPS protocol stream. This system would likely be installed in the HTTPS interface. 

#### Application Protocol-based Intrusion Detection System (APIDS) 

The APIDS could also be a system or agent residing within a group of servers. The differens is that it monitors the communication on application based protocols.


An example being monitoring the SQL protocol's middleware as it communicates with the database in the web server. 

#### Hybrid Intrusion Detection System 

As the it states it is indeed a hybrid of two or more IDS. In this hybrid a host agent or a systems data is combined with the network's information in order to have a complete view of the network system. Its been proven to be more effective in terms of efficiency.

### Two Methods Used by IDS 

#### Signature-Based

This method detets the attacks on the specific patterns of the basis in the network traffic like the number of bytes or bits. It compares these patterns to already known malicious sequences in malware. The biggest flaw in this method is that the signatures have to be KNOWN, any new sequences will not be detected and will bypass the software. 

#### Anomaly-Based 

Now to cover the flaw of the signature based method, anomaly methods detects the unknown malware attacks. This is done through the usage of machine learning that creates a model of trustful activity. Anything that does not follow the model is declared suspicious and is then flagged. 

## Intrusion Prevention Systems ( IPS )

The main difference between an IPS and an IDS is the control system that accepts or rejects a packet based on the guidelines configured when installed. IPS also requires that the database be updated with new threat data regularly, while IDS requires a human or another system to look at the results. The IDS and the IPS are augmented together and work on the IPS to detect and mitigate threats. 

### Classifying the 4 Types of IPS

#### Network-based Intrusion Prevension System (NIPS)

It monitors the ENTIRE network by analyzing protocol activity for suspicious traffic 

#### Wireless intrusion prevention system (WIPS)

It monitors the WIRELESS network by analyzing protocol activity for suspicious traffic 

#### Network Behavior Analysis

The examination of network traffic for unusual traffic flows,(like DDoS attacks), or specific forms or policy violations and malware.

#### Host-Based Intrusion Prevention System (HIPS)

An inbuilt software package inside a single host that scans events that occure within that host.

## Comparison of IPS and IDS Summarized

1. IPS are able to actively prevent and block intrusions that are detected

2. IPS can actually take the actions of dropping detected packets, sending an alarm, resetting a connection, or blocking traffic from the offensive IP Addresses while an IDS sends it to admin to investigate. 

3. IPS can also correct CRC errors, defragments packet streamsm, and mitigate TCP sequencing issues

## The Load Balancing 

A method that acts like a reverse proxy to distribute network and application traffic across servers using the load balancer hardware.

### How does it differ from DNS Redirection?

It doesn't really. It just helps the issuing of DNS requests become less overwhelming to a network. 

### lbd cmd in Kali Linux

Using the lbd can detect whether a given domain is using load balancing or not. It checks for both DNS and HTTP load balancing. 
lbd instagram.com
## Web Application Firewalls (WAF)

These application firewalls filters, monitors, and blocks HTTP traffic. It's a layer 7 defense firewall that protects against attacks such as cross-site forgery, cross site scripting (XSS), and SQL injections. 

### wafw00f in Kali Linux

This tool fingerprints and identifies Web Application Firewall products. It connects to the web server, and it starts out with a normal HTTP response and then escalates from there. 

#### How does it work?

1. Sends the normal HTTP Request and identifies the number of WAF solutions from the analysis of the response
2. If unsuccessfull, it sends a number of HTTP requests
3. If that is also unsucessful, it analyzes all the responses collectively to and guesses if a WAF is in place, responding to the attacks

**wafw00f <\domain_URL\>**
Use the following command to view all the firewalls wafw00f can detect

**wafw00f -l**
