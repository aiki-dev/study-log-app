from flask import Flask, render_template, request
import csv

app = Flask(__name__)

#　"/"にアクセスした時の処理（GETは表示、POSTは送信）
@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        study_time = request.form["study_time"]

        # CSVに追記保存（過去データを消さない）
        with open("study_log.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([study_time])

        message = f"あなたは {study_time} 時間勉強しました"

    return render_template("index.html", msg=message)

#　このファイルを直接実行した時のみアプリ起動
if __name__ == "__main__":
    app.run(debug=True)
