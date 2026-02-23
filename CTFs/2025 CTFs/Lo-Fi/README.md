# TryHackMe: Lo-Fi — Write-Up

> [![Medium](https://img.shields.io/badge/Read_Full_Walkthrough_with_Images-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@andreymsdev/lo-fi-tryhackme-d71bc27ba0df)

---

### Category: Web Hacking / Local File Inclusion (LFI)

A simple web application serving lo-fi beats, but with a critical flaw in how it handles page requests.

## 1. Reconnaissance
I started with an **Nmap** scan to identify open ports and services:
* **Ports**: 22 (SSH) and 80 (Apache 2.2.22).
* **Target**: A web server hosting the "Lo-Fi Music" site.

## 2. Spotting the Vulnerability
While navigating the site, I noticed the URL structure:
`http://MACHINE_IP/?page=relax.php`

This indicates that the `page` parameter is being used to include files dynamically. Without proper sanitization, this leads to a **Local File Inclusion (LFI)** vulnerability.

## 3. Exploitation (Path Traversal)
To confirm the vulnerability, I attempted to read the system's password file using path traversal:
`http://10.65.166.175/?page=../../../../../etc/passwd`

The server successfully returned the content of `/etc/passwd`, confirming that I could break out of the web root directory (`/var/www/html`).

## 4. Hunting the Flag
The challenge stated the flag was in the root of the filesystem (`/`). I used `curl` to test different depths and file names:

```bash
curl "[http://10.65.166.175/?page=../../../../../flag.txt](http://10.65.166.175/?page=../../../../../flag.txt)
```
By going up enough levels `(../)`, I reached the root directory and captured the flag.

---

## Technical Takeaways

Input Validation: Never trust user-supplied input in functions like `include()` or `require()`.

Path Traversal: Each `../` moves the pointer up one directory level. Even if you don't know the exact depth, adding extra `../` will eventually stop at the system root (`/`).

Least Privilege: Web servers should have restricted permissions to prevent reading sensitive files like flag.txt or /etc/passwd.

---

## Redes!

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
  <a href="https://tryhackme.com/p/Tux10" target="_blank">
    <img src="https://img.shields.io/badge/-TryHackMe-%23212C42?style=for-the-badge&logo=tryhackme&logoColor=white" alt="TryHackMe" />
  </a>
</p>