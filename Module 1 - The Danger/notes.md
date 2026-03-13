# Module 1: The Danger

## Module Objective
Explain why networks and data are attacked.

## 1.0 Introduction

### 1.0.1 First Time in This Course
CyberOps Associate v1.0 covers knowledge and skills needed to successfully handle the tasks, duties, and responsibilities of an associate-level Security Analyst working in a Security Operations Center (SOC).

Upon completion of the CyberOps Associate v1.0 course, students will be able to:

- Install virtual machines to create a safe environment for implementing and analyzing cybersecurity threat events.
- Explain the role of the Cybersecurity Operations Analyst in the enterprise.
- Explain the Windows Operating System features and characteristics needed to support cybersecurity analyses.
- Explain the features and characteristics of the Linux Operating System.
- Analyze the operation of network protocols and services.
- Explain the operation of the network infrastructure.
- Classify the various types of network attacks.
- Use network monitoring tools to identify attacks against network protocols and services.
- Explain how to prevent malicious access to computer networks, hosts, and data.
- Explain the impacts of cryptography on network security monitoring.
- Explain how to investigate endpoint vulnerabilities and attacks.
- Evaluate network security alerts.
- Analyze network intrusion data to identify compromised hosts and vulnerabilities.
- Apply incident response models to manage network security incidents.

### 1.0.2 Ethical Hacking Statement
The Cisco Networking Academy Program is focused on creating the global problem solvers needed to build, scale, secure, and defend the networks that are used in our businesses and daily lives. The need for well-trained cybersecurity specialists continues to grow at an exponential rate. Training to become a cybersecurity specialist requires in-depth understanding and exposure to how cyber attacks occur, as well as how they are detected and prevented. These skills will naturally also include learning the techniques that threat actors use to circumvent data, privacy, and computer and network security.

In this course, learners use tools and techniques in a "sandboxed" virtual machine environment that allows them to create, implement, monitor, and detect various types of cyber attacks. The hands-on training is performed in this environment so that students can gain the necessary skills and knowledge needed to thwart these and future cyber attacks. Security holes and vulnerabilities that are created in this course should only be used in an ethical manner and only in this "sandboxed" virtual environment. Experimentation with these tools, techniques, and resources outside of the provided sandboxed virtual environment is at the discretion of the instructor and local institution. If the learner has any doubt about which computer systems and networks are part of the sandboxed virtual environment, they should contact their instructor prior to any experimentation.

Unauthorized access to data, computer, and network systems is a crime in many jurisdictions and often is accompanied by severe consequences, regardless of the perpetrator's motivations. It is the learner's responsibility, as the user of this material, to be cognizant of and compliant with computer use laws.

### 1.0.3 Download Cisco Packet Tracer
To obtain and install Cisco Packet Tracer, follow the instructions below:

- https://www.netacad.com/resources/lab-downloads

### 1.0.4 Why Should I Take This Module?
Have you ever had something stolen? Perhaps you have had a wallet stolen or had your house robbed. Not only do you need to protect your physical property, you need to protect your information. Who is stealing information and why are they doing it? Maybe it is an individual just seeing if they are able to hack the information. Often it is for financial gain. There are many reasons. Keep reading this module to find out more about the threats and threat actors responsible for these attacks.

### 1.0.5 What Will I Learn in This Module?
- Module Title: The Danger
- Module Objective: Explain why networks and data are attacked.

| Topic Section | Topic Title | Topic Objective |
| --- | --- | --- |
| 1.1 | War Stories | Explain how vulnerabilities in people, organizations, and nations are exploited by attackers. |
| 1.2 | Threat Actors | Differentiate threat actor types and their motivations, including script kiddies, hacktivists, organized crime, and nation-state groups. |
| 1.3 | Threat Impact | Explain how cyberattacks affect privacy, business operations, competitive advantage, and national security. |
| 1.4 | The Danger Summary | Review key module concepts on attacks, attackers, and impact. |

