# ***Brute Force***

---


<img src="images/rocklee.jpg" alt="rocklee" width="800">

---

This script performs username enumeration against an authorized CTF or lab environment by sending login requests and analyzing server responses to identify valid usernames.

---

## Functions

**Sends** POST requests to a login endpoint using usernames from a wordlist.

**Detects** valid usernames based on server response messages:

* `"Wrong password"` → Username exists
* `"wrong username"` → Username does not exist.

---

### Requirements

* Python 3.x
* `requests` library

* A username wordlist (e.g., from SecLists)

---

#### Installation

```
pip install requests

```

---

##### How to use

* Set the `url` variable to the target login endpoint.
* Ensure the `file_path` points to a valid username list.

* Run the script.

---

TryHackMe Challenge: https://tryhackme.com/room/lookup

---

![naruto da imagem](./images/naruto.png)

---
