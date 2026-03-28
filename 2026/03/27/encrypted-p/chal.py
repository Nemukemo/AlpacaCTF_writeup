import os
from Crypto.Util.number import getPrime, bytes_to_long

m = bytes_to_long(os.getenv("FLAG", "Alpaca{REDACTED}").encode())
p = getPrime(512)
q = getPrime(512)
n = p * q
e = 65537
c1 = pow(m, e, n)
c2 = pow(p, e, n)

assert m < n

print(f"n = {n}")
print(f"e = {e}")
print(f"c1 = {c1}")
print(f"c2 = {c2}")
