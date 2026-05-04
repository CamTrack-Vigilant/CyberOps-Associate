5.0 Introduction
Scroll to begin

### 5.0.1 Why Should I Take this Module?
We all communicate on networks daily. Looking at social media, streaming video, or researching information on the internet are common activities that we normally don’t think much about. However, numerous technological processes are at work to bring us the content that we want from the web.

In this module, you will learn how network protocols work together to allow us to request information and to return that information to us over the network.

### 5.0.2 What Will I Learn in this Module?

Find the module overview image in the Content folder below:

![Module overview](./Content folder/Screenshot 2026-05-04 153009.png)

---

5.1 Network Communications Process
Scroll to begin

#### 5.1.1 Networks of Many Sizes
Networks come in all sizes. They range from simple networks that consist of two computers, to networks connecting millions of devices.

Simple home networks let you share resources, such as printers, documents, pictures, and music, among a few local end devices.

Small office and home office (SOHO) networks allow people to work from home, or a remote office. Many self-employed workers use these types of networks to advertise and sell products, order supplies, and communicate with customers.

Businesses and large organizations use networks to provide consolidation, storage, and access to information on network servers. Networks provide email, instant messaging, and collaboration among employees. Many organizations use their network’s connection to the internet to provide products and services to customers.

The internet is the largest network in existence. In fact, the term internet means a “network of networks”. It is a collection of interconnected private and public networks.

In small businesses and homes, many computers function as both the servers and clients on the network. This type of network is called a peer-to-peer network.

**Small Home Networks**

Small home networks connect a few computers to each other and to the internet.

**Small Office and Home Office Networks**

The SOHO network allows computers in a home office or a remote office to connect to a corporate network, or access centralized, shared resources.

**Medium to Large Networks**

Medium to large networks, such as those used by corporations and schools, can have many locations with hundreds or thousands of interconnected hosts.

**World Wide Networks**

The internet is a network of networks that connects hundreds of millions of computers world-wide.

---

#### 5.1.2 Client-Server Communications
All computers that are connected to a network and that participate directly in network communication are classified as hosts. Hosts are also called end devices, endpoints, or nodes. Much of the interaction between end devices is client-server traffic. For example, when you access a web page on the internet, your web browser (the client) is accessing a server. When you send an email message, your email client will connect to an email server.

Servers are simply computers with specialized software. This software enables servers to provide information to other end devices on the network. A server can be single-purpose, providing only one service, such as web pages. A server can be multipurpose, providing a variety of services such as web pages, email, and file transfers.

Client computers have software installed, such as web browsers, email clients, and file transfers applications. This software enables them to request and display the information obtained from the server. A single computer can also run multiple types of client software. For example, a user can check email and view a web page while listening to internet radio.

Examples of common servers:

- File Server - The file server stores corporate and user files in a central location.
- Web Server - The web server runs web server software that allows many computers to access web pages.
- Email Server - The email server runs email server software that enables emails to be sent and received.

Client devices access files with client software such as file explorers; browsers access web servers with browser software; mail clients access email servers with mail client software.

---

#### 5.1.3 Typical Sessions
A typical network user at school, at home, or in the office, will normally use some type of computing device to establish many connections with network servers. Those servers could be located in the same room or around the world. Below are illustrative scenarios showing how network communications occur in everyday use.

**Scenario: Terry (student, BYOD)**
Terry uses her cell phone on school Wi‑Fi to submit search queries. The device encodes the search terms into binary, sends them as radio waves to the school network, converts to electrical signals on wired segments, traverses ISP networks, and reaches the search engine’s servers which respond with results addressed back to Terry’s device.

**Scenario: Michelle (gamer)**
Michelle connects a gaming console via Ethernet to a home network that reaches the ISP by cable modem and router. Gameplay data is sent in many small packets to the game provider’s servers and responses (graphics/audio) are returned quickly to enable real‑time play.

**Scenario: Dr. Awad (medical cloud use case)**
Medical imaging (X‑rays, MRIs) is digitized and securely transmitted to cloud storage and services. Encryption and secure network services protect patient data while enabling doctors to review, collaborate, and consult remotely.

---

#### 5.1.4 Tracing the Path
Network traffic often travels through many different networks and points of presence (PoPs), across Tier 1/2/3 ISPs, Internet Exchange Points (IXP), and regional routers. Because routing policies and peering agreements vary, traffic paths can be indirect and differ between outbound and return routes.

Understanding and tracing the path of traffic is essential for cybersecurity analysts to determine true origins and destinations of network communications.

