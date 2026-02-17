# 学習ログアプリ

PythonとFlaskを使って作成した、学習時間を記録するWebアプリです。

## 作成目的
日々の勉強時間を記録し、継続的に学習できるようにするために作成しました。
Webアプリの基本構造（フロントエンドとバックエンドの連携）を理解することも目的としています。

## 使用技術
- Python
- Flask
- HTML
- CSVファイル
- Git / GitHub

## 機能
- 学習時間の入力フォーム
- POST送信によるデータ受け取り
- CSVファイルへの保存
- 入力後にメッセージ表示

## 工夫した点
- FlaskのGET/POSTの流れを理解しながら実装しました。
- データをCSVに保存することで、簡単なデータ管理ができるようにしました。

## 起動方法（Windows）

1. 仮想環境を作成
   python -m venv venv
2. 仮想環境を有効化
   venv\Scripts\activate
3. Flaskをインストール
   pip install flask
4. アプリを起動
   python app.py
5. ブラウザでアクセス
   http://127.0.0.1:5000