### 1.0.6 Class Activity - Top Hacker Shows Us How It's Done
In this class activity, you will view a TED Talk video that discusses various security vulnerabilities. You will also research one of the vulnerabilities mentioned in the video.

#### Part 2 Response: Remote Car Unlock Key Fob Exploit
Chosen hack (from the video):
Driving through a parking lot clicking a key fob until it opens a nearby car of the same make — or, in the more advanced version, manipulating the key so it opens every car from one manufacturer.

a. What is the vulnerability being exploited?
Some car manufacturers use weak or shared key codes in their remote entry systems. In certain models the same code works across multiple vehicles, and in at least one case a researcher was able to manipulate the key so it opened every car from that manufacturer. The core problem is that the keyless entry system does not use strong, unique cryptography per vehicle.

b. What information, data, or control can be gained by a hacker exploiting this vulnerability?
The attacker gains full physical access to the car without any visible sign of a break-in. They can steal valuables, personal documents, or items stored inside. Because there is no forced entry, most insurance companies will not cover the loss. In a worst case the attacker could also take the car itself.

c. How is the hack performed?
The attacker drives or walks through a parking lot repeatedly pressing a cloned or modified fob. When the car responds, it unlocks silently. In the more sophisticated version the researcher reverse-engineered the key protocol for a particular manufacturer and produced a single key that could open any vehicle from that brand.

d. What about this particular hack interested me specifically?
What caught my attention is how invisible it is. There is no smashed window, no alarm, no evidence — just a locked car that was briefly unlocked and re-locked. It also made me think about how much trust we place in small everyday devices like key fobs without ever questioning their security.

e. How do you think this particular hack could be mitigated?
- Manufacturers should use strong per-vehicle cryptography with true rolling codes that cannot be replayed or predicted.
- Independent security researchers should test remote entry systems before vehicles go on sale.
- Firmware update mechanisms should exist so vulnerabilities can be patched after release.
- As a car owner: avoid leaving valuables in your vehicle, use a physical steering wheel lock as a second layer, and park in monitored areas when possible.

## 1.1 War Stories

### 1.1.1 Hijacked People
Sarah stopped by her favorite coffee shop to grab her afternoon drink. She placed her order, paid the clerk, and waited while the baristas worked furiously to fulfill the backup of orders. Sarah pulled out her phone, opened the wireless client, and connected to what she assumed was the coffee shop's free wireless network.

However, sitting in a corner of the store, a hacker had just set up an open rogue wireless hotspot posing as the coffee shop's wireless network. When Sarah logged onto her bank's website, the hacker hijacked her session and gained access to her bank accounts. Another term for rogue wireless hotspots is evil twin hotspots.

Search the internet for "evil twin hotspots" to learn more about this security threat.

### 1.1.2 Ransomed Companies
Rashid, an employee in the finance department of a major publicly held corporation, receives an email from his CEO with an attached PDF. The PDF is about the company's third quarter earnings. Rashid does not remember his department creating the PDF. His curiosity is piqued, so he opens the attachment.

The same scenario plays out across the organization as dozens of other employees are successfully enticed to click the attachment. When the PDF opens, ransomware is installed on the employees' computers and begins the process of gathering and encrypting corporate data. The goal of the attackers is financial gain, because they hold the company's data for ransom until they are paid.

### 1.1.3 Targeted Nations
Some of today's malware is so sophisticated and expensive to create that security experts believe only a nation-state or group of nations could possibly have the influence and funding to create it. Such malware can be targeted to attack a nation's vulnerable infrastructure, such as the water system or power grid.

This was the purpose of the Stuxnet worm, which infected USB drives. These drives were carried by five Iranian component vendors into a secure facility that they supported. Stuxnet was designed to infiltrate Windows operating systems and then target Step 7 software. Step 7 was developed by Siemens for their programmable logic controllers (PLCs). Stuxnet was looking for a specific model of Siemens PLCs that controls the centrifuges in uranium processing facilities. The worm was transmitted from the infected USB drives into the PLCs and eventually damaged many of these centrifuges.

