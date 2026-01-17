from base64 import b32encode, b64encode, b32decode, b64decode

# 15バイトの'a'でペイロードを作成
test_data = b"a" * 15

b32_payload = b32encode(test_data).decode().rstrip("=")
b64_base = b64encode(test_data).decode().rstrip("=")

# Base64に改行を追加して文字数を増やす
b64_payload = "\n".join([b64_base[i:i+1] for i in range(len(b64_base))])

print("=" * 50)
print("ペイロード生成完了！")
print("=" * 50)
print()
print("Base32に入力する文字列:")
print(b32_payload)
print()
print("Base64に入力する文字列:")
print(b64_payload)
print()
print("=" * 50)
print("検証:")
print(f"b32の長さ: {len(b32_payload)}")
print(f"b64の長さ: {len(b64_payload)}")
print(f"b64 > b32: {len(b64_payload) > len(b32_payload)}")
print()

# デコードして一致確認
try:
    result32 = b32decode(b32_payload)
    result64 = b64decode(b64_payload)
    print(f"デコード結果が一致: {result32 == result64}")
    print(f"パディングなし: {'=' not in b32_payload and '=' not in b64_payload}")
except Exception as e:
    print(f"エラー: {e}")