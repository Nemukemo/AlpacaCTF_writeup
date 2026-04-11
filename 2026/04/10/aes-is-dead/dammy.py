from PIL import Image, ImageDraw, ImageFont
import os

# 試したいダミーのフラグ
dummy_flag = "Alpaca{AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA}"

# 画像の生成（chall.pyと同じ処理）
font = ImageFont.truetype("DejaVuSans.ttf", 128)
draw = ImageDraw.Draw(Image.new("RGB", (1, 1), "white"))
left, top, right, bottom = draw.textbbox((0, 0), dummy_flag, font=font)

img = Image.new("RGB", (right - left, bottom - top), "white")
draw = ImageDraw.Draw(img)
draw.text((-left, -top), dummy_flag, fill="black", font=font)

# ダミー画像を保存
img.save("dummy.bmp")
target_size = 863 * 1024  # 863KB = 884032 bytes

for i in range(1, 10000):
    dummy_flag = "Alpaca{" + "A" * i + "}"
    
    font = ImageFont.truetype("DejaVuSans.ttf", 128)
    draw = ImageDraw.Draw(Image.new("RGB", (1, 1), "white"))
    left, top, right, bottom = draw.textbbox((0, 0), dummy_flag, font=font)
    
    img = Image.new("RGB", (right - left, bottom - top), "white")
    draw = ImageDraw.Draw(img)
    draw.text((-left, -top), dummy_flag, fill="black", font=font)
    
    img.save("dummy.bmp")
    
    size = os.path.getsize("dummy.bmp")
    if size >= target_size:
        print(f"目標サイズ到達: {size} バイト")
        print(f"Aの文字数: {i}")
        break

# ファイルサイズを確認
print(f"ダミーのサイズ: {os.path.getsize('dummy.bmp')} バイト")