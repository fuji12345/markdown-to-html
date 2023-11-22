# markdown-to-html
## 概要
- [https://recursionist.io/](Recursion)の課題で作成しました。
- マークダウン形式のファイルから、HTML形式のファイルを作成します。

## 環境の設定
poetryで管理しているので、以下でパッケージをインストールする。
```bash
poetry install
```

## 実行
- poetryの環境に入る。
```bash
poetry shell
```

- 実行
```bash
python main.py --input-path {マークダウンのファイルがあるパス} --output-path {作成したHTMLファイルを置くパス}
```
