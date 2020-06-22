# twitter-bot-sample
twitter bot(2017年SFC webテキスト処理法の授業で作成)

# 概要
指定したアカウントのツイートを取得し、加工処理して定期的にツイートするpythonスクリプト

# Usage
## 準備
- Twitter Developer Accountを取得
- [Create New App]で新規appを作成する
- 各種Keyを取得
  - Consumer Key(API Key)
  - onsumer Secret(API Secret)
  - Access Token
  - Access Token Secret

## 指定したアカウントのツイートを取得
- twitter_crawl_sample.pyに各種Keyを書き込む
- python3 -m pip install tweepy
- python3 twitter_crawl_sample.py #引数1 #引数2 #引数3
  - 1.twitterのid(例: takapon_jp)
  - 2.取得する件数(例: 1000)
  - 3.出力先(例: out.txt)
> python3 twitter_crawl.py Idea_note123 1000 out.txt

## ツイートを加工
### 今回は各ツイートをコンマ区切りでテキストファイルに抽出
> ruby split.rb out.txt >> 出力先ファイル

- ツイートを足したい時は出力先にコンマ区切りで書き足す

### その他(任意)
-  クロールした時のナンバリングを削除
> cut -f2 入力ファイル > 出力ファイル

- RTが入ってる行を削除
> sed -i -e "/RT/d" ファイル

- @が入ってる行を削除
> sed -i -e "/@/d" ファイル

- httpが入ってる行を削除
> sed -i -e "/http/d" ファイル

- 行末にピリオドを追加
> sed -i -e "s/\$/./" ファイル

- 改行を削除
> cat 入力ファイル | tr -d '\r' | tr -d '\n' > 出力ファイル

## ツイートする
> python3 tweet_sample.py

## 自動で定期的に実行するようにする

> $crontab -e
```cron
* */5 * * * python3 -m pip install tweepy numpy --user && python3 ファイルへのパス/tweet.py
```
例は5時間ごと

# 参考
- このプログラムはSFCの授業「Webテキスト処理法」で[東中先生](https:- vu.sfc.keio.ac.jp/faculty_profile/cgi/f_profile.cgi?id=4be499caec70d42f)が作成されたものを使用しています。
- https://qiita.com/hikouki/items/e744b3a4d356d2af12cf