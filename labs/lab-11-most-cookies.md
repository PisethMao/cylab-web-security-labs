
---

```markdown
# Lab 11: Most Cookies

## Category

Web Exploitation

## Challenge Description

In this challenge, the web application uses Flask session cookies. The application says that Flask session cookies should be secure, but the secret key used to sign the cookie is weak.

The goal of the challenge is to discover the Flask secret key, forge a valid admin session cookie, and access the flag.

## Concept

Flask session cookies are signed, not encrypted. This means the data inside the cookie can be decoded and read by the user.

However, the user cannot modify the cookie unless they know the secret key used by the Flask application. If the secret key is weak or predictable, it can be brute-forced using a wordlist.

In this lab, the secret key was found using a cookie-name wordlist.

## Tools Used

* Browser Developer Tools
* VS Code Terminal
* Python
* flask-unsign
* cookies.txt wordlist

## Solving Steps

### 1. Open the Challenge Website

First, I opened the challenge instance in the browser.

Then I inspected the website cookies using:

```text
Right click → Inspect → Application → Cookies