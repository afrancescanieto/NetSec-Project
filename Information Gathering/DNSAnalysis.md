# DNS Analysis

First question we must ask ourselves is why do we need to use DNS Analysis? DNS Analysis allows us to get as much information possible on the DNS servers/records. With that information we can then see what part of the network isn’t alerting the IPS/IDS of possible vulnerable DNS traffic.  A common problem is that most of the monitoring is going on in the Zone Transfers.

## Using dnsrecon

In the standard enumeration when using dnsrecon you can identify whether or not the domain is using DNSSec, you can find the SOA record, the mail servers, the IP ranges that the company is using, what servers can send emails (SPF), as well as the SRV services. 

**dnsrecon -d <\domain URL\>**

There are 7 types of enumeration in this command that can help get information: 
  1. Zone Transfer
  2. Reverse Lookup 
  3. Domain and Host Brute-Force 
  4. Standard Record Enumeration 
  5. Cache Snooping 
  6. Zone Walking 
  7. Google Lookup


### Zone Transfer

Using zone transfer you can find the topology of the network in a company. When a user is attempting to perform a zone transfer a DNS query is sent to list all the name servers,host names, MX and CNAME records, zone serial number etc.. in the DNS. Pretty much all the info you need. Because of this Zone Transfers are not easily accessible. Except through dnsrecon.

**dnsrecon -d <\domain URL\> -a**

### Reverse Lookup

Using the reverse lookup you can find the domain names associated to a range of IP addresses 

**dnsrecon -d  <\domain URL\> -s**

### Domain Brute Force

Using the domain brute force you can obtain A and CNAME Records and their IP Addresses

**dnsrecon -d <\domain URL\> -D namelist.txt -t brt**

### Cache Snooping

Cache snooping is when a query is preformed on a DNS Server. The snooping can only successfully occur if a particular DNS record is cached. If this is true it can be deduced that the site has been visited by it's DNS Server owner. Information such as the owner, a vendor, a bank's service provider, or any other vital information could be exploited. 

**dnsrecon -t snoop -n Sever -D namelist.txt**

There are two way to do this:

  1. Non-Recursive Queries
  2. Recursive Queries

#### The Non-Recursive Query Method

Without the recursion in the query, the query is sent for the name the snooper is interested in. As previously stated, if the name is in the server's cache it will show up. 

#### The Recursive Query Method

The snooper has to do some digging. With the power of deduction, the snooper has to find if the server responed from it's cache through the time it took for it to respond and the TTL of the answers that were displayed. 

### Zone Walking

Using this method can show internal records if the proper safety measures in the Zone were not configured. This information helps map network hosts through the enumeration of the contents inside of the Zone. 

**dnsrecon -d <\domain URL\> -t zonewalk**

### Google Lookup

Uses google to find subdomains and hosts. 

**dnsrecon -d <\domain URL\> -g -c googleiglookup.csv**

**less /usr/share/dnsrecon/googleiglookup.csv**