Zero Days, a film released in 2016, documents what is known about the development and deployment of the Stuxnet targeted malware attack. Search for Zero Days to find the film or information about the film.

### 1.1.4 Video - Anatomy of an Attack
Watch this video to view details of a complex attack.

### 1.1.5 Lab - Installing the Virtual Machines
In this lab, you will install VirtualBox on your personal computer. You will then download and install the CyberOps Workstation Virtual Machine (VM).

CyberOps Workstation VM:
- MD5 Checksum: 6a70f156715f85c09fbb859c80c4b6c5
- SHA512 Checksum: 2cc44d6585001d99bce5dfc19ed5ef920714ca03

Security Onion VM:
- MD5 Checksum: 8d65135641b9c94e788909026805ad6b
- SHA512 Checksum: aaca24b0036be5d61dd42a0b3503403e18ae0e12

Lab answers:
- Applications in the CyberOps menu: Analyst's Home, Wireshark, Firefox Web Browser, Terminal, Keyboard, and DPI Scaling.
- IP addresses assigned to the virtual machine: `127.0.0.1/8` on the loopback interface, `10.0.2.15/24` on `enp0s3`, `fd17:625c:f037:2:a00:27ff:fea0:548a/64` as the global IPv6 address, and `fe80::a00:27ff:fea0:548a/64` as the link-local IPv6 address.
- Browser test: Yes, the browser was able to open a search engine successfully.
- Reflection: A virtual machine is useful because it gives me a safe, isolated environment where I can practice cybersecurity tasks without risking my main computer. It also makes it easier to test tools, run a different operating system, and reset the system if something goes wrong. The disadvantages are that virtual machines need a lot of disk space, RAM, and CPU resources, they can run slower than a physical machine, and setup or compatibility problems can sometimes make labs harder to complete.

### 1.1.6 Lab - Cybersecurity Case Studies
In this lab, you will analyze the given cases and answer questions about them.

## 1.2 Threat Actors

### 1.2.1 Threat Actors
Threat actors include, but are not limited to, amateurs, hacktivists, organized crime groups, state-sponsored groups, and terrorist groups. Threat actors are individuals or groups of individuals who perform cyberattacks. Cyberattacks are intentional malicious acts meant to negatively impact another individual or organization.

Common categories and motivations include:
- Amateurs
- Hacktivists
- Financial gain actors
- Trade secrets and geopolitical actors

Amateurs, also known as script kiddies, have little or no skill. They often use existing tools or instructions found on the internet to launch attacks. Some are just curious, while others try to demonstrate their skills by causing harm. Even though they are using basic tools, the results can still be devastating.

Hacktivists are hackers who protest against a variety of political and social ideas. Hacktivists publicly protest against organizations or governments by posting articles and videos, leaking sensitive information, and disrupting web services with illegitimate traffic in distributed denial of service (DDoS) attacks.

Much of the hacking activity that consistently threatens our security is motivated by financial gain. These cybercriminals want to gain access to our bank accounts, personal data, and anything else they can leverage to generate cash flow.

In the past several years, we have heard many stories about nation states hacking other countries, or otherwise interfering with internal politics. Nation states are also interested in using cyberspace for industrial espionage. The theft of intellectual property can give a country a significant advantage in international trade.

Defending against the fallout from state-sponsored cyberespionage and cyberwarfare will continue to be a priority for cybersecurity professionals.

### 1.2.2 How Secure Is the Internet of Things?
The Internet of Things (IoT) is all around us and quickly expanding. We are just beginning to reap the benefits of the IoT. New ways to use connected things are being developed daily. The IoT helps individuals connect things to improve their quality of life. For example, many people are now using connected wearable devices to track their fitness activities.

