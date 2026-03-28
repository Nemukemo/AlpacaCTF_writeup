from pwn import *

# 1. サーバーへ接続（実際のIPとポートに書き換えます）
io = remote('34.170.146.252', 51958)

# 2. textの入力
io.recvuntil(b"text> ")
io.sendline(b"\x1b(B")

# 3. encodingの入力
io.recvuntil(b"encoding> ")
io.sendline(b"iso2022_jp")

# 4. 結果の表示（フラグの受け取り）
io.interactive()