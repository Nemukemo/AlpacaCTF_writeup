from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# ==========================================
# 1. サーバー実行時に表示された [DEBUG] key の値をここにコピペしてください
#    例: server_key_hex = "0123456789abcdef0123456789abcdef"
# ==========================================
server_key_hex = "2e832b8ceab66b33cce7c9a4256523b2" 

try:
    # 鍵をバイト列に変換
    # (貼り付け忘れ防止のチェック)
    if "ここに" in server_key_hex and len(server_key_hex) != 32:
        raise ValueError("server_key_hex にサーバーの鍵をコピペしてください！")
    
    # 前後の空白を削除
    key = bytes.fromhex(server_key_hex.strip())
    print(f"[*] Using Key: {key.hex()}")

    # 2. 送りたい中身（Plaintext）を作る "🦙🦙🦙🦙🦙"
    target_username = chr(129433) * 5
    print(f"[*] Target Username: {target_username}")

    # 3. パディングを追加して暗号化
    plaintext_bytes = target_username.encode('utf-8')
    padded_plaintext = pad(plaintext_bytes, AES.block_size)
    
    iv = os.urandom(16)
    cipher_encrypt = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher_encrypt.encrypt(padded_plaintext)

    # ==========================================
    # 4. [重要] ローカルで復号テスト (Sanity Check)
    #    ここでエラーが出るなら、サーバーに送っても絶対エラーになります
    # ==========================================
    print("\n--- Local Sanity Check (Verification) ---")
    cipher_decrypt = AES.new(key, AES.MODE_CBC, iv) # 同じ鍵とIVを使う
    check_padded = cipher_decrypt.decrypt(ciphertext)
    check_plaintext = unpad(check_padded, AES.block_size).decode()
    
    if check_plaintext == target_username:
        print("[OK] Verification successful! Payload is valid.")
    else:
        print("[!] Verification failed! Decrypted text does not match.")
        
    # 5. サーバーに送る値を表示
    print("\n--- Paste these into the Server ---")
    print(f"Ciphertext (hex): {ciphertext.hex()}")
    print(f"IV (hex):         {iv.hex()}")

except Exception as e:
    print(f"\n[!] Error: {e}")
    print("ヒント: server_key_hex の値を正しく設定しましたか？")