# Lab 04 - Mod 26

## Category

Cryptography

## Difficulty

Easy

## Objective

The objective of this lab is to understand ROT13 encoding and decode the provided text to find the flag.

## Tools Used

* CYLab Security Academy
* CyberChef
* Browser

## Lab Description

In this challenge, the platform provides a file named `values.txt`. The text inside the file is encoded using ROT13. To solve the challenge, I used CyberChef to decode the message and reveal the flag.

## Steps

1. Opened the `Mod 26` challenge page.
2. Clicked the `values.txt` file.
3. Copied the encoded text from the file.
4. Opened CyberChef.
5. Searched for the `ROT13` operation.
6. Added `ROT13` to the recipe area.
7. Pasted the encoded text into the input box.
8. CyberChef decoded the text and displayed the flag.
9. Copied the full flag and submitted it to CYLab Security Academy.

## Encoded Text

```text
cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_45559noq}
```

## Command / Method Used

This lab was solved using CyberChef with the following operation:

```text
ROT13
```

## Flag Format

```text
picoCTF{...}
```

> Note: The real flag is hidden here because this repository is for learning documentation. Do not publish real flags publicly unless required by the teacher.

## What I Learned

I learned that ROT13 is a simple letter substitution method where each letter is shifted by 13 positions in the alphabet. I also learned how to use CyberChef to decode encoded text in a browser.

## Security Concept

ROT13 is not real encryption because it is very easy to reverse. It is mainly used as a basic encoding technique or as an introduction to cryptography concepts in CTF challenges.

## Conclusion

This lab helped me understand basic cryptography and encoding. I practiced using CyberChef to decode ROT13 text and retrieve a flag from an encoded file.
