
def get_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        is_prime = True
        for p in primes:
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 1
    return primes

# 暗号化された文字列
# Rubyのソースコード上で "Coufhlj@bixm|UF\\JCjP^P<" となっていたため、
# バックスラッシュはエスケープされています。実際の文字は '\' です。
encrypted_str = "Coufhlj@bixm|UF\\JCjP^P<"

# 最初の23個の素数を取得
primes = get_primes(23)

# 復号 (XOR)
flag_chars = []
for i in range(len(encrypted_str)):
    char_code = ord(encrypted_str[i])
    prime = primes[i]
    decrypted_char = chr(char_code ^ prime)
    flag_chars.append(decrypted_char)

print("Flag: " + "".join(flag_chars))
