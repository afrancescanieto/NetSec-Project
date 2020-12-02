# OSINT Analysis

The general definition of Open-Source Intelligence is information availible to the general public. It's important to note that it is not limited to only google. 
The definition as per U.S public law states that OSINT can be,

1. Produced from PUBLICLY available info
2. Collected and analyzed to an audience appropriate to the situation

Again, just because it can be found in mass search engines, doesn't mean its not open sourced. 
Other information that can be considered open sourced include:

1. Info published for the public such as news media
2. For public consumption availablity on request such as census data
3. For public consumption through a subscription such as industry journals
4. Data that can be seen or heard casually 
5. Data available at a meeting for the general public to attend
6. Data that is obtained at a general public meeting 


## How can it be used in regards to Penetration Testing?

OSINT is used by pentesting professionals to find weaknesses in a network. 
Some common ones found by using OSINT include:

1. Leaks of sensitive info on Social Media
2. Open Ports or unsecured devices connected to the internet
3. Software that are considered unpatched 
4. Assets that are exposed, such as proprietary code on pastebins

A big point to make is that if something is available to analysts then it is also available to hackers. The whole goal of a Pentester is to find and remove sensitive information before someone with the same abilities does the same thing but with more malicious intent. 

## Techniques used to help narrow information down 

First things first, the approach of finding everything/anything is counterproductive and useless. There is so much Open Source information to cover and it's not efficent or realistic to analyze all that volume. 

Second, identify which of the two categories the OSINT you're looking for falls in: 
1. Passive Collection 
2. Active Collection 

### Passive Collection

Involving the use of threat intelligence platforms ( TIP ) to integrate different types of threats into one accessible location. The only downside to this approach is the possiblity of threat overloading. Typically solved through AI and machine learning. The reverse malicious side to this approach is when organized threat groups use botnets to grab valuable info through traffic sniffing and keylogging. 

#### Threat Intelligence Platforms (TIPs)

Essentially a part of a security vendor software that take multiple feeds of OSINT into one single stream. Like the interface. 

### Active Collection 

This technique is the use of different search techniques for specific leads or information. 
It can be done for either one of the following reasons: 

1. An investigation needs to be conducted regaredin a potential threat that has been alerted from passive collection
2. A specific focus has been assigned, such as a particular Pentest exercise.


## OSINT Tools

### maltego Tool

maltego is a data mining tool that uses found data to create graphs in order to analyze connections. Connections between data such as, 

1. Names
2. Email Organization
3. Domains 
4. Documents

Because of this, relationships linking people such as social profiles, mutual friends, and related companies can be found.

#### Performing a Network Recon

In a simple network recon, the domain is going to be used to create a graph. Let's say we're creating a graph of instagram.com. Things you would expect to see from selecting **Run ALL Transform** include DNS Servers, related sites, related emails, email servers, even the names attached to the emails. From the names, you can click a specific person and create a graph of all of their emails. 

maltego Is a rabbit hole of information that can only be learned through usage and time consumption. 

### theHarvester Tool

Like the previous tool, theHarvester can gather emails, names, subdomains, IPs, and URLs through public sources. 

When using theHarvester tool, you have to specify not only the domain name but the data source. Meaning that it's less broad than maltego, and faster to use. A con of this tool is that it doesn't create a graph and you can't branch out without concatenating more commands to the previous. 

**sudo theharvester -d <\domain URL\> 200 -b bing**

The command above states that we are searching within 200 result of the domain instagram.com using the data source bing.

You can also conduct a DNS brute force attack using theHarvester.

**sudo theharvester -d <\domain URL\> -c -b google**

The command above states that we are conducting a DNS brute force attack on the domain instagram.com and by default using the dns-names.txt file found in /usr/share/theHarvester/.
