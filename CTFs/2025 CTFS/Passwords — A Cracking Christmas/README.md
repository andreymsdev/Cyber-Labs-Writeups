# TryHackMe: Passwords — A Cracking Christmas Write-Up

> [![Medium](https://img.shields.io/badge/Read_Full_Walkthrough_with_Images-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@andreymsdev/passwords-a-cracking-christmas-821ec5661bc1)

---

### Category: Cryptography / Password Cracking / Security Awareness

This challenge focuses on the risks associated with weak passwords in encrypted archives and PDFs, demonstrating how attackers use offline brute-force and dictionary attacks to gain unauthorized access.

## 1. Cracking Encrypted PDFs
To recover the password for the file `flag.pdf`, I used **pdfcrack**. This tool allows for a direct attack against the PDF's encryption scheme.

**Command used:**

```bash
pdfcrack -f flag.pdf -w /usr/share/wordlists/rockyou.txt
```

The tool successfully identified the user password, allowing access to the document and the first flag.

## 2. Cracking Encrypted ZIP Archives
Cracking a ZIP file requires a two-step process: extracting the hash and then cracking it.

:**Step A: Hash Extraction:** I used zip2john to convert the ZIP file's encryption into a format that John the Ripper can understand.

```bash
zip2john flag.zip > ziphash.txt
```

Step B: Dictionary Attack Using the extracted hash and the rockyou.txt wordlist, I ran John the Ripper:

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt ziphash.txt
```

Once cracked, I unzipped the file using the recovered password and retrieved the second flag `from flag.txt`.

## Technical Lessons

- Hash-based Cracking: Encryption protects confidentiality, but it doesn't prevent offline attacks. Tools like zip2john make it easy to separate the protection layer from the data.

- Wordlist Power: The effectiveness of a dictionary attack depends heavily on the quality of the wordlist (e.g., rockyou.txt).

- Strong Password Policy: This lab reinforces why long, complex passwords and modern encryption standards (like AES-256 for ZIP) are vital to defend against automated tools.

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