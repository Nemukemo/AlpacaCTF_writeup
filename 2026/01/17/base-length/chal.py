from base64 import b32decode, b64decode

b32 = input("Base32: ")
b64 = input("Base64: ")

assert b32.count("=") == 0 and b64.count("=") == 0, "Don't use padding!"
assert b32decode(b32) == b64decode(b64), "Decoded values are not equal!"

# Base32: 5 bits -> 1 char,
# Base64: 6 bits -> 1 char, so ...
if len(b32) >= len(b64):
    print("Expected :)")
else:
    # never reach here :)
    print("Wow... The flag is Alpaca{**** REDACTED ****}")