Illustration (concept): multiple clouds (Internet users → Tier 3 → Tier 2 → Tier 1, PoP, IXP) connected by routers and PoPs, showing many possible paths between source and destination.

---

#### 5.1.5 Lab - Tracing a Route
Lab activities:

1. Verify connectivity to a website (e.g., use `ping` or web browser).
2. Use `traceroute` (Linux) or `tracert` (Windows) to examine the network path to a destination host.
3. Use a web‑based traceroute tool to compare results and observe intermediate hops.

This lab helps you practice path tracing, interpreting hops, and identifying where latency or routing anomalies occur.

---

Notes and further study suggestions:

- Review how protocols at different layers (physical, data link, network, transport, application) interact during typical sessions.
- Practice using network utilities: `ping`, `traceroute`/`tracert`, `nslookup`/`dig`, and packet capture tools like Wireshark.
- Consider lab scenarios for client‑server interactions, secure data transfer (TLS), and routing behavior across ISPs.

---

## 5.2 Communications Protocols
Scroll to begin

### 5.2.1 What are Protocols?
Simply having a wired or wireless physical connection between end devices is not enough to enable communication. For communication to occur, devices must know "how" to communicate. Communication, whether by face-to-face or over a network, is governed by rules called protocols. These protocols are specific to the type of communication method occurring.

For example, consider two people communicating face-to-face. Prior to communicating, they must agree on how to communicate. If the communication is using voice, they must first agree on the language. Next, when they have a message to share, they must be able to format that message in a way that is understandable. For example, if someone uses the English language, but poor sentence structure, the message can easily be misunderstood.

Similarly, network protocols specify many features of network communication:

![Protocol characteristics](./Content%20folder/Screenshot%202026-05-05%20002626.png)

**Key protocol characteristics:**
- Message encoding
- Message formatting and encapsulation
- Message size
- Message timing
- Message delivery options

---

### 5.2.2 Network Protocols
Network protocols provide the means for computers to communicate on networks. Network protocols dictate the message encoding, formatting, encapsulation, size, timing, and delivery options. Networking protocols define a common format and set of rules for exchanging messages between devices.

Some common networking protocols are:
- **HTTP** - Hypertext Transfer Protocol
- **TCP** - Transmission Control Protocol
- **IP** - Internet Protocol

> **Note:** IP in this course refers to both the IPv4 and IPv6 protocols. IPv6 is the most recent version of IP and will eventually replace the more common IPv4.

As a cybersecurity analyst, you must be very familiar with the structure of protocol data and how the protocols function in network communications.

![Network protocols overview 1](./Content%20folder/Screenshot%202026-05-05%20003004.png)

![Network protocols overview 2](./Content%20folder/Screenshot%202026-05-05%20003134.png)

![Network protocols overview 3](./Content%20folder/Screenshot%202026-05-05%20003237.png)

![Network protocols overview 4](./Content%20folder/Screenshot%202026-05-05%20003314.png)

---

### 5.2.3 The TCP/IP Protocol Suite
Today, the TCP/IP protocol suite includes many protocols and continues to evolve to support new services.

#### Application Layer

**Name System**
- **DNS** - Domain Name System. Translates domain names such as cisco.com into IP addresses.

**Host Configuration**
- **DHCPv4** - Dynamic Host Configuration Protocol for IPv4. A DHCPv4 server dynamically assigns IPv4 addressing information to DHCPv4 clients at start-up and allows the addresses to be re-used when no longer needed.
- **DHCPv6** - Dynamic Host Configuration Protocol for IPv6. DHCPv6 is similar to DHCPv4. A DHCPv6 server dynamically assigns IPv6 addressing information to DHCPv6 clients at start-up.
- **SLAAC** - Stateless Address Autoconfiguration. A method that allows a device to obtain its IPv6 addressing information without using a DHCPv6 server.

**Email**
- **SMTP** - Simple Mail Transfer Protocol. Enables clients to send email to a mail server and enables servers to send email to other servers.
- **POP3** - Post Office Protocol version 3. Enables clients to retrieve email from a mail server and download the email to the client's local mail application.
- **IMAP** - Internet Message Access Protocol. Enables clients to access email stored on a mail server as well as maintaining email on the server.

**File Transfer**
- **FTP** - File Transfer Protocol. Sets the rules that enable a user on one host to access and transfer files to and from another host over a network. FTP is a reliable, connection-oriented, and acknowledged file delivery protocol.
- **SFTP** - SSH File Transfer Protocol. As an extension to Secure Shell (SSH) protocol, SFTP can be used to establish a secure file transfer session in which the file transfer is encrypted. SSH is a method for secure remote login that is typically used for accessing the command line of a device.
- **TFTP** - Trivial File Transfer Protocol. A simple, connectionless file transfer protocol with best-effort, unacknowledged file delivery. It uses less overhead than FTP.

