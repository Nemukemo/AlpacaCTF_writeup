from base64 import b32encode, b64encode
from pwn import *

# 接続先の設定
HOST = "localhost"
PORT = 1337

# 15バイトの'a'でペイロードを作成
test_data = b"a" * 15

b32_payload = b32encode(test_data).decode().rstrip("=")
b64_base = b64encode(test_data).decode().rstrip("=")

# Base64の後ろに改行を追加して文字数を増やす
# Base64デコーダーは末尾の改行を無視する
b64_payload = b64_base + "\n" * 20  # 20個の改行を追加

print(f"[*] b32の長さ: {len(b32_payload)}")
print(f"[*] b64の長さ: {len(b64_payload)}")
print(f"[*] b64 > b32: {len(b64_payload) > len(b32_payload)}")
print()

# サーバーに接続
io = remote("34.170.146.252", 60350)

# Base32を送信
io.recvuntil(b"Base32: ")
io.sendline(b32_payload.encode())
print(f"[+] Base32送信: {b32_payload}")

# Base64を送信
io.recvuntil(b"Base64: ")
io.sendline(b64_payload.encode())
print(f"[+] Base64送信済み")

# レスポンスを受信
response = io.recvall(timeout=2).decode()
print()
print("[*] サーバーからの応答:")
print(response)

io.close()
