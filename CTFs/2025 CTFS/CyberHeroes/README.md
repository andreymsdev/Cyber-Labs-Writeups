# TryHackMe: CyberHeros — Write-Up

> [![Medium](https://img.shields.io/badge/Read_Full_Walkthrough_with_Images-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@andreymsdev/tryhackme-cyberheros-write-up-13cf0474cdb6)

---

### Category: Web Hacking / Authentication Bypass / JavaScript Logic

This challenge focuses on exploiting misconfigurations and insecure coding practices where sensitive logic is handled on the client-side rather than the server-side.

## 1. Initial Recon
I started with an **Nmap** scan to identify open ports and services:
* **Result**: Port 80/tcp open (Apache/2.4.48 Ubuntu).

The main page displayed a clear message: *“Join our forces, find the vuln on our login page and login to join us.”*

## 2. Directory Enumeration
Using **Gobuster** to hunt for hidden paths, I found:
* `/assets/`: Directory listing enabled (Misconfiguration).
* `/.htaccess` & `/.htpasswd`: Existing but protected (403).

This step confirmed that although some files were protected, the server had unnecessary directory exposure.

## 3. Analyzing the Login Logic
Accessing `login.html` and inspecting the source code revealed the authentication logic hardcoded in **JavaScript**:

```javascript
if (a.value=="h3ck3rBoi" & b.value==RevereString("54321@terceSrepuS")) {
   xhttp.open("GET", "RandomLo0o0o0o0o0o0o0o0o0o0gpath12345_Flag_"+a.value+"_"+b.value+".txt", true);
   xhttp.send();
}
```

By reversing the string `"54321@terceSrepuS"`, I obtained the credentials:

- **Username:** `h3ck3rBoi`
- **Password:** `SuperSecret@12345`

## 4. Flag Capture

The script generates a dynamic path for the flag file based on the credentials. By logging in or manually constructing the URL using the discovered credentials, the flag was retrieved successfully.

## Vulnerabilities Identified

- **Hardcoded Credentials:** Storing authentication logic in client-side JavaScript allows anyone to bypass the login by inspecting the code.

- **Security by Obscurity:** The use of a simple "Reverse" function for passwords provides no real security.

- **Information Exposure:** The server revealed valid file naming patterns through client-side scripts.

## Conclusion

The attack path followed a logical progression, from initial reconnaissance to the final exploitation:

1.  **Nmap**: Identified open port 80 (Apache Web Server).
2.  **Gobuster**: Enumerated directories and discovered configuration flaws (Directory Listing).
3.  **Code Analysis**: Inspecting the JavaScript in `login.html` revealed hardcoded credentials and the authentication logic.
4.  **Flag Retrieval**: Used the discovered credentials and logic to access the hidden flag file.


---

## Get in Touch!

<p>
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