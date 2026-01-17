// gcc -o chal main.c
#include <stdio.h>
#include <string.h>
#include <unistd.h>

/*
** 【脆弱性の解説】**

 このプログラムには「配列境界チェックの不備」による脆弱性があります。
 
 1. posの範囲チェックが不完全:
    - `if (pos >= 100)` は正の方向のみチェック
    - 負数（pos < 0）のチェックがない！
 
 2. 負数を入れると何が起きる？
    - shorts[100]は配列の先頭アドレスから始まる
    - shorts[-1] → 配列の1つ手前のメモリ（posやreturnアドレスがある場所）
    - shorts[-10] → さらに手前のスタック領域を書き換え可能
 
 3. 攻撃手法（Out-of-Bounds Write）:
    - スタック上のレイアウトを調べる（gdbなどで）
    - returnアドレスまでのオフセットを計算
    - posに負数を入力して、returnアドレスを上書き
    - win()関数のアドレスに書き換え → シェル起動
 
 4. short型の制約:
    - short = 2バイト（-32768～32767）
    - 1回の書き込みで2バイトずつ上書き
    - 64bitアドレス（8バイト）なら4回に分けて書き込む必要がある
*/

/*
** How to get the address of `win` **

  $ nm chal | grep win
  XXXXXXXXX

*/

// 【攻撃の目標】この関数を呼び出せればシェルが起動する
// nm chal | grep win でこの関数のアドレスを取得できる
void win() {
    execve("/bin/sh", NULL, NULL);
}

int main(void) {
    // スタックレイアウト（例）:
    // [低いアドレス]
    //   ...
    //   returnアドレス (8バイト) ← ここを書き換えたい！
    //   保存されたrbp (8バイト)
    //   pos (2バイト)           ← shorts[100]のすぐ後ろ
    //   shorts[99] (2バイト)
    //   shorts[98] (2バイト)
    //   ...
    //   shorts[0] (2バイト)
    // [高いアドレス]
    
    short shorts[100], pos;  // shorts配列200バイト + pos 2バイト

    /* disable stdio buffering */
    // バッファリング無効化 → 攻撃時に出力がすぐ見える（デバッグしやすい）
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

    printf("pos > ");
    scanf("%hd", &pos);  // %hd = short型（-32768～32767）
                          // 負数も入力可能！
    
    // 【脆弱性の核心】pos >= 100 だけチェック → 負数が素通り！
    if (pos >= 100) {
        puts("You're a hacker!");
        return 1;
    }
    // 正しいチェック例: if (pos < 0 || pos >= 100) { ... }
    
    printf("val > ");
    // posが負数の場合、配列の境界外（手前）に書き込める
    // 例: pos=-5 → shorts[-5]に書き込み（配列の10バイト手前）
    scanf("%hd", &shorts[pos]);  // ← Out-of-Bounds Write発生！

    return 0;
}

