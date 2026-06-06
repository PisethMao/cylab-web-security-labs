import requests
import base64

URL = "http://wily-courier.picoctf.net:49484/"

s = requests.Session()
s.get(URL)

cookie = s.cookies.get("auth_name")

if not cookie:
    print("[-] auth_name cookie not found")
    exit()

# Decode TWICE to get the actual ciphertext
decoded_once = base64.b64decode(cookie)
cipher = base64.b64decode(decoded_once)

print("[+] Original cookie length:", len(cookie))
print("[+] Cipher length:", len(cipher))
print("[+] Testing bit flips... This might take a minute.")

for i in range(len(cipher)):
    for bit in range(8):
        data = bytearray(cipher)
        # Flip the bit
        data[i] ^= 1 << bit

        # Encode TWICE to reconstruct the proper cookie format
        encoded_once = base64.b64encode(bytes(data))
        forged_cookie = base64.b64encode(encoded_once).decode()

        # Request the root URL, not /search
        r = requests.get(URL, cookies={"auth_name": forged_cookie})
        text = r.text

        # If the flag is on the page, we win
        if "picoCTF{" in text:
            start = text.find("picoCTF{")
            end = text.find("}", start) + 1
            print(f"\n[+] FLAG FOUND at index={i}, bit={bit}!")
            print(f"\n{text[start:end]}\n")
            exit()

print("[-] Testing complete. Flag not found.")