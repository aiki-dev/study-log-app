from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        study_time = request.form["study_time"]

        # CSVに保存
        with open("study_log.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([study_time])

        message = f"あなたは {study_time} 時間勉強しました"

    return render_template("index.html", msg=message)

if __name__ == "__main__":
    app.run(debug=True)
