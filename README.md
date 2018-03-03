# PythonOmikuji
おみくじ

## 処理
randintメソッドを使用して1 ～ 6のランダムな数字を使って、おみくじの結果を出力します。

## コード
```
import random
omikuji = random.randint(1,6)
if omikuji == 1:
    print("大吉")
elif omikuji == 2:
    print("中吉")
elif omikuji == 3:
    print("小吉")
elif omikuji == 4:
    print("吉")
elif omikuji == 5:
    print("凶")
else:
    print("大凶")
```

## 出力結果  
```
大吉
```
  
## 開発環境
| 開発ツール |  |
|:-|:-|
| OS | Windows10 |
| 仮想化ソフト | Oracle VM VirtualBox 5.2 |
| 構築ソフト | Vagrant 2.0.2 |
| 仮想化上OS | CentOS 6.9 |
| SSHクライアント | PuTTY 0.6.8 |
| FTPクライアント | Cyberduck 6.3.5 |
| エディタ | Atom 1.24.0 |
| 開発言語 | Python 3.6.4 |
