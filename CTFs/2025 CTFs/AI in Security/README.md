# TryHackMe: AI in Security — Write-Up

> [![Medium](https://img.shields.io/badge/Read_Full_Walkthrough_with_Images-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@andreymsdev/ai-in-security-old-saint-nick-b3f90c61a203)

---

### Category: AI Security / Red Team / Blue Team / DevSecOps

This challenge explores the influence of AI in cybersecurity, demonstrating how automated assistants can help generate exploits, analyze logs, and review source code.

## 1. Reconnaissance
An **Nmap** scan revealed the following services:
* **Port 80**: Main web server.
* **Port 5000**: Vulnerable application hosting the login page.
* **Port 3000**: Service associated with the challenge interface.

## 2. Red Team: AI-Assisted Exploitation
Using the AI assistant, I generated a Python script to exploit a **SQL Injection** vulnerability on the login page. The AI suggested using the payload:
`alice' OR 1=1 -- -`



By running the script against `http://MACHINE_IP:5000/login.php`, the application bypassed authentication and returned the first flag in the response body.

## 3. Blue Team & Software Analysis
The AI assistant also demonstrated defensive capabilities:
* **Log Analysis**: Identifying patterns of the automated SQLi attack.
* **Code Review**: Detecting the specific lines of code where input sanitization was missing.

## 4. Final Flag
After completing all stages of the AI showcase (Red Team, Blue Team, and Software), the final system flag was presented as a reward for completing the investigation.

---

## Technical Lessons
* **AI as a Tool**: AI can significantly speed up script development for penetration testing, but it requires human oversight to adjust parameters like URLs and ports.
* **SQL Injection Risk**: Even simple payloads like `' OR 1=1` are still effective if developers rely on unsanitized user inputs.
* **The Heart of the Challenge**: Identifying that port **5000** was the actual target was crucial for successful exploitation.

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