#!/usr/bin/env python
# coding: utf-8

# # Wireless Attacks 

# The aim of a wireless attack is to capture information sent across the network and intrude with the network traffic. There are four main attacks, 
# 
# 1. Packet Sniffing ( Discussed in another section ) 
# 2. Rogue Access Points 
# 3. Jamming 
# 4. Evil Twinning 

# ### Rogue Access Points

# A Rogue AP is any access point that is unauthorized on a network. These access points make the entire network suseptible to DDoS attacks, packet captures, and ARP poisoning. 

# ### Jamming

# Creating wireless interference within a network causes other mehthods of wireless attacks to become more accesible. Bluetooth devices, a microwave oven, or a cordless phone are small factors that can cause this interference to happen. 

# ### Evil Twinning

# By configuring a wireless access point exactly as the target existing network, attackers can take a Mr. Hyde form. The attacker's access point is indistinguishable from the actual access points. 

# ## 802.11 Wireless Tools

# ### bully 

# A Wi-Fi protected Setup (WPS) allows users to configure devices in a network without needing to type in a passphrase, rather just a small PIN. This makes brute force attacks perfect to exploit that vulnerability. Bully is the tool to use for this scenario. 
bully mon0 -b 00:25:9C:97:4F:48 -e Mandela2 -c 9
# 1. **mon0** is the name of the wireless adapter in monitor mode.
# 
# 2. **--b 00:25:9C:97:4F:48** is the BSSID of the vulnerable AP.
# 
# 3. **-e Mandela2** is the SSID of the AP.
# 
# 4. **-c 9**  is the channel the AP is broadcasting on.

# bully can also be used to gain informationfor the offline pixiewps tool. 

# ### aircrack-ng

# Aircrack-ng is special through its method of containing tools that aid the processes of detection, packet sniffing, and password cracking
# 
# It contains tools such as, 
# 
# 1. Airmon-ng
# 2. Airodump-ng
# 3. Aireplay-ng
# 4. Airbase-ng

# ##### Airmon-ng 

# A script that puts a network interface card into monitor mode, thus allowing the capturing of packets to be available without authenication or a connection to an access point. 
airmon-ng start <interface name>
# The command above will concatenate the interface name with "mon" to inform that the monitor mode has been enabled. 

# ##### Airodump-ng

# Captures and saves raw data packets after monitor mode has been enabled. 
airodump-ng <interface name> # the new interface name with the monitor mode enabled. 
# The command above displayes all the access points and their MAC addresses. 

# ##### Aireplay-ng 

# Aireplay can capture traffic from a live network or use packets from an existing Pcap file to inject into network, thus creating artificial traffic. 

# ##### Aircrack-ng 

# Aircrack is then run to brute force the WEP/WPA key. 

# ## Bluetooth Tools

# ### spooftooph

# Abilities that spooftooph contains: 
# 
# 1. Clone and log Bluetooth device information
# 
# 2. Generate a random new Bluetooth profile
# 
# 3. Change Bluetooth profile every X seconds
# 
# 4. Specify device information for Bluetooth interface
# 
# 5. Select device to clone from scan log
spooftooph -i <interface> -s -d scan.log
# The command above: 
# 
# 1. Scans a local area for devices 
# 2. Saves the list of devices found 
spooftooph -i <interface> -r
# The command above randomly generates a bluetooth profile. 
spooftooph -i <interface > -t 10 
# The command above scans for devices every 10 seconds and clones the first profile on the list. 