**Web and Web Service**
- **HTTP** - Hypertext Transfer Protocol. A set of rules for exchanging text, graphic images, sound, video, and other multimedia files on the World Wide Web.
- **HTTPS** - HTTP Secure. A secure form of HTTP that encrypts the data that is exchanged over the World Wide Web.
- **REST** - Representational State Transfer. A web service that uses application programming interfaces (APIs) and HTTP requests to create web applications.

#### Transport Layer

**Connection-Oriented**
- **TCP** - Transmission Control Protocol. Enables reliable communication between processes running on separate hosts and provides reliable, acknowledged transmissions that confirm successful delivery.

**Connectionless**
- **UDP** - User Datagram Protocol. Enables a process running on one host to send packets to a process running on another host. However, UDP does not confirm successful datagram transmission.

#### Internet Layer

**Internet Protocol**
- **IPv4** - Internet Protocol version 4. Receives message segments from the transport layer, packages messages into packets, and addresses packets for end-to-end delivery over a network. IPv4 uses a 32-bit address.
- **IPv6** - IP version 6. Similar to IPv4 but uses a 128-bit address.
- **NAT** - Network Address Translation. Translates IPv4 addresses from a private network into globally unique public IPv4 addresses.

**Messaging**
- **ICMPv4** - Internet Control Message Protocol for IPv4. Provides feedback from a destination host to a source host about errors in packet delivery.
- **ICMPv6** - ICMP for IPv6. Similar functionality to ICMPv4 but is used for IPv6 packets.
- **ICMPv6 ND** - ICMPv6 Neighbor Discovery. Includes four protocol messages that are used for address resolution and duplicate address detection.

**Routing Protocols**
- **OSPF** - Open Shortest Path First. Link-state routing protocol that uses a hierarchical design based on areas. OSPF is an open standard interior routing protocol.
- **EIGRP** - Enhanced Interior Gateway Routing Protocol. An open standard routing protocol developed by Cisco that uses a composite metric based on bandwidth, delay, load and reliability.
- **BGP** - Border Gateway Protocol. An open standard exterior gateway routing protocol used between Internet Service Providers (ISPs). BGP is also commonly used between ISPs and their large private clients to exchange routing information.

#### Network Access Layer

**Address Resolution**
- **ARP** - Address Resolution Protocol. Provides dynamic address mapping between an IPv4 address and a hardware address.

> **Note:** You may see other documentation state that ARP operates at the Internet Layer (OSI Layer 3). However, in this course we state that ARP operates at the Network Access layer (OSI Layer 2) because its primary purpose is to discover the MAC address of the destination. A MAC address is a Layer 2 address.

**Data Link Protocols**
- **Ethernet** - Defines the rules for wiring and signaling standards of the network access layer.
- **WLAN** - Wireless Local Area Network. Defines the rules for wireless signaling across the 2.4 GHz and 5 GHz radio frequencies.

---

### 5.2.4 Message Formatting and Encapsulation
When a message is sent from source to destination, it must use a specific format or structure. Message formats depend on the type of message and the channel that is used to deliver the message.

**Analogy: Letter Formatting**

A common example of requiring the correct format in human communications is when sending a letter. An envelope has the address of the sender and receiver, each located at the proper place on the envelope. If the destination address and formatting are not correct, the letter is not delivered.

The process of placing one message format (the letter) inside another message format (the envelope) is called **encapsulation**. **De-encapsulation** occurs when the process is reversed by the recipient and the letter is removed from the envelope.

![Message formatting and encapsulation](./Content%20folder/Screenshot%202026-05-05%20004108.png)

---

### 5.2.5 Message Size
Another rule of communication is message size.

**Analogy: Face-to-Face Communication**

When people communicate with each other, the messages that they send are usually broken into smaller parts or sentences. These sentences are limited in size to what the receiving person can process at one time. It also makes it easier for the receiver to read and comprehend.

**Network Message Size**

Likewise, when a long message is sent from one host to another over a network, it is necessary to break the message into smaller pieces. The rules that govern the size of the pieces, or frames, communicated across the network are very strict. They can also be different, depending on the channel used. Frames that are too long or too short are not delivered.

The size restrictions of frames require the source host to break a long message into individual pieces that meet both the minimum and maximum size requirements. The long message will be sent in separate frames, with each frame containing a piece of the original message. Each frame will also have its own addressing information. At the receiving host, the individual pieces of the message are reconstructed into the original message.

---

### 5.2.6 Message Timing
Message timing is also very important in network communications. Message timing includes the following:

**Flow Control** - This is the process of managing the rate of data transmission. Flow control defines how much information can be sent and the speed at which it can be delivered. For example, if one person speaks too quickly, it may be difficult for the receiver to hear and understand the message. In network communication, there are network protocols used by the source and destination devices to negotiate and manage the flow of information.

**Response Timeout** - If a person asks a question and does not hear a response within an acceptable amount of time, the person assumes that no answer is coming and reacts accordingly. The person may repeat the question or instead, may go on with the conversation. Hosts on the network use network protocols that specify how long to wait for responses and what action to take if a response timeout occurs.

**Access Method** - This determines when someone can send a message. When a device wants to transmit on a wireless LAN, it is necessary for the WLAN network interface card (NIC) to determine whether the wireless medium is available. A collision of information occurs when two devices try to send at the same time, and it is necessary for the two to back off and start again.

---

### 5.2.7 Unicast, Multicast, and Broadcast
A message can be delivered in different ways. Sometimes, a person wants to communicate information to a single individual. At other times, the person may need to send information to a group of people at the same time, or even to all people in the same area.

Hosts on a network use similar delivery options to communicate. These methods of communication are called unicast, multicast, and broadcast.

**Unicast**
- A one-to-one delivery option referred to as unicast, meaning there is only a single destination for the message.

**Multicast**
- When a host needs to send messages using a one-to-many delivery option, it is referred to as multicast.

**Broadcast**
- If all hosts on the network need to receive the message at the same time, a broadcast may be used. Broadcasting represents a one-to-all message delivery option.

---

### 5.2.8 The Benefits of Using a Layered Model
You cannot actually watch real packets travel across a real network the way you can watch the components of a car being put together on an assembly line. So, it helps to have a way of thinking about a network so that you can imagine what is happening. A model is useful in these situations.

Complex concepts such as how a network operates can be difficult to explain and understand. For this reason, a layered model is used to modularize the operations of a network into manageable layers.

**Benefits of Using a Layered Model:**

- Assisting in protocol design because protocols that operate at a specific layer have defined information that they act upon and a defined interface to the layers above and below
- Fostering competition because products from different vendors can work together
- Preventing technology or capability changes in one layer from affecting other layers above and below
- Providing a common language to describe networking functions and capabilities

**Two Layered Models:**
1. **Open System Interconnection (OSI) Reference Model**
2. **TCP/IP Reference Model**

![Layered models comparison](./Content%20folder/Screenshot%202026-05-05%20004837.png)

---

### 5.2.9 The OSI Reference Model
The OSI reference model provides an extensive list of functions and services that can occur at each layer. This type of model provides consistency within all types of network protocols and services by describing what must be done at a particular layer, but not prescribing how it should be accomplished.

It also describes the interaction of each layer with the layers directly above and below. The TCP/IP protocols discussed in this course are structured around both the OSI and TCP/IP models.

![OSI Reference Model details 1](./Content%20folder/Screenshot%202026-05-05%20005020.png)

![OSI Reference Model details 2](./Content%20folder/Screenshot%202026-05-05%20005056.png)

The functionality of each layer and the relationship between layers will become more evident throughout this course as the protocols are discussed in more detail.

---

## 5.3 Data Encapsulation

![Data encapsulation overview 1](./Content%20folder/Screenshot%202026-05-05%20005458.png)

![Data encapsulation overview 2](./Content%20folder/Screenshot%202026-05-05%20005630.png)

![Data encapsulation overview 3](./Content%20folder/Screenshot%202026-05-05%20005651.png)

![Data encapsulation overview 4](./Content%20folder/Screenshot%202026-05-05%20005831.png)

![Data encapsulation overview 5](./Content%20folder/Screenshot%202026-05-05%20005900.png)

![Data encapsulation overview 6](./Content%20folder/Screenshot%202026-05-05%20005944.png)

![Data encapsulation overview 7](./Content%20folder/Screenshot%202026-05-05%20010005.png)

![Data encapsulation overview 8](./Content%20folder/Screenshot%202026-05-05%20010058.png)

![Data encapsulation overview 9](./Content%20folder/Screenshot%202026-05-05%20010119.png)

![Data encapsulation overview 10](./Content%20folder/Screenshot%202026-05-05%20010201.png)
