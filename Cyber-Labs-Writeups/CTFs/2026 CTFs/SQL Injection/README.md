# SQL Injection 

SQL Injection (SQLi) is a type of cyber attack where malicious SQL (Structured Query Language) code is injected into a vulnerable application's input fields. This can manipulate the application's database queries, potentially granting unauthorised access to the database or allowing attackers to retrieve, modify, or delete data.

---

What I Learned (Summary)

* **Vulnerability Detection:** Identifying entry points in input fields, URLs, and headers using characters like `'` or `"`.
* **Attack Types:**
    * **In-Band:** Using `UNION` statements to display data directly on the page.
    * **Blind (Boolean):** Inferring data through "True/False" server responses.
    * **Blind (Time-Based):** Exfiltrating data by measuring server delays with `SLEEP()` functions.
    * **Out-of-Band:** Forcing the database to send data to an external server via `DNS`.
* **Database Mapping:** Using `information_schema` to systematically discover tables and columns.
* **Defense:** Implementing **Prepared Statements** and **Input Validation** as the primary defenses.
## Task 1 - BRIEF
**What does SQL stand for?** Structured Query Language

---

## Task 2 - What is a Database?
A database is a way of electronically storing collections of data in an organised manner. A database is controlled by a DBMS, which is an acronym for Database Management System. DBMSs fall into two camps: Relational and Non-Relational. Within a DBMS, you can have multiple databases, each containing its own set of related data.

* **What is the acronym for the software that controls a database?** DBMS
* **What is the name of the grid-like structure which holds the data?** Table

---

## Task 3 - What is SQL?
SQL (Structured Query Language) is a feature-rich language used for querying databases. These SQL queries are better referred to as statements.

* **What SQL statement is used to retrieve data?** `SELECT`
* **What SQL clause can be used to retrieve data from multiple tables?** `UNION`
* **What SQL statement is used to add data?** `INSERT`

---

## Task 4 - What is SQL Injection?
The point wherein a web application using SQL can turn into SQL Injection is when user-provided data gets included in the SQL query.

From the URL above, you can see that the blog entry selected comes from the id parameter in the query string. The web application needs to retrieve the article from the database and may use an SQL statement that looks something like the following.

* **What character signifies the end of an SQL query?** `;`

---

## Task 5 - In-Band SQLi
In-Band SQL Injection is the easiest type to detect and exploit; In-Band just refers to the same method of communication being used to exploit the vulnerability and also receive the results, for example, discovering an SQL Injection vulnerability on a website page and then being able to extract data from the database to the same page.

### My Methodology:
By using single quotes, we can see that the site breaks. Breaking the syntax confirms that we can inject malicious commands.

Using a single or double quote in `id=1` results in a syntax error. To exploit this, I used the 'Onion Trick' (`UNION SELECT`) to align the columns until the error disappeared, revealing that the query uses three columns.

For fingerprinting, I used `0 UNION SELECT 1, 2, database()` and discovered the database name: **sqli_one**.

Next, I listed the tables using `group_concat(table_name)` from `information_schema.tables`, which identified the `article` and `staff_users` tables.

Finally, by querying `information_schema.columns`, I found the columns: `id`, `password`, and `username`. This allowed me to extract the credentials and capture the flag.

* **What is the flag after completing level 1?** `THM{SQL_INJECTION_3840}`

---

## Task 6 - Blind SQLi - Authentication Bypass
**The Exploit**
* **Target Field:** Password
* **Payload:** `' OR 1=1;--`
* **Resulting Query:** `SELECT * FROM users WHERE username='' AND password='' OR 1=1;--`

* **What is the flag after completing level two?** `THM{SQL_INJECTION_9581}`

---

## Task 7 - Blind SQLi - Boolean Based
**Vulnerability:** The GET parameter in the `/checkuser` endpoint allowed for SQL injection.  
**Technique:** Union-Based Injection was used to join a second query to the original one.  
**Key Bypass:** Using a non-existent username forced the database to ignore the first part of the query and return the data from the UNION statement instead.

### Execution Steps:
1. **Column Enumeration:** Identified 3 columns using `' UNION SELECT 1,2,3`
2. **Data Extraction:** Leaked the admin password by injecting `' UNION SELECT 1,2,password FROM users WHERE username='admin'`
3. **Authentication:** Logged in via the main form using the discovered credentials.

* **What is the flag after completing level three?** `THM{SQL_INJECTION_10934}`

---

## Task 8 - Blind SQLi - Time Based
**Method:** Blind Time-Based SQL Injection via the referrer parameter.  
**Core Logic:** The server provided no data or errors. Success was measured solely by response time using the `SLEEP(5)` function.

### Exploit Flow:
1. **Detection:** Proved the injection by forcing a 5-second delay.
2. **Table Check:** Confirmed the `users` table via time-delay queries.
3. **Data Leaking:** Brute-forced the password `4961` by testing characters with the `LIKE` operator and observing which attempts triggered the 5-second sleep.
4. **Result:** Logged in as admin to retrieve the flag.

* **What is the final flag after completing level four?** `THM{SQL_INJECTION_MASTER}`

---

## Task 9 - Out-of-Band SqLI
Out-of-band SQL Injection isn't as common as it either depends on specific features being enabled on the database server or the web application's business logic, which makes some kind of external network call based on the results from an SQL query.

* **Name a protocol beginning with D that can be used to exfiltrate data from a database.** DNS

---

## Task 10 - Remediation
As impactful as SQL Injection vulnerabilities are, developers do have a way to protect their web applications from them by following the advice below:

* **Prepared Statements (With Parameterized Queries):** In a prepared query, the first thing a developer writes is the SQL query, and then any user inputs are added as parameters afterwards. Writing prepared statements ensures the SQL code structure doesn't change and the database can distinguish between the query and the data.
* **Input Validation:** Input validation can go a long way to protecting what gets put into an SQL query. Employing an allow list can restrict input to only certain strings.
* **Escaping User Input:** Escaping user input is the method of prepending a backslash (`\`) to special characters, which then causes them to be parsed just as a regular string.

* **Name a method of protecting yourself from an SQL Injection exploit.** Prepared Statements

---

**Room Link:** [https://tryhackme.com/room/sqlinjectionlm](https://tryhackme.com/room/sqlinjectionlm)

[![Medium Article](https://img.shields.io/badge/Medium_Article-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@andreymsdev/sql-injection-complete-walkthrough-tryhackme)
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