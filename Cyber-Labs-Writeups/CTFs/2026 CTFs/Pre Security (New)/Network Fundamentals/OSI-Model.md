![OSI Model](../images/osimodel.png)

Learn about the fundamental networking framework that determines the various stages in which data is handled across a network

---

## What is the OSI Model?

**The Open Systems Interconnection**(OSI) model is a conceptual framework that divides network communications functions into seven layers. Sending data over a network is complex because various hardware and software technologies must work cohesively across geographical and political boundaries. The OSI data model provides a universal language for computer networking, so diverse technologies can communicate using standard protocols or rules of communication. Every technology in a specific layer must provide certain capabilities and perform specific functions to be useful in networking. Technologies in the higher layers benefit from abstraction as they can use lower-level technologies without having to worry about underlying implementation details.

#### Why is the OSI model that important?

Every tech student must have studied OSI model in the university. Because the layers of The Open Systems Interconnection (OSI) model encapsulate every type of network communication across both *software and hardware components*. he model was designed to allow two standalone systems to communicate via standardised interfaces or protocols based on the current layer of operation.

#### Key Benefits of the OSI Model

1. **Conceptual Clarity and Modular Architecture**

The OSI model provides a framework for organizing complex networked systems into distinct, functional layers. By decomposing systems into smaller, manageable parts through abstraction, engineers can better conceptualize and manage the architecture as a whole.

2. **Accelerated Research and Development**

The model streamlines development by allowing engineers to focus on specific technological layers. This specialization enables the creation of interoperable systems using repeatable processes and standardized protocols, significantly reducing the time required to build and integrate new networking solutions.

3. **Flexible Standardization**

Rather than mandating specific protocols, the OSI model defines the tasks and functions each layer must perform. This approach offers several advantages:

- **Abstraction:** Lower-level networking complexities are hidden, allowing developers to focus on high-level application logic.

- **Interoperability:** It allows for rapid system building and decomposition without requiring deep knowledge of every underlying component.

- **Scalability:** Modern applications can easily integrate or swap technologies at different levels without redesigning the entire system.

## The Seven layers of the OSI MODEL:

![Osi Model](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.fs.com%2Fimages%2Fcommunity%2Fupload%2FkindEditor%2F202107%2F29%2Foriginal-seven-layers-of-osi-model-1627523878-JYjV8oybcC.png&f=1&nofb=1&ipt=6a8b447be5297ab8f7dcecefbc7514056036747a79307375efa8ae90940b8291)

---

**Physical**

They physical layer refers to the physical communication medium and the technologies to trasmit data across that medium. At its core, data communication is the transfer of digital and electronic signals through various physical channels like fiber-optic cables, copper cabling, and air. The physical layer includes standards for technologies and metrics closely related with the channels, such as Bluetooth, NFC, and data transmission speeds.

![Physical Layer](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.lifewire.com%2Fthmb%2FfMTgZXa9S4IQkQmpebezKmh_BdM%3D%2F1500x1000%2Ffilters%3Ano_upscale()%3Amax_bytes(150000)%3Astrip_icc()%2Flayers-of-the-osi-model-illustrated-818017-finalv1-2-ct-ed94d33e885a41748071ca15289605c9.png&f=1&nofb=1&ipt=2af5d146e2abae4006aba32553b89cae24994ff33ee7b81afb1b349499ec7ed0)

