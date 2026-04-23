# **W1seGuy**

---


Your friend told me you were wise, but I don't believe them. Can you prove me wrong?

---

## **What is XOR in Cryptography?**

XOR (Exclusive OR) is a logical operation that compares two bits:

* If the bits are the same (0 and 0, or 1 and 1), the result is 0
* If the bits are different (0 and 1, or 1 and 0), the result is 1

In cryptography, XOR is often used because:

* **Reversible**: Applying the same key again restores the original message
* **Simple, Fast, and Useful**: Only requires bitwise operations

BUT the **XOR cipher** is not secure for serious use today — but it's great for learning how encryption works.

---

## NETCAT

```
nc 10.201.39.23 1337 
```

---

### Discovering the XOR Key and CTF

In the challenge code, we can observe that:

1. The first 4 letters of the encoded string are “THM{”
2. The last character of the string is "}"

> flag = 'THM{thisisafakeflag}'

So in the code, we can ask three questions:

1. hex_text = input("Enter the encoded text (hex): ")
2. start = input("Enter the known starting letters: ")
3. end = input("Enter the known ending character: ")

Using this, we can discover the XOR key and decode the message.

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