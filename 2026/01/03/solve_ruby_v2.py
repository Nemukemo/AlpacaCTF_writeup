
def get_generator23_sequence(n):
    # Prime::Generator23.new.take(n) の挙動を模倣
    # 実際には 2, 3, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37...
    # となる（2と3の倍数以外の数、ただし最初の2,3は含まれると仮定）
    
    seq = [2, 3]
    candidate = 5
    while len(seq) < n:
        if candidate % 2 != 0 and candidate % 3 != 0:
            seq.append(candidate)
        candidate += 1
    return seq

# 暗号化された文字列
encrypted_str = "Coufhlj@bixm|UF\\JCjP^P<"

# 数列を取得
seq = get_generator23_sequence(23)

# 復号 (XOR)
flag_chars = []
for i in range(len(encrypted_str)):
    char_code = ord(encrypted_str[i])
    val = seq[i]
    decrypted_char = chr(char_code ^ val)
    flag_chars.append(decrypted_char)

print("Sequence:", seq)
print("Flag: " + "".join(flag_chars))
