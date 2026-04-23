# TryHackMe: Seven Minutes on the Seine — OSINT Write-Up

> [![Medium](https://img.shields.io/badge/Read_Full_Walkthrough_with_Images-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@andreymsdev/the-case-seven-minutes-on-the-seine-tryhackme-ctf-561631484b96)

---

### Category: OSINT (Open Source Intelligence) / Security Investigation

This investigation simulates a real-world response to a heist at the **Louvre Museum**. The goal was to reconstruct the events using only public tools and open-source data.

## Investigation Steps

### 1. The Heist Context
A crew in hi-vis vests breached the **Galerie d’Apollon**. My role as an analyst was to identify their escape route and details of the breach using:
* **Google Maps**: For geographical reconstruction of the museum exits.
* **Browser Inspection Tools**: To find hidden clues in the web structure.
* **Public Databases**: Verification of museum protocols and archives.

### 2. Manual Search vs. AI
During the lab, I realized that while AI is a powerful tool, it struggled with the specific details of this case. The successful approach required "old-school" manual searching through the Louvre's official documentation and Google Maps satellite views.

* **Key Discovery**: Identifying the correct access point at the museum (e.g., `PORTE_DES_LIONS`).

### 3. Louvre Protocol & CCTV Analysis
The second part of the challenge focused on a surveillance audit. Reports indicated:
* Outdated servers.
* Weak password policies.

By searching for publicly leaked information or "obvious" credential patterns related to the Louvre audits, I successfully bypassed the CCTV system login to review the footage from the date of the incident.

---

## Personal Takeaways & Security Impact
* **The Power of OSINT**: This CTF proves that most information needed for a breach (or an investigation) is already out there if you know where to look.
* **Credential Vulnerability**: The most striking lesson was how a **single weak password** can render millions of dollars in security technology (cameras, servers, sensors) completely useless. 
* **Persistence**: When the lab environment failed, direct IP access and manual research saved the investigation.

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