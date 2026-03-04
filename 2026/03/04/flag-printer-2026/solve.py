from pwn import *

# 接続先の設定（実際のIPとポートに変更してください）
HOST = '34.170.146.252'
PORT = 10951

def solve():
    # サーバーに接続
    io = remote(HOST, PORT)
    flag = ""
    
    print("[+] 接続しました。FLAGの受信を開始します...")
    
    while True:
        try:
            # timeout=4.0 とすることで、4秒間何も受信しなかったら次へ進む
            # (socatの5秒制限に引っかかる前にアクションを起こすため)
            recv_data = io.recv(1, timeout=4.0)
            
            if recv_data:
                # 文字を受信できた場合
                char = recv_data.decode('utf-8', errors='ignore')
                flag += char
                print(f"\r現在取得中のFLAG: {flag}", end="")
            else:
                # 4秒間何も受信できなかった場合（サーバーが長時間sleep中）
                # socatの切断を防ぐためにダミーデータを送信してタイマーをリセット
                # ※サーバー側のプログラムがエラーで落ちないよう、無害な空白や改行を送るのが一般的です
                io.send(b" ")
                
        except EOFError:
            # サーバー側から正規に接続が切られた場合（全て出力し終わった等）
            print("\n[+] 通信が終了しました。")
            break
        except Exception as e:
            print(f"\n[!] エラーが発生しました: {e}")
            break
            
    print(f"\n[★] 最終獲得FLAG: {flag}")

if __name__ == "__main__":
    solve()