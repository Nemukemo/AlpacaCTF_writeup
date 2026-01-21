import struct

# いただいたデータをリストに格納
flag_longs = [
    0x9beff28796ecf3e9, 0x2335ae47c5b3ea6a,
    0x7bd30354a9dfecfe, 0x3243804702b92b8c,
    0x7caad2839ae4bf07, 0x2749c14807c2e873,
    0xbcd9c683a3ebf11c, 0x4119a527d9aa0a73
]

# バイト列に変換
enc_bytes = b''.join([struct.pack('<Q', val) for val in flag_longs])

MAGIC_CONST = 0x522C

print("Flag: ", end="")

for i in range(0, len(enc_bytes), 2):
    word = enc_bytes[i] + (enc_bytes[i+1] << 8)
    word_idx = i // 2
    
    # ★修正ポイント★ 周期を 4 から 8 に変更！
    k = word_idx % 8
    
    # 計算回数
    count = 256 - ((1 << k) + 1)
    
    # 逆算
    total_added = (MAGIC_CONST * count)
    original_word = (word - total_added) & 0xFFFF
    
    char1 = original_word & 0xFF
    char2 = (original_word >> 8) & 0xFF
    
    if char1 == 0: break
    print(chr(char1), end="")
    if char2 == 0: break
    print(chr(char2), end="")

print()