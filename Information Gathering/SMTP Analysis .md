# SMTP Analysis 

SMTP is the protocol in charge of sending and recieving electionic mail transmisions. Each message sent through the Simple Mail Transfer Protocol (SMTP) contains both control information such as envelopes and headers and the data needing to be transfered.This is important because within the headers there is a recipient header. All of the control information contained in the SMTP message is only available in the recipient's storage, UNLESS the message is a mailing list in which they are considered public and makes for a perfect opportunity for exploitation.  

### Building a Network Topology with SMTP 

Since SMTP headers always contain a receiver header, data can be extracted from that control. 
Data such as: 

1. IP addresses of the sending gateway 
2. The fully qualified domain name (Hostname and domain name) 
3. The transfer protocol used. (HTTP, SMTP, POP3 ) 
4. Message Transfer Agent server software
5. The timestamp of when it sent 

So how does this benefit an attacker/pentester? 

They can,

1. Find out the corporate IP Subnetting: such as internal IP addresses scheme, static or dynamic connection to corporate locations.

2. Find the Corporate SMTP gateway policies: are corporate locations using the same one , or is it a every one for themselves?

3. Find the general whereabouts of the gateway through the timezone on the timestamp 

4. Find the software and versions used by the server

5. Check whether relay links are being encrypted or not and which type of encryption they are using 

6. Whether or not email tracing is being used, it becomes suspicious if one email is going through a totally different server. 


### A Possible Psuedo Attack Plan 

After gathering all that information what's the goto to see the full picture? 

1. Plot an SMTP connectivity graph 
2. What nodes are the most common in a larger part of the traffic?
3. Take into consideration the server software and releases. Pros? Cons? 

## SWAKS 

SWAKS is used as an email tester. It lets you customize and alter any part of the email. The server it speaks to, the control information, attachments etc. 

### Basic Example: 
 swaks -f someone@example.net -t liquidat@example.com
### Testing User Authentication 
 swaks -tls --server example.com -f liquidat@example.com -t someone@example.net  -ao --auth-user=liquidat
### Testing authentication between servers
 swaks -tls -s example.com -f someone@example.net -t liquidat@example.com --ehlo $(host $(wget http://automation.whatismyip.com/n09230945.asp -O - -q))