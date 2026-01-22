# TryHackMe: Splunk Basics — SIEM Investigation

> [![Medium](https://img.shields.io/badge/Read_Full_Walkthrough_with_Images-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@andreymsdev/splunk-basics-did-you-siem-21c64a5c9f5e)

---

### Category: Blue Team / Security Operations (SOC) / Log Analysis

In this challenge from TryHackMe’s *Advent of Cyber*, I used **Splunk** to investigate a simulated attack against a web server, practicing **Threat Hunting** and log analysis skills.

## 1. Exploring the Logs
The first step was to identify the attacker's IP and understand the environment. I used a basic query to filter web traffic:
`index=main sourcetype=web_traffic`

## 2. Detecting Anomalies and Traffic Peaks
To identify the day with the highest activity, I used visualizations of traffic patterns, focusing on the `client_ip` field. The traffic peak revealed the exact moment the infrastructure was under the most pressure.

## 3. Identifying SQL Injection (Havij)
I filtered the logs for malicious **User Agents**. I identified automated SQL Injection attempts using the **Havij** tool by filtering events associated with that specific agent.

## 4. Path Traversal Attempts
Using the previously identified attacker IP, I filtered for suspicious paths (e.g., `../../etc/passwd`). This allowed me to accurately count how many attempts were made to access sensitive server files.

## 5. Firewall Logs and Data Exfiltration
To confirm if the attack was successful and if data theft occurred, I analyzed the firewall logs between the compromised server and the attacker's Command and Control (C2) IP.

I used the Splunk `stats sum(size_bytes)` command to calculate the total volume of data exfiltrated to the C2 server.

## Technical Lessons (Threat Hunting Mindset)

- **Noise Filtering**: I learned how to filter out benign traffic (common browsers) to focus on attack tools like `sqlmap`, `Havij`, `curl`, and `wget`.

- **Attack Chain Analysis**: I was able to trace the attacker's steps from reconnaissance and exploitation to final exfiltration.

- **The Value of SIEM**: Splunk proved essential for correlating web traffic with firewall logs, enabling a much faster incident response.

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
</p>