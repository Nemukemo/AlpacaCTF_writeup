import struct

# 暗号化されたファイルの読み込み
with open("flag.enc", "rb") as f:
    enc_data = f.read()

# ダミー画像から54バイトの正常なヘッダーをベースとして取得
# （先ほど作成された Aが21文字のBMP画像などを dummy.bmp としてください）
with open("dummy.bmp", "rb") as f:
    header = bytearray(f.read(54))

# 横幅の当たりをつける（ファイルサイズから2300〜2450付近と推測できます）
for width in range(2300, 2450):
    # ヘッダーの18バイト目〜21バイト目が「横幅」のデータなので書き換える
    header[18:22] = struct.pack("<I", width)
    
    # 書き換えたヘッダー(54バイト) + 暗号化データの残り(54バイト目以降) を結合
    recovered_data = header + enc_data[54:]
    
    # 幅ごとのファイル名で保存
    with open(f"flag_{width}.bmp", "wb") as f:
        f.write(recovered_data)

print("生成完了！画像を順番に見て、文字が読めるものを探してください。")
# 2374