# SSL Analysis

It all begins with the SSL certificate. These certificates an encrypted link established by cryptographically by smaller data files. Thiis link is passed between a web server and a browser, and it's job is to ensure that the data passed through the two is to stay private. 

### Why is the SSL info used in an attack ?

**Intel Reconnaissance:** Makes it easier to extract larger data from the OSINT from the targets. 

**Attack Surface Analysis:** Blue Teams typically need to reduce the amount of possible ways network and software enviornments can be exposed to attacks through SSL certificates. If the certificates aren't in place, or leave the network or software vulnerable, it's important to know. 

**SSL Expiration Monitoring:** Monitor whether or not the SSL Certificates have been expired and the data tunnel unencrypted. 

## ssldump

The SSL/TSL network protocol analyzer, ssldump, can identify SSL/TSL traffic then decodes the traffic records and then shows them in standard output as text. IF the private key is provided ssldump can also decrypt connections and then show the application data traffic. 

For the best results, using the tcpdump to capture traffic and then decoding it with ssldump allows for the examination of traffic to be in more detail. 

#### Capturing the target traffic 

The following guidelines should be observed when capturing conversations with tcpdump:

1. Close all existing browser tabs and open a brand new one to ensure a new session key is being used. 
    This is due to ssldump not being able to decrypt traffic in which the handshake and the key exchange were not seen. 

2. The **-w** option is used to capture the packets examined into a given file. 

3. The **-i** option is to specify the interface / VLAN where the traffic is going to be captured. 

4. Use the **-s** option to capture the entire packet by specifying a value of 0 or the max size of a target packet for decrypting and examining the application data.

tcpdump -vvv -s 0 -nni external -w /var/tmp/www-ssl-client.cap host 10.1.1.100 and port 443
The command above examines the client side SSL traffic specific to a certain virtual server. 
tcpdump -vvv -s 0 -nni internal -w /var/tmp/www-ssl-server.cap host 192.168.22.33 and net 10.1.1.0/24 and port 8080

The command above is the server-side SSL traffic from one client to any other member. 

-vvv Maximum verbosity
-s Snaplength (0 captures full packets)
-nn Do not resolve host or service names
-i Interface - can be ifname or vlan name
-w Write output to file

#### Examination of the SSL Handshake / Record Messages 

The SSL connections that are established use a SSL Handshke methof that:

1. Negotiates security capabilities between the client and server(public key algorithm, symmetric key algorithm, compression algorithms) 

2. The certificate is then trasmitted from the server to the client, of which the latter must validate the identity of the server. And Vice Versa

3. Session Key Information is exchanged


Messages between these handshake transactions canbe viewed through the **ssldump -r** option which then requires an argument of the tcpdump capture file made previously. 

More useful options: 

-n Do not resolve host names.
-A Print all fields (ssldump, by default, prints only the most interesting).
-e Print absolute timestamps.
-d Display application data, including traffic before session initiates.
-M Output a pre-master secret log file (v. 11.2.0 and later)
ssldump -nr /var/tmp/www-ssl-client.cap
#### The Examination of the decrypted application data

##### Usage of Symmetric Pre-master secret keys

**ssldump -M** allows for the creation of a premaster secret key log file. It can be used to decrypt application data without access to the server's private key. This will only decrypt the data and not display it. 

The strategy for this is: 
Log in to the BIG-IP command line.
Capture the packet trace containing the SSL traffic (refer to the Capturing the target traffic section).

ssldump -r /path/to/capture_file -k /path/to/private_key -M /path/to/pre-master-key_log_file
After this is done the capture file and the PMS log file can be loaded into Wireshark. 

##### Usage of asymmetric key 

To fully read in the data, **-k** option specifies the path and name of the file that contains the private key. 
ssldump -Aed -nr /var/tmp/www-ssl-client.cap -k /config/ssl/ssl.key/www-ssl.key
## sslh

This tool serves as a multiplexer by allowing multiple programs to run on port 443. That way SSL and SSH can be used at the same time. Comes in handy when most ports are blocked by firewalls and access to the remote server is needed. 
ssh -p 443 sk@192.168.225.50
## sslscan 

sslscan is a rapid SSL port scanner that determines the supported and preferred ciphers as well as which SSL protocols are supported. After the scan sslscan returns the SSL Certificate. 
sslscan [Options] [host:port | host]

## sslyze

sslyze is a faster and more powerful version of the sslscan. 

It includes: 

1. Multi-processed and multi-threaded scanning
2. SSL 2.0/3.0 and TLS 1.0/1.1/1.2 compatibility 
3. Performance testing: session resumption and TLS tickets support
4. Security testing: weak cipher suites, insecure renegotiation, CRIME, Heartbleed and more 
5. Server certificate validation and revocation checking through OCSP stapling 
6. Support for StartTLS handshakes on SMTP, XMPP, LDAP, POP, IMAP, RDP and FTP 
7. Support for client certificates when scanning servers that perform mutual authentication XML output to further process the    scan results

sslyze –-regular www.yahoo.com