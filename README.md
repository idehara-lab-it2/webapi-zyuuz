# iTunes の検索 web API を叩いてみよう

## 叩き方：

`https://itunes.apple.com/search?` の後に、必要なパラメータを `key=value` の形で並べる。（HTTP の `get` メソッド）

それぞれのパラメータは `&` で区切る

* [叩き方](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/Searching.html#//apple_ref/doc/uid/TP40017632-CH5-SW1)
* [サンプル](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/SearchExamples.html#//apple_ref/doc/uid/TP40017632-CH6-SW1)

## 結果

* [呼び出し結果](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/UnderstandingSearchResults.html#//apple_ref/doc/uid/TP40017632-CH8-SW1)

実際にブラウザのアドレスに入れてみると、結果が見られる。

```
{
 "resultCount":50,
 "results": [
{"wrapperType":"track",
```

で始まることから、`data['results'][0]` などでアクセスできることが分かる。

# repl.it との連携

## repl.it のアカウント登録

[repl.it](https://replit.com/) から、多摩大学のアカウントでユーザ登録する。

## GitHub リポジトリとの接続

[repl.it](https://replit.com/) から、「New Repl」→「Import from GitHub」と進み、github のリポジトリのアドレスを指定する。

## ファイルのコミット・プッシュ

[repl.it](https://replit.com/) でファイルを変更すると、左の「Version Control」タブから、Commit and Push ボタンが押せるようになる。送り先のブランチも選べる。

# 課題

1. 検索結果の一番最初の１個について、`collectionName` と `trackName` を表示してみよう。
1. できる人は、検索結果のすべてについて、`collectionName` と `trackName` を表示してみよう。（加点対象外）
1. ものすごくできる人は、検索結果の `collectionName` を、重複を取り除いて表示してみよう。（加点対象外）
