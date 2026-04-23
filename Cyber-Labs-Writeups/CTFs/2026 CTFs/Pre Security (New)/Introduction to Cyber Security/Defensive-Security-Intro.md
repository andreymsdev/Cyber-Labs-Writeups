![Defensive Security Intro](../images/defensivesecintro.png)

Introducing defensive security and related topics, such as Threat Intelligence, SOC, DFIR, Malware Analysis, and SIEM.

---

## Introduction to Defensive Security

In this room, we will explore the world of defensive security. We will uncover how defensive security teams play a pivotal role in protecting networks and organisations across the globe.

Defensive security, known as the blue team, is used to prepare and proactively protect an organisation's IT infrastructure.  It is concerned with two main tasks:

1. Preventing intrusions from occurring.
2. Detecting intrusions when they occur and responding properly.

**Answer the questions below**

Which team focuses on defensive security?

> Blue Team

---

## Exploring the SOC

**A Security Operations Centre** (SOC) is a team of cyber security professionals that monitors the network and its systems to detect malicious cyber security events. Some of the main areas of interest for a SOC are:

1. **Trends & Vulnerability Awareness** (Keeping up to date with the latest trends and vulnerabilities in the industry).
2. **Policy Violations** (A security policy is a set of rules that outline how an organisation's assets are to be used and protected).
3. **Unauthorised & Illegal Activity** (The SOC team establishes a baseline of acceptable behaviour and activity. Any deviation from this baseline is investigated. Illegal activity exposes the organisation to higher risk.)
4. **Intrusion & Breach Detection** (The SOC team is responsible for detecting and responding to these breaches.)

**Answer the questions below**

What would you call a team of cyber security professionals that monitors a network and its systems for malicious events?

> Security Operations Centre

---

## Digital Forensics

Digital forensics is the application of traditional forensic science processes to digital devices. *Digital forensics is used to preserve and analyse digital evidence to aide in the investigation of incidents, such as a breach*. This may involve looking at information from:

1. **File System** (Analysing a low-level copy of a system's storage reveals much information, such as installed programs, created, partially overwritten and deleted files.)
2. **System Memory** (If an attacker runs a malicious program within the memory without saving it to the disk, the memory can be analysed to uncover details about how the program operates.)
3. **System Logs** (Log files provide plenty of information about what happened on a system. Even if the attacker tries to clear their traces, some traces will remain.)
4. **Network Logs** (Logs of the network traffic that have traversed a network would help answer more questions about whether an attack is occurring and what it entails.)

**Answer the questions below**

An attacker deploys a piece of malicious code that does not save to the disk. What digital forensics technique would we use in this instance?

> Memory

---

## Incident Response

Incident Response is how organisations manage security events such as breaches, data leaks and cyber attacks. An incident response process is a defined set of stages to minimise damage, contain the threat and recover fast. The process will look like so:

![Example](https://tryhackme-images.s3.amazonaws.com/user-uploads/5f04259cf9bf5b57aed2c476/room-content/b162600f5990f249d921aa0e8b7822f7.png)

**Further details:**

1. **Preparation** (Creating the necessary resources and frameworks to handle an incident. This includes creating incident response teams, infrastructure to support in the incident response process, as well anything to help prevent the incidents, such as providing phishing awareness training.)
2. **Detection & Analysis** (Using tooling and processes to detect incidents and assess their scope (reach) and severity. Logs can be analysed for suspicious events.)
3. **Containment, Eradication, and Recovery** (Limiting the impact of the incident, such as preventing a virus from spreading and eliminate the cause and restore affected systems.)
4. **Post-Incident Activity** (Review the incident overall, how it was handled and could've been prevented. What were the learning points throughout the process? Do we need to provide further cyber awareness training?)

**Answer the questions below**

What phase of the incident response process involves providing "cyber awareness" training to employees?

> Preparation

---

## Practical Example of Defensive Security

You have been given access to the organisation's internal **Security Information and Event Management** (SIEM) tool, which gathers security-related information and events from various sources and presents them in one dashboard. If the SIEM finds something suspicious, an alert will be generated.

**Simulating a SIEM**

Here we have to analyze the logs, analyze the IP, then block from the internal firewall.

**Answer the questions below**

What is the flag that you obtained by following along?

> THREAT-BLOCKED

---

## Key Takeaways

- Defensive security focuses on prevention and detection.  
- SOC teams monitor networks for malicious activity.  
- Digital forensics helps preserve and analyze evidence.  
- Incident response minimizes damage and improves resilience.  
- SIEM tools centralize alerts and support defensive actions.  

---
