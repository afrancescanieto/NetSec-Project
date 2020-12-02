# SMB Analysis

Server Message Block (SMB) is known to be an intimedating protocol due to the huge size, sparse documentation, and wide variety of uses. It is commonly used for file and printer sharing services. It can also handle the shared services inbetween serial ports and different types of communication throughout nodes on the network. Since this protocol contains many capabilities and commonly a low security infrastructure, it makes it incredibly suseptible to attacks. 

## Enum4linux tool 

The enum4linux tool is an older tool that enumerates informaion from Windows and Samba systems. A benefit of using enum4linux is the ability to quickly dump data from servers with a NULL session enabled. Meaning the SMB data is collected with an anonymous connetion. 
Useful functions in the Enum4linux tool for information gathering include,

1. User Listing or RID cycling
2. Group membership information
3. Detection of host's workgroup or domain
4. Detecting the remote operating system
5. Password policy retrieval


**sudo enum4linux -a <\IP address\>**

The command above gives the information of enumerating all the remote hosts. 

## nbtscan Tool

This tool is useful when looking for specific NetBIOS name information. The difference between the nbtscan and the netstat tool being that nbtscan operates on a range of addresses instead of just only one. In Pentesting this can be useful in finding the remote machine names. 

**nbtscan -v <\IP_address\>**

The above command outputs a verbose version of the NetBIOS information. 

## smbmap Tool

Compared to the other two, smbmap is more specific in what it allows the users to enumerate. 
Some information the smbmap tool will list includes,

1. Share Drives
2. Drive Permissions
3. The share contents
4. It has an upload and download functionality 
5. Auto-downloads file names with matching patterns 
6. Executes remote commands



**smbmap -H <\IP_address\>**

The command above looks for ports used by the SMB service.

**smbmap -H <\IP_address\> -r <\disk name\>**

The command above lists the contents in the disk chosen if it has read and write permissions. 
