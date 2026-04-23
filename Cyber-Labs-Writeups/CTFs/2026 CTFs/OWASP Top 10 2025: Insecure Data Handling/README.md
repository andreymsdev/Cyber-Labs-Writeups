# OWASP Top 10 2025: Insecure Data Handling

> [![Medium](https://img.shields.io/badge/Read_with_images!-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@andreymsdev/owasp-top-10-2025-dominating-insecure-data-handling-tryhackme-write-up-2cf4f23415ee)

---

### TryHackMe Write-Up and Exploitation Laboratory
This repository documents the technical exploration and exploitation of three key categories from the OWASP Top 10 (2025). The focus is on application behavior and the risks associated with untrusted user input.

## Repository Structure
* [brute_xor.py](./brute_xor.py): Python script for automated brute-forcing of repeating XOR keys.
* [sql_injection.py](./sql_injection.py): Documentation and implementation of SSTI (Server-Side Template Injection) payloads.
* [pickle_rce_gen.py](./pickle_rce_gen.py): Payload generator for Remote Code Execution via Insecure Deserialization.

---

## A04: Cryptographic Failures
### Overview
Cryptographic failures occur when sensitive data is not adequately protected during storage or transmission. In this practical challenge, a note-sharing service used a weak, shared derivative key based on a repeating XOR cipher.

### Implementation: XOR Brute Force
The application utilized a key with a known prefix ("KEY"). The following script was developed to automate the discovery of the final character and decrypt the target data.

File link: [brute_xor.py](./brute_xor.py)

```python
# Logic for key rotation and XOR operation
for char in possible_chars:
    key = prefix + char
    decrypted = "".join(chr(cipher_data[i] ^ ord(key[i % 4])) for i in range(len(cipher_data)))
    
    if "Meeting" in decrypted or "reminder" in decrypted.lower():
        print(f"Key found: {key}")
        break
```

---

## A05: Injection (SSTI)

### Overview
Injection vulnerabilities arise when untrusted data is sent to an interpreter as part of a command or query. This practical demonstrates Server-Side Template Injection (SSTI) within a Jinja2 environment. Unlike standard SQL injection, SSTI targets the template engine used to render dynamic web pages.

### Exploitation Technique
By injecting template expressions such as `{{7*7}}`, it was possible to confirm that the server was evaluating mathematical operations, identifying the engine as Jinja2. The attack was then escalated to Remote Code Execution (RCE) by traversing the Python object hierarchy to access the `os` module.

File link: [sql_injection.py](./sql_injection.py)

**Payload utilized:**
```python
{{ self.__init__.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read() }}
```
---

## A08: Software and Data Integrity Failures

### Overview

Integrity failures occur when an application relies on plugins, libraries, or data from untrusted sources without verification. A primary example is Insecure Deserialization.

### Implementation: Pickle RCE

Using Python's `pickle` module, the `__reduce__` method was leveraged to execute arbitrary system commands during the object reconstruction process (deserialization).

File link: [pickle_rce_gen.py](./pickle_rce_gen.py)

```python
class MaliciousPayload:
    def __reduce__(self):
        # Execution of system-level commands
        return (os.popen, ("cat flag.txt",))
```

## Technical Takeaways

- OWASP 2025 Updates: Understanding the current landscape of web security risks and priority shifts.

- Cryptographic Analysis: Practical application of XOR decryption and automated brute-force techniques.

- Template Engines: Recognition of SSTI as a critical vector for full system compromise beyond standard SQLi.

- Serialization Risks: Analysis of how binary object formats can be weaponized to achieve RCE.

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
  <a href="https://devpost.com/andreymsdev" target="_blank">
    <img src="https://img.shields.io/badge/-Devpost-%23003E54?style=for-the-badge&logo=devpost&logoColor=white" alt="Devpost" />
  </a>
</p>