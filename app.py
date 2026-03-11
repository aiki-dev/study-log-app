from flask import Flask, render_template, request
import csv
from datetime import datetime

app = Flask(__name__)

#　"/"にアクセスした時の処理（GETは表示、POSTは送信）
@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    error = ""

    if request.method == "POST":
        study_date = request.form["study_date"]
        subject = request.form["subject"]
        study_time = request.form["study_time"]

        #　空欄チェック
        if not study_date or not subject or not study_time:
            error = "すべての項目を入力してください。"
        
        else:
            try:
                datetime.strptime(study_date, "%Y-%m-%d")
            except ValueError:
                error = "正しい日付を入力してください。"
            
            if error == "":
                if not study_time.isdigit():
                    error = "学習時間は整数で入力してください。"
                else:
                    study_time_int = int(study_time)
                    if study_time_int < 1 or study_time_int > 1440:
                        error = "学習時間は1~1440の範囲で入力してください。"
            if error == "":
                # CSVに追記保存（過去データを消さない）
                with open("study_log.csv", "a", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow([study_date, subject, study_time])

                message = f"{study_date} / {subject} / {study_time}分 を保存しました。"

    return render_template("index.html", msg=message, error=error)

#　このファイルを直接実行した時のみアプリ起動
if __name__ == "__main__":
    app.run(debug=True)
