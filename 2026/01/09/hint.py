# 0から65535（基本多言語面）の範囲で探す例
sum = ""
for i in range(65536):
    char = chr(i)
    if char != char.swapcase().swapcase():
        sum += char
        print(f"見つけた！ 文字: {char}, コードポイント: {i}")
print(sum)