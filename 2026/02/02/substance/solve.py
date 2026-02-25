from math import gcd
from Crypto.Util.number import long_to_bytes

n1 = 70430356624056699219964353455091734195306937238245707901514922333654568000660
n2 = 5585179348150525015655680494025565656820428601640301759505137819334580532521858

# GCDを計算
g = gcd(n1, n2)

# gはflagの倍数なので、小さい数で割ってflagを探す
for div in range(2, 2027):
    candidate = g // div
    try:
        flag_bytes = long_to_bytes(candidate)
        if b'Alpaca{' in flag_bytes:
            print(flag_bytes.decode())
            break
    except:
        continue