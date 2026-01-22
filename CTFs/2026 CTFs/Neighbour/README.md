# TryHackMe: Neighbour CTF Write-Up

> [![Medium](https://img.shields.io/badge/Read_Full_Walkthrough_with_Images-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@andreymsdev/january-1st-2026-code-stuff-and-tryhackme-neighbour-ctf-8acb31495934)

### Category: Insecure Direct Object Reference (IDOR) / Broken Access Control

This write-up documents the exploitation of access control flaws based on URL parameters, demonstrating how a lack of identity validation can allow unauthorized access to privileged accounts.

## Exploitation Process

### 1. Initial Enumeration
The first step was to perform a port scan using **Nmap** to identify active services on the target.

* **Result**: Port **80 (HTTP)** was open, indicating an active web service.



### 2. Web Application Analysis
Accessing the target IP via Firefox revealed a login page requiring credentials. 

* **Investigation**: By inspecting the page source code (`Ctrl + U`), I analyzed the authentication logic. Although no credentials were hardcoded, the system allowed initial access as a `guest`.



### 3. Vulnerability Identification (IDOR)
Once logged in as a guest, the URL structure revealed a vulnerable parameter:

`http://<TARGET_IP>/profile.php?user=guest`

The application relied solely on the `user` parameter to determine which profile to display, without verifying if the authenticated user had the authorization to view other profiles.



### 4. Exploitation and Flag Capture
By manually modifying the parameter from `guest` to `admin` in the URL:

`http://<TARGET_IP>/profile.php?user=admin`

The system granted full access to the administrator's profile, exposing sensitive information and the challenge flag.

---

## Key Takeaways
* **Access Control**: Never trust user-supplied parameters to define access permissions.
* **IDOR Mitigation**: Direct object references must be validated on the server-side by comparing the session identity with the requested resource.
* **Security Testing**: Always inspect URL parameters and source code for hidden logic or bypasses.

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
  <a href="https://tryhackme.com/p/Tux10" target="_blank">
    <img src="https://img.shields.io/badge/-TryHackMe-%23212C42?style=for-the-badge&logo=tryhackme&logoColor=white" alt="TryHackMe" />
  </a>
  <a href="https://devpost.com/andreymsdev" target="_blank">
    <img src="https://img.shields.io/badge/-Devpost-%23003E54?style=for-the-badge&logo=devpost&logoColor=white" alt="Devpost" />
  </a>
</p>