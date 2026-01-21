# msgとencrypt(msg)、encrypt(FLAG)を知っている場合
encrypted_msg = bytes.fromhex("aa9054e15ee209d458784a70bab6a5d62523f26eef2458cb3d48ccc6122fba1d75733c17c70a908a64b45b0caaf8d0e3bd30bcc0900283af88d82d4020cdacf7eaa5685ccf443776b4d9")
encrypted_flag = bytes.fromhex("af9d4dec44a333d44d2e0e62ade1f5c95a38e438eb6a0acf0b10c1b92513cf627828250ff43cbbae42db6244a3")
msg = b"Daily AlpacaHack is a daily CTF challenge with a fun new puzzle every day."

# XORで鍵ストリームを復元
keystream = bytes(a ^ b for a, b in zip(encrypted_msg, msg))

# FLAGを復元
flag = bytes(a ^ b for a, b in zip(encrypted_flag, keystream[:len(encrypted_flag)]))
print(flag)