# Lab 10 - head-dump

## Category

Web Exploitation

## Difficulty

Easy

## Main Concept

Exposed Heap Dump and Sensitive Data Leakage

## Challenge Description

In this lab, the website was a simple picoCTF News web application. The challenge description mentioned that there was an endpoint exposing a file containing server memory. The goal was to find that endpoint, download the heap dump file, and search inside it for the hidden flag.

## Vulnerability

The application exposed a heap dump endpoint. A heap dump contains memory data from the running server application. If this file is publicly accessible, it may leak sensitive information such as tokens, credentials, environment variables, internal application data, or flags.

## Steps to Solve

First, I opened the challenge website and explored the page.

I noticed a post mentioning API documentation with keywords such as:

```text
nodejs
swagger UI
API Documentation
```

This suggested that the application might have a Swagger documentation page.

I opened the API documentation endpoint:

```text
/api-docs
```

From the API documentation, I found an endpoint related to heap dump generation.

Then I accessed the heap dump endpoint, which downloaded a file like this:

```text
heapdump-1780736701147.heapsnapshot
```

After the file was downloaded, I searched inside it for the flag using the terminal.

I first tried searching for the `.heapsnapshot` file:

```bash
grep -a -i "picoCTF" *.heapsnapshot
```

When the filename was known, I searched the exact file:

```bash
grep -a -i "picoCTF" heapdump-1780736701147.heapsnapshot
```

To make the output cleaner, I used:

```bash
strings heapdump-1780736701147.heapsnapshot | grep -i "picoCTF"
```

Then I used this command to print only the flag format:

```bash
strings heapdump-1780736701147.heapsnapshot | grep -o "picoCTF{[^}]*}"
```

The command displayed the hidden flag.

## Flag

```text
picoCTF{PUT_YOUR_FLAG_HERE}
```

## Important Note

The heap dump file should not be pushed to GitHub because it is only a temporary challenge file and may contain sensitive memory data.

Before committing, I removed it:

```bash
rm heapdump-1780736701147.heapsnapshot
```

## Lesson Learned

This lab shows why sensitive debugging endpoints should never be publicly exposed. Heap dump files can contain private server memory data, including secrets and flags. Developers should disable heap dump endpoints in production, protect debugging tools with authentication, and avoid exposing internal diagnostic files to the public.

## Status

Completed
