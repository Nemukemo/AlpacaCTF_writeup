import os, re
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from PIL import Image, ImageDraw, ImageFont

flag = os.getenv('FLAG', 'Alpaca{REDACTED}')
assert re.match(r"^Alpaca\{[A-Za-z]+\}$", flag)

# Generate image
font = ImageFont.truetype("DejaVuSans.ttf", 128)
draw = ImageDraw.Draw(Image.new("RGB", (1, 1), "white"))
left, top, right, bottom = draw.textbbox((0, 0), flag, font=font)

img = Image.new("RGB", (right - left, bottom - top), "white")
draw = ImageDraw.Draw(img)
draw.text((-left, -top), flag, fill="black", font=font)

img.save("flag.bmp")

# Encrypt image
key = os.urandom(16)
aes = AES.new(key, AES.MODE_ECB)

data = pad(open("flag.bmp", "rb").read(), 16)
open("flag.enc", "wb").write(aes.encrypt(data))

os.unlink("flag.bmp")