[Image from LifeWire Website](https://www.lifewire.com/layers-of-the-osi-model-illustrated-818017)

**Data Link Layer**

The data link layer refers to the technologies used to connect two machines across a network where the physical layer already exists. It manages data frames, which are digital signals encapsulated into data packets. Flow control and error control of data are often key focuses of the data link layer. Ethernet is an example of a standard at this level. The data link layer is often split into two sub-layers: the Media Access Control (MAC) layer and Logical Link Control (LLC) layer. 

![Data Link Layer](https://www.lifewire.com/thmb/BoAH0Wd3pRNi5algz3S6nP9N-Z0=/750x0/filters:no_upscale():max_bytes(150000):strip_icc()/layers-of-the-osi-model-illustrated-818017-finalv1-3-ct-9d3e1bf44a554e3db31f706201fc69f6.png)

**Network Layer**

The network layer is concerned with concepts such as routing, forwarding, and addressing across a dispersed network or multiple connected networks of nodes or machines. The network layer may also manage flow control. Across the internet, the Internet Protocol v4 (IPv4) and IPv6 are used as the main network layer protocols.

![Network Layer](https://www.lifewire.com/thmb/KbyU-p2e0FgMxdmhokkZAwuEhlo=/750x0/filters:no_upscale():max_bytes(150000):strip_icc()/layers-of-the-osi-model-illustrated-818017-finalv1-4-ct-9ffde2c7142849819c3fcf5e305a242f.png)

**Transport Layer**

The primary focus of the transport layer is to ensure that data packets arrive in the right order, without losses or errors, or can be seamlessly recovered if required. Flow control, along with error control, is often a focus at the transport layer. At this layer, commonly used protocols include the Transmission Control Protocol (TCP), a near-lossless connection-based protocol, and the User Datagram Protocol (UDP), a lossy connectionless protocol. TCP is commonly used where all data must be intact (e.g. file share), whereas UDP is used when retaining all packets is less critical (e.g. video streaming).

![Transport Layer](https://www.lifewire.com/thmb/CeRxeoLkX1P8MEijwXpyesiUlZw=/750x0/filters:no_upscale():max_bytes(150000):strip_icc()/layers-of-the-osi-model-illustrated-818017-final-5-ct-373fc5a9edc74359819021555f37467d.png)

**Session Layer**

The session layer is responsible for network coordination between two separate applications in a session. A session manages the beginning and ending of a one-to-one application connection and synchronization conflicts. Network File System (NFS) and Server Message Block (SMB) are commonly used protocols at the session layer.

![Session Layer](https://www.lifewire.com/thmb/vyEeh7XAr9hDdqXZZg46jS3cLUk=/750x0/filters:no_upscale():max_bytes(150000):strip_icc()/layers-of-the-osi-model-illustrated-818017-finalv1-6-ct-f21bdae22e54415b881d77babe8ca51d.png)

**Presentation Layer**

The presentation layer is primarily concerned with the syntax of the data itself for applications to send and consume. For example, Hypertext Markup Language (HTML), JavaScipt Object Notation (JSON), and Comma Separated Values (CSV) are all modeling languages to describe the structure of data at the presentation layer. 
Application layer

![Presentation Layer](https://www.lifewire.com/thmb/htyb5obXUu4C3a2DHLzAMo2vWOY=/750x0/filters:no_upscale():max_bytes(150000):strip_icc()/layers-of-the-osi-model-illustrated-818017-finalv1-7-ct-e102db1b79da4926b510f944183989f8.png)

**Application Layer**

The application layer is concerned with the specific type of application itself and its standardized communication methods. For example, browsers can communicate using HyperText Transfer Protocol Secure (HTTPS), and HTTP and email clients can communicate using POP3 (Post Office Protocol version 3) and SMTP (Simple Mail Transfer Protocol).

Not all systems that use the OSI model implement every layer.

![Application Layer](https://www.lifewire.com/thmb/QAQRr60YGkvEAO2ExW4Yt_lb0Qs=/750x0/filters:no_upscale():max_bytes(150000):strip_icc()/layers-of-the-osi-model-illustrated-818017-finalv1-8-ct-089b2573bf47462d85f9343f50329f72.png)

---

**The TCP/IP model**

The TCP/IP model is comprised of five different layers:

- The physical layer
- The data link layer
- The network layer
- The transport layer
- They application layer

While layers like the physical layer, network layer, and application layer appear to map directly to the OSI model, this isn’t quite the case. Instead, the TCP/IP model most accurately maps to the structure and protocols of the internet.

The OSI model remains a popular networking model to describe how networking operates from a holistic perspective for educational purposes. However, the TCP/IP model is now more commonly used in practice.

---

## Sources

 - [TryHackMe](https://tryhackme.com/dashboard)
 - [LifeWire Tech for Humans](https://www.lifewire.com/layers-of-the-osi-model-illustrated-818017) 
 - [AWS](https://aws.amazon.com/what-is/osi-model/#what-is-the-osi-model--14xfgxr)
 