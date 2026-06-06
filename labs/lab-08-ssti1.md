# Lab 08 - SSTI1

## Category

Web Exploitation

## Difficulty

Easy

## Main Concept

Server-Side Template Injection

## Challenge Description

In this lab, the website allowed users to submit text that was rendered by the server. The goal was to test whether the input was being processed by a server-side template engine and then use that vulnerability to read the flag.

## What is SSTI?

SSTI stands for Server-Side Template Injection. It happens when user input is placed directly into a server-side template without proper sanitization. If the template engine evaluates the input, an attacker may be able to execute template expressions on the server.

## Steps to Solve

First, I opened the challenge website from the CYLab workspace.

The page allowed me to submit a message or announcement. Since the challenge name was SSTI1, I tested whether the server evaluated template syntax.

I submitted this simple payload:

```jinja2
{{7*7}}