from flask import Flask, render_template, request
import csv
import os
from datetime import datetime

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CSV_PATH = os.path.join(BASE_DIR, "study_log.csv")
app.config["CSV_PATH"] = DEFAULT_CSV_PATH

#　"/"にアクセスした時の処理（GETは表示、POSTは送信）
@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    error = ""
    records = []
    search_subject = ""
    search_from = ""
    search_to = ""

    search_subject = request.args.get("search_subject", "")
    search_from = request.args.get("search_from", "")
    search_to = request.args.get("search_to", "")

    if search_from and search_to and search_from > search_to:
        error = "日付の範囲が正しくありません。"

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
                with open(app.config["CSV_PATH"], "a", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow([study_date, subject, study_time])

                message = f"{study_date} / {subject} / {study_time}分 を保存しました。"

    # CSVからデータを読み込む
    if os.path.exists(app.config["CSV_PATH"]):
        with open(app.config["CSV_PATH"], "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    record_date = row[0]
                    record_subject = row[1]
                    record_time = row[2]

                    if search_subject and search_subject not in record_subject:
                        continue

                    if search_from and record_date < search_from:
                        continue

                    if search_to and record_date > search_to:
                        continue

                    records.append({
                        "study_date": record_date,
                        "subject": record_subject,
                        "study_time": record_time
                    })
    return render_template(
        "index.html",
        msg=message,
        error=error,
        records=records,
        search_subject=search_subject,
        search_from=search_from,
        search_to=search_to,
    )

#　このファイルを直接実行した時のみアプリ起動
if __name__ == "__main__":
    app.run(debug=True)
