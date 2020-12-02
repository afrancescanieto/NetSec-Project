# Forensics

Digital forensics in Cyber Security are essentially the front lines in mitigating cybercrime, they collect, process, perserve, and analyze computer-related evidence. 

Forensics is not typically used in Pentesting, but the information on how it works is beneficial to further understand the mechanics of hacking. 

## Forensic Carving Tools

When using forensic carving tools, the main concept to understand is file carving. In computer forensics, File carving is a process that extracts data from a disk drive/other storage device without having to use the original file system on which the file was created. 

### scalpel 

This tool reads a database of header and footer definitions, then extracts matching files from a set of image or raw device files. 

**scalpel /dev/sda1 -o output **

In the command above, **-o** defines the directory *output* where scalpel will place the recovered files. 

**ls -la** # view the output directory

**ls -l output** # open the recovered files

**cat output/audit.txt** # summary of what the scalpel tool has achieved 

**Before running Scalpel from the same directory, the existing content inside of it has to be deleted.**

## Forensic Imaging 

A forensic image is a duplicate of an electronic media, like a hard-disk drive. 

### guymager

This tool is an open-source GUI application that is used to create disk images. 

Guymager suppports,

1. Raw dd images
2. EO1
3. AFF 

## PDF Forensics Tools 

### pdf-parser

The pdf-parser the fundemental elements used in the file analyzed. 

Fundemental elements include;

1. Header 
2. A list of Objects
3. A cross reference table
4. Trailer

### pdfid

This tool will scan a file to look for certain PDF key words. It is recommended to scan a PDF file with pdfid then use pdf-parser to analyze the file.


pdfid will scan a PDF for these stirings and count the occurences: 

1. obj
2. endobj
3. stream
4. endstream
5. xref
6. trailer
7. startxref
8. /Page
9. /Encrypt
10. /ObjStm
11. /JS
12. /JavaScript
13. /AA
14. /OpenAction
15. /JBIG2Decode
16. /RichMedia
17. /Launch
18. /XFA

## Sleuth Kit Suite

### autopsy 

Autopsy is a GUI that is used by military and law enforcement to retrieve evidence from a physical drive. 

http://localhost:9999/autopsy

Pasting that URL into a web browser after starting up autopsy shows the home page of the tool. 

More on how to use the slueth kit autopsy: https://linuxhint.com/sleuth_kit_autopsy/
