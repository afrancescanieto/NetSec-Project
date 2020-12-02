# Reporting

Onto the final phase of the pentesting journey, reporting. As it states, reporting is to communicate to a higher up, what was done, how it was done and most importantly how the organization should fix the vulnerabilites discovered. Since an attacker's point of view is taboo and rarely seen, it's imperative to the organization that they understand the information security infrastructure they currently have and how it can be excessively improved to preven actual malicious attacks from happening. 

The report is composed of a minimum of eight parts including, 

1. A Cover Sheet
2. The Executive Summary 
3. Summary of Vulnerablities 
4. Test Team Details 
5. List of Tools Used 
6. A Copy of the Original Scope of Work 
7. The Main Body of the Report
8. Final Delivery 

## The Cover Sheet 

The cover sheet are the formalities of the professional report. It includes, 

1. A logo of the testing company 
2. The name of the client
3. Any titles of the test performed 
    - Ex: "DMZ test" 
    - Avoids Confusion in case several test are being performed for the same client
4. The date range the tests were perform 
    - Helps the security auditor make a judgement whether or not tests are improving or getting worse over time. 
5. The document's classification
    - The client should be questioned on how they want their document's classified 
    - Most Reports are Commercially Sensitive Documents

## The Executive Summary 

Despite popular belief the Executive Summary does not have to be a written telenovela. Maximum the summary should be less than a page long. Specific tools or technologies and techniques aren't mentioned, because they do not care. They want the TL;DR, with the general gist being ; 

1. **What was done:**
" We performed a penatration test of servers that belong to XXX application. " 

2. **What happened:**
" We found security problems in one of the payment servers." 

3. **What needs to be done about it and why:** 
" You should tell someone to fix these problems and then get us to re-test the payment server, if not you won't be PCI compliant and will get a fine." 

4. **The last line of the summary shouls always spell out whether the systems that were tested are secure or not:**
" Overall the system has been found to be insecure" 

Do not leave room for doubt, be assertive and confident in the conclusion of the summary. 



## Summary of Vulnerabilites 

The vulnerabilites should be grouped onto a single page, so that the IT manager can **glance** at it and understand the work that needs to be done. Fancy graphics like tables and charts are encouraged to make it simpler, but no overdoing it! This isn't a first grade vision board. 

Vulnerabilities are best grouped by category, severity, or CVSS score. 

Catagories can include: 

1. Software issue
2. Network Device Configuration 
3. Password Policy 

## Test Team Details 

The name of every tester involved in the testing process needs to be recorded. This is for the client to be able to know who exactly has been on their network and have contacts available to discuss the report with. 

## List of Tools Used 

This sections includes versions and a small description of the function used. This allows for repeatability, meaning that if somone wants to replicate the test they will have the available tools exactly how they were used. 

## A Copy of the Original Scope of Work 

This will mainly been in agreement in advance.

## The Main Body of the Report

The meat and bones. The main body should include, 

1. Details of the detected vulnerabilities 
2. How the vulnerablities were detected
3. Clearly stated explanations of how the vulnerabilities could be exploited
4. The probablity of the exploitation 

The biggest problem encountered with the main body in many pentester's report are the lack of explanations. Just the same as commenting code when developing software, scanner output should be explained not just copy and pasted.

The explanation of the remedial advice should also be exapolated. The exact steps as to why and how to fix a problem should be listed. 

The best advice when writing a report is to speak with the client directly and infer or ask how detailed or how general they would want it, learn who the audience is. 

# Final Delivery 

This is the most important part of the report. Imagine being a pentester and sending out all the weaknesses of a company's security infrastructure unencrypted. 

When sending out the report to a client, electronic distribution using a public key cryptography is the best option. If not possible, symmetric enryption can be used with a strong key and must be transmitted out of band. 

A sample report from Offensive Security can be found here: https://www.offensive-security.com/reports/sample-penetration-testing-report.pdf
