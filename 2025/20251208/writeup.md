# 問題理解
## 前提知識
### そもそもRSA暗号とは＆Common Modulus Attackとは
分かりやすく解説してくれるサイトあったのでリンク[数学に自信がないハッカーでも以下略](https://whitemarkn.com/penetrationtest/common-modulus/)
この問題は、RSA暗号のCommon Modulus Attack（共通法攻撃）の亜種と、平文の構成方法を利用した数学的アプローチの組み合わせで解くことができます

### ソースコード理解
1. 初期設定
   ```python
    e1 = 65517
    e2 = 65577
    while True:
        p = getPrime(512)
        q = getPrime(512)
        if gcd((p-1)*(q-1), e1) == gcd((p-1)*(q-1), e2) == 1:
            break
    n = p * q
    ```
    1. 指数$e1$,$e2$の定義
    2. ```getPrime(512)```により、512bit,10進数で約154桁の素数を生成
    3. ```p```,```q```をそれぞれ-1した値を掛け合わせて指数との最大公約数を求める。その結果が$e1$と$e2$のどちらとも1であった場合、それを公開鍵の法(modulus)としている

2. メッセージのパディング
3. 暗号化と出力

## 解法