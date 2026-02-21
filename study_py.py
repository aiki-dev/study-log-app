import os  #　ファイルが存在するか確認するために使う

days=int(input("何日分入力しますか？"))
total=0
for i in range(days):
    #　iは0から始まるので+1して表示
    time=int(input(f"{i+1}日目の勉強時間（分）を入力してください→"))

    #　毎日の時間を合計に足していく
    total+=time

average=total/days
print("合計勉強時間は",total,"分です")
print("平均勉強時間は",average,"分です")

filename="study_log.csv"

#　ファイルがまだ無い場合だけ作る
if not os.path.exists(filename):

    #　新しくファイルを作って、項目名を書く
    with open(filename,"w",encoding="utf-8") as f:
        f.write("days,total,average\n")

#　追記モードでデータを保存（前のデータは消えない）
with open("study_log.csv","a",encoding="utf-8") as f:
    f.write(f"{days},{total},{average}\n")

print("study_log.csvに保存しました！")
