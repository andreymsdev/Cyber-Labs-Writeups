# TryHackMe: Bricks Heist — Write-Up

> [![Medium](https://img.shields.io/badge/Read_Full_Walkthrough_with_Images-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@andreymsdev/tryhack3m-bricks-heist-e13319dcfd25)

---

### Category: Web Hacking / Malware Analysis / Cryptojacking

This lab involves hacking back a compromised WordPress server and investigating a suspicious background process that points to a larger cybercrime operation.

## 1. Initial Enumeration
After adding `bricks.thm` to my `/etc/hosts`, I started with an **Nmap** scan:
* **Open Port**: 80 (HTTP)
* **Technology**: WordPress 6.5

Using `curl` and `wpscan`, I identified the theme **Bricks version 1.9.5**, which is known to be vulnerable to Remote Code Execution (RCE).

## 2. Exploitation (RCE)
I utilized a Python exploit targeting the Bricks theme vulnerability to gain an interactive shell on the server.

* **Flag Found**: `THM{fl46_650c844110baced87e1606453b93f22a}` located at `/data/www/default/`.

## 3. Post-Exploitation & Incident Response
The server was extremely slow, indicating a compromise beyond my own access. I began investigating system processes:

* **Suspicious Service**: `TRYHACK3M` (identified via `systemctl`).
* **Malicious Process**: `kdevtmpfsi` — a well-known cryptocurrency miner.
* **Log File**: Found `inet.conf` containing encoded strings.

## 4. Decoding & Threat Intel
Using **CyberChef**, I performed a multi-stage decoding (Hex → Base64 → Base64) to reveal the attacker's wallet address:
* **Wallet**: `bc1qyk79fcp9hd5kreprce89tkh4wrtl8avt4l67qa`

By searching this wallet on **Blockchair**, I found connections to transactions involving the **LockBit** ransomware group, linking this specific cryptojacking instance to a major threat actor.

---

## Technical Takeaways
* **Vulnerability Research**: Identifying specific theme versions (Bricks 1.9.5) is crucial for finding high-impact RCEs.
* **Malware Indicators**: Recognizing `kdevtmpfsi` allowed for a quick pivot from web exploitation to incident response.
* **Blockchain OSINT**: Following the money (wallets) is a powerful way to attribute attacks to known threat groups.

---

## Get in Touch!

<p align="center">
  <a href="https://www.linkedin.com/in/andrey-ms" target="_blank">
    <img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="mailto:andreym.professional@gmail.com">
    <img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail" />
  </a>
  <a href="https://medium.com/@andreymsdev" target="_blank">
    <img src="https://img.shields.io/badge/-Medium-%23000000?style=for-the-badge&logo=medium&logoColor=white" alt="Medium" />
  </a>
</p>