How secure are these devices? For example:
- Who wrote the firmware?
- Did the programmer pay attention to security flaws?
- Is your connected home thermostat vulnerable to attacks?
- What about your DVR?
- If vulnerabilities are found, can firmware be patched?

Many devices on the internet are not updated with the latest firmware. Some older devices were not even developed to be updated with patches. These situations create opportunity for threat actors and risk for device owners.

In October 2016, a DDoS attack against the domain name provider Dyn took down many popular websites. The attack came from a large number of webcams, DVRs, routers, and other IoT devices that had been compromised by malicious software. These devices formed a botnet controlled by hackers. This botnet was used to create an enormous DDoS attack that disabled essential internet services.

Search for:
- "Dyn Analysis Summary of Friday October 21 Attack"
- Avi Rubin TED talk: "All Your Devices can be Hacked"

### 1.2.3 Lab - Learning the Details of Attacks
In this lab, you will research and analyze IoT application vulnerabilities.

## 1.3 Threat Impact

### 1.3.1 PII, PHI, and PSI
The economic impact of cyberattacks is difficult to determine with precision. However, it is estimated that businesses will lose over $5 trillion annually by 2024 due to cyberattacks.

Personally identifiable information (PII) is any information that can be used to positively identify an individual. Examples include:

- Name
- Social security number
- Birthdate
- Credit card numbers
- Bank account numbers
- Government-issued ID
- Address information (street, email, phone numbers)

One of the more lucrative goals of cybercriminals is obtaining lists of PII that can then be sold on the dark web. Stolen PII can be used to create fake financial accounts, such as credit cards and short-term loans.

A subset of PII is protected health information (PHI). The medical community creates and maintains electronic medical records (EMRs) that contain PHI. In the U.S., handling of PHI is regulated by HIPAA. In the European Union, GDPR protects a broad range of personal information, including health records.

Personal security information (PSI) is another type of PII. This includes usernames, passwords, and other security-related information used to access network services. According to a 2019 Verizon report, the second most common way threat actors breached a network was by using stolen PSI.

Recent examples of major PII/PHI breaches:

- In 2019, an online graphic design platform had a breach where PII for approximately 137 million users was viewed by hackers, with details for 4 million accounts appearing on the internet.
- In 2020, a major Chinese social media company was hacked, resulting in theft of PII (including phone numbers) from 172 million users.
- In 2019, a company that makes games played on Facebook was hacked and the PII of 218 million users was stolen.

### 1.3.2 Lost Competitive Advantage
Companies are increasingly worried about corporate espionage in cyberspace. The loss of intellectual property to competitors is a serious concern. An additional major concern is the loss of trust that comes when a company is unable to protect its customers' personal data. The loss of competitive advantage may come from this loss of trust rather than from another company or country stealing trade secrets.

### 1.3.3 Politics and National Security
It is not just businesses that get hacked. In February 2016, a hacker published the personal information of 20,000 U.S. Federal Bureau of Investigation (FBI) employees and 9,000 U.S. Department of Homeland Security (DHS) employees. The hacker was apparently politically motivated.

The Stuxnet worm was specifically designed to impede Iran's progress in enriching uranium that could be used in a nuclear weapon. Stuxnet is a prime example of a network attack motivated by national security concerns. Cyberwarfare is a serious possibility. State-supported hacker groups can cause disruption and destruction of vital services and resources within an enemy nation.

The internet has become essential as a medium for commercial and financial activities. Disruption of these activities can devastate a nation's economy. Controllers similar to those attacked by Stuxnet are also used to control water flow at dams and switching on electrical power grids. Attacks on such controllers can have dire consequences.

### 1.3.4 Lab - Visualizing the Black Hats
In this lab, you will research and analyze cybersecurity incidents to create scenarios for how organizations can prevent or mitigate an attack.

## 1.4 The Danger Summary
This section recaps key points from the module, including:

- War stories and real-world attack examples
- Threat actor types and motivations
- Threat impact areas such as PII theft, economic losses, and national security risks
