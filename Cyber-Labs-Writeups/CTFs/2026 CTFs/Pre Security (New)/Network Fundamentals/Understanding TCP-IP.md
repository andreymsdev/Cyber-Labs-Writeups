## Understanding TCP/IP

## A Fresh Start

Understanding TCP/IP and these network concepts is essential because they are the foundation of how the internet works. From sending an email to streaming a video, everything depends on these layers and rules working together.

It’s good to know that there is also the **OSI model**, which has 7 layers instead of 4. The OSI model is more theoretical, used mostly for teaching and explaining concepts. **TCP/IP**, on the other hand, is more practical — it’s the one actually used on the internet today.

![Five Layers of the TCP/IP Model](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.whatismyip.com%2Fstatic%2Fe3c2d375b219e64f67c8bc157b203f83%2Ftcp-ip-model.webp&f=1&nofb=1&ipt=b27a498d149d1c82ecd09cfa8ecb4f07c66d60141984311561f6ecbec2a6c81e)

This image shows how the model is divided into four parts. Think of it like a stack: at the top are the programs you interact with (application), and at the bottom is the physical network that actually moves the data.

## Application Layer
Here we have the protocols that people interact with directly:
* **SMTP** — good for emails
* **FTP** — for sending files
* **HTTP** — opening websites
* **DNS** — translating domains into IP addresses

## Transport Layer
This is where we find TCP and UDP:
* **TCP** — more reliable, because it confirms delivery of packets. Good for emails, web browsing, and other cases where accuracy matters.
* **UDP** — less reliable (it doesn’t confirm lost packets), but faster. Good for streaming, video calls, and gaming, where speed is more important than perfect delivery.

## Internet Layer
Here the packets are encapsulated. This layer adds the IP addresses of origin and destination, making sure data knows where it’s coming from and where it’s going.

## Network Access Layer
This is the physical side: cables, optic fiber, Wi-Fi, and other technologies that actually carry the packets across the network.

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*arGZYZ1SnCUJ8u6lYcK53A.png)
---

Together, the packets pass through this process step by step, starting from the application you use (like opening a website) down to the physical medium that delivers the data.

> Data goes down layer by layer, turning into segments, packets, and bits, until it crosses the physical medium and reaches the other host.

Here you can see the journey of information: it starts as data in the application, becomes segments in the transport layer, packets in the internet layer, and finally bits in the network layer. On the other side, the process is reversed, rebuilding the original message.

## Connection and data communication concepts
Here are some of the concepts that are important to know when learning TCP/IP:

* **Addressing** — Every device needs an IP address so data knows exactly where to go, like a digital home address.
* **Encapsulation** — Data is wrapped layer by layer, with headers added at each step, so the receiver knows how to unpack it.
* **De-encapsulation:** The receiver reverses this, "stripping away" headers layer by layer to reveal the original message.
* **Routing** — Routers choose the best path for packets, making sure information doesn’t get lost and reaches the destination efficiently.
* **Reliability** — Protocols like TCP check for errors and resend lost packets, ensuring the message arrives complete.
* **Efficiency** — Networks balance speed and resources. Some protocols (like UDP) skip extra checks to deliver data faster, which is great for streaming and real-time communication.

## Network Concepts
* **LAN (Local Area Network)** — A small network, usually inside a home, office, or school. Fast and limited to a local area.
* **WAN (Wide Area Network)** — A larger network that connects multiple LANs across cities or even countries. The internet itself is the biggest WAN.
* **Switches** — Devices that connect computers inside a LAN. They forward data only to the specific device that needs it, making communication faster and more efficient.
* **Protocols** — The rules of communication. Examples are TCP/IP, HTTP, FTP. Without protocols, devices wouldn’t understand each other.
* **Topologies** — The way networks are physically or logically arranged. Examples: star, bus, ring, mesh. Each has pros and cons for speed, reliability, and cost.
* **Security** — Protecting data and devices from attacks. Includes firewalls, encryption, and safe practices to keep networks reliable and trustworthy.

---

### Sources
* Computer Networking: Principles, Protocols and Practice (Olivier Bonaventure)

**YouTube educational channels:**
* TCP/IP and the OSI Model Explained
* How the Internet Works in 5 Minutes

*Images: The second was created by me and inspired by visuals found on Pinterest*
