![Offensive Security Intro](../images/ofsecintro.png)

Hack your first website (legally in a safe environment) and experience an ethical hacker's job.

---

## What is Offensive Security?

"To outsmart a hacker, you need to think like one."

This is the core of "Offensive Security." It involves breaking into computer systems, exploiting software bugs, and finding loopholes in applications to gain unauthorized access. The goal is to understand hacker tactics and enhance our system defences.

**Answer the questions below**

Which of the following options better represents the process where you simulate a hacker's actions to find vulnerabilities in a system?

- Offensive Security
- Defensive Security 

> Offensive Security

---

## Starting the Lab

Here is a fake bank. 

![Fake Bank](https://tryhackme-images.s3.amazonaws.com/user-uploads/63588b5ef586912c7d03c4f0/room-content/63588b5ef586912c7d03c4f0-1716285774320)

**Answer the questions below**

What is your bank account number in the FakeBank web application?
 
> 8881

---

## Your First Hack

Our goal is to find a way to hack the FakeBank application to steal money. For that purpose, they have provided us with an account in the bank, just as if we were a regular user.

One of the easiest ways we can try to hack the application is by finding hidden features in the application. Sometimes, applications will expose sensitive functionality to users via secret URLs. If we can find such URLs, we might be able to perform actions that a regular user is not supposed to do.

To find hidden URLs, we will use a tool called  `dirb`. This tool uses a brute-force approach, by taking a list of potential page names and testing one by one if they exist in your website. This approach works because people use predictable names a lot of times.

**Answer the questions below**

`Dirb` should have found 2 hidden URLs. One of them is `http://fakebank.thm/images`. What is the other one?

> http://fakebank.thm/bank-deposit

---

## Adding Funds to Your Account

You should have found a secret page that allows you to add funds to a bank account `(http://fakebank.thm/bank-deposit)`. Type the hidden page into the FakeBank website using the browser's address bar.

From this page, you should be able to add funds to your bank account (remember your bank account number is 8881). Let's add $2000 to it:

Adding $2000 or more to our account, we should be able to see a new balance reflected on our account page. Press the `Return to Your Account` button at the end of the deposit receipt to go there now and confirm you got the money!

**Answer the questions below**

If your balance is now positive, a pop-up should appear with some green words in it. Input the green words as the answer to this question (all in uppercase).

(You may need to hit Refresh if you closed the pop-up already)

> BANK-HACKED

---

## Key Takeaways

- Learned how offensive security simulates hacker actions.
- Practiced using `dirb` to discover hidden URLs.
- Understood how insecure web applications can expose sensitive functionality.

