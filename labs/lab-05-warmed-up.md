# Lab 05 - Warmed Up

## Category

General Skills

## Difficulty

Easy

## Objective

The objective of this lab is to convert a hexadecimal number from base 16 into a decimal number in base 10.

## Tools Used

* CYLab Security Academy
* Browser
* Basic number conversion

## Lab Description

In this challenge, the question asks for the decimal value of `0x3D`. The value is written in hexadecimal format, also known as base 16. To solve the challenge, I converted the hexadecimal number into decimal format.

## Given Value

```text
0x3D
```

## Method

The prefix `0x` means the number is written in hexadecimal.

In hexadecimal:

```text
D = 13
```

So:

```text
0x3D = (3 × 16) + 13
```

Calculation:

```text
3 × 16 = 48
48 + 13 = 61
```

Therefore:

```text
0x3D = 61
```

## Steps

1. Opened the `Warmed Up` challenge page.
2. Read the question asking to convert `0x3D` from base 16 to base 10.
3. Identified that `0x` represents hexadecimal.
4. Converted `3D` into decimal.
5. Found that the decimal value is `61`.
6. Submitted the answer in the required flag format.

## Flag Format

```text
picoCTF{...}
```

## What I Learned

I learned how to convert a hexadecimal value into a decimal value. Hexadecimal uses base 16, which includes numbers `0-9` and letters `A-F`. In this lab, I learned that `D` represents `13` in decimal.

## Security Concept

Hexadecimal is commonly used in computing, programming, memory addresses, colors, encoding, and cybersecurity. Understanding number systems is important because many security tools and low-level data formats use hexadecimal values.

## Conclusion

This lab helped me practice basic number conversion from hexadecimal to decimal. It is a simple but important foundation for cybersecurity and computer science.
