def caesar_cipher(text,key):
    result=""
    for c in text:
        if c.isalpha():
            base =97 if c.islower() else 65
            result += chr((ord(c) - base + key) % 26 + base)
        else:
            result += c
    return result

text = input("Clear message: ")
key = int(input("Key between (1-25): "))
print(caesar_cipher(text, key))
