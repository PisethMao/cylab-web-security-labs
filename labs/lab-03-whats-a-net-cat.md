# Lab 03 - what's a net cat?

## Category

General Skills

## Difficulty

Easy

## Objective

The objective of this lab is to learn how to use `netcat` to connect to a remote service and retrieve the flag.

## Tools Used

* CYLab Security Academy
* CYLab Webshell
* Terminal
* Netcat (`nc`)

## Lab Description

In this challenge, the platform provides a remote host and port. The task is to connect to the service using the `nc` command and read the response from the server.

## Steps

1. Opened the `what's a net cat?` challenge page.
2. Clicked `Launch Instance` to start the challenge server.
3. Read the provided host and port from the challenge description.
4. Opened the CYLab Webshell terminal.
5. Used the `nc` command to connect to the remote service.
6. The server returned a message and displayed the flag.
7. Copied the full flag and submitted it to CYLab Security Academy.

## Command Used

```bash
nc fickle-tempest.picoctf.net 60724
```

## Output

```text
You're on your way to becoming the net cat master
picoCTF{...}
```

## Flag Format

```text
picoCTF{...}
```

> Note: The real flag is hidden here because this repository is for learning documentation. Do not publish real flags publicly unless your teacher requires it.

## What I Learned

I learned that `netcat` is a simple command-line networking tool used to connect to a remote host and port. It can be used to send and receive raw data from network services.

## Security Concept

Netcat is useful in cybersecurity because it helps test network services, inspect open ports, and understand client-server communication. In this lab, I used it safely in an authorized CTF environment.

## Conclusion

This lab helped me understand the basic usage of netcat. I learned how to connect to a remote service using a host and port, receive data from the server, and submit the returned flag.
