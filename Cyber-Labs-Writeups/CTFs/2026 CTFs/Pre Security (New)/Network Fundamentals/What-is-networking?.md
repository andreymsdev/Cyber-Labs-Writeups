![What is Networking?](../images/whatisnetworking.png)

Begin learning the fundamentals of computer networking in this bite-sized and interactive module

---

## What is Networking?

Networks are simply things connected. For example, your friendship circle: you are all connected because of similar interests, hobbies, skills and sorts.

Networks can be found in all walks of life:

- A city's public transportation system
- Infrastructure such as the national power grid for electricity
- Meeting and greeting your neighbours
- Postal systems for sending letters and parcels

Networks are integrated into our everyday life. Be it gathering data for the weather, delivering electricity to homes or even determining who has the right of way at a road. Because networks are so embedded in the modern-day, networking is an essential concept to grasp in cybersecurity.

**Answer the questions below**

What is the key term for devices that are connected together?

> Network

---

## What is the Internet?

The Internet is one giant network that consists of many, many small networks within itself. 

The first iteration of the Internet was within the ARPANET project in the late 1960s. This project was funded by the United States Defence Department and was the first documented network in action. However, it wasn't until 1989 when the Internet as we know it was invented by Tim Berners-Lee by the creation of the World Wide Web (WWW). It wasn't until this point that the Internet started to be used as a repository for storing and sharing information, just like it is today.

**Answer the questions below**

Who invented the World Wide Web?

> Tim Berners-Lee

---

## Identifying Devices on a Network

Devices on a network are very similar to humans in the fact that we have two ways of being identified:

- Our Name
- Our Fingerprints

Devices have the same thing: two means of identification, with one being permeable. These are:

- An IP Address
= A Media Access Control (MAC) Address — think of this as being similar to a serial number.

#### IP Addresses

Briefly, an IP address (or Internet Protocol) address can be used as a way of identifying a host on a network for a period of time, where that IP address can then be associated with another device without the IP address changing. First, let's split up precisely what an IP address is in the diagram below:

![IP Addresses](https://tryhackme-images.s3.amazonaws.com/user-uploads/5de96d9ca744773ea7ef8c00/room-content/a0de0d68641982ddf1a8c5a9f1984c4c.png)

An IP address is a set of numbers that are divided into four octets. The value of each octet will summarise to be the IP address of the device on the network. *This number is calculated through a technique known as IP addressing & subnetting*, but that is for another day. What's important to understand here is that **IP addresses can change from device to device but cannot be active simultaneously more than once within the same network.**

IP Addresses follow a set of standards known as protocols. These protocols are the backbone of networking and force many devices to communicate in the same language, which is something that we'll come onto another time. However, we should recall that devices can be on both a private and public network. Depending on where they are will determine what type of IP address they have: a public or private IP address.

A public address is used to identify the device on the Internet, whereas a private address is used to identify a device amongst other devices. Take the table & screenshot below as an example. 

#### IPV4 x IPV6

- IPv4: Uses 32-bit addresses (e.g., 192.168.1.1). Limited to 4.3 billion addresses, which is no longer enough for all the world's devices.

- IPv6: Uses 128-bit alphanumeric addresses (e.g., 2001:db8::8a2e...). It provides virtually infinite addresses and has built-in security (IPSec) and better efficiency.

#### MAC Addresses

**Devices on a network will all have a physical network interface, which is a microchip board found on the device's motherboard**. This network interface is assigned a unique address at the factory it was built at, called a MAC (Media Access Control ) address. The MAC address is a twelve-character hexadecimal number (a base sixteen numbering system used in computing to represent numbers) split into two's and separated by a colon. These colons are considered separators. For example, a4:c3:f0:85:ac:2d. The first six characters represent the company that made the network interface, and the last six is a unique number. Basically it's an ID.

![IP Addresses](https://tryhackme-images.s3.amazonaws.com/user-uploads/5de96d9ca744773ea7ef8c00/room-content/394caee97fb1b9f7b5a5f7a7ea0a9f71.png)

An interesting thing with MAC addresses is that they can be faked or "spoofed" in a process known as spoofing. This spoofing occurs when a networked device pretends to identify as another using its MAC address. When this occurs, it can often break poorly implemented security designs that assume that devices talking on a network are trustworthy. Take the following scenario: A firewall is configured to allow any communication going to and from the MAC address of the administrator. If a device were to pretend or "spoof" this MAC address, the firewall would now think that it is receiving communication from the administrator when it isn't.

Places such as cafes, coffee shops, and hotels alike often use MAC address control when using their "Guest "or "Public" Wi-Fi. This configuration could offer better services, i.e. a faster connection for a price if you are willing to pay the fee per device.  The interactive lab attached to this task has been made to replicate this scenario!

#### IP Address vs. MAC Address

- IP Address (Logical): Like your home address. It identifies where your device is on a network. It can change if you move to a different Wi-Fi.

- MAC Address (Physical): Like your ID/SSN number. It is a unique 12-character hexadecimal code assigned at the factory. It identifies who the device is, regardless of the network.

#### Practical

The interactive labs simulate a hotel Wi-Fi network where you have to pay for the service. You'll note that the router is not allowing Bob's packets ( blue) to the TryHackMe website and is placing them in the bin, but Alice's packets (green) are going through fine because she has paid for Wi-Fi. Try changing Bob's MAC address to the same as Alice's to see what happens.

Deploy the interactive lab and proceed to answer the following questions below.

**Answer the questions below**

What does the term "IP" stand for?
> Internet Protocol
What is each section of an IP address called?
> Octet
How many sections (in digits) does an IPv4 address have? 
> 4
What does the term "MAC" stand for?
> Media Access Control
Deploy the interactive lab using the "View Site" button and spoof your MAC address to access the site.  What is the flag?
> THM{YOU_GOT_ON_TRYHACKME}

---

## Ping (ICMP)

Ping is one of the most fundamental network tools available to us. Ping uses ICMP (Internet Control Message Protocol) packets to determine the performance of a connection between devices, for example, if the connection exists or is reliable.

The time taken for ICMP packets travelling between devices is measured by ping, such as in the screenshot below. This measuring is done using ICMP's echo packet and then ICMP's echo reply from the target device.

![IP Addresses](https://assets.tryhackme.com/additional/networking-fundamentals/intro-to-networking/ping/ping1.png)

Here we are pinging a device that has the private address of 192.168.1.254. Ping informs us that we have sent six ICMP packets, all of which were received with an average time of 4.16 milliseconds.

#### Latency and Ping

- Ping: Measured in milliseconds (ms). It is the time it takes for a data packet to travel to a server and back.

- High Ping = Lag: The higher the ping, the slower the connection feels.

- TCP Impact: Since TCP requires a "confirmation" (ACK) for every packet sent, high ping forces the sender to wait longer before sending the next batch of data, effectively slowing down your real-world speed.

**Answer the questions below**

What protocol does ping use?

> ICMP

What is the syntax to ping 10.10.10.10?

> ping 10.10.10.10

What flag do you get when you ping 8.8.8.8?

> THM{I_PINGED_THE_SERVER}

---

## Key Takeaways

- Networking is the connection of devices, similar to social or transport networks. 
- The Internet is a giant network of smaller networks, invented by Tim Berners-Lee in 1989 with the World Wide Web. 
- Devices are identified by **IP addresses** (logical, changeable) and **MAC addresses** (physical, unique). 
- IPv4 uses 32-bit addresses (limited), while IPv6 uses 128-bit addresses (virtually unlimited). 
- MAC addresses can be spoofed, which can bypass weak security designs. 
- Ping uses ICMP packets to test connectivity and measure latency. 