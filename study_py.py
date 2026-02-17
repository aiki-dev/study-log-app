import os
days=int(input("何日分入力しますか？"))
total=0
for i in range(days):
    time=int(input(f"{i+1}日目の勉強時間（分）を入力してください→"))
    total+=time
average=total/days
print("合計勉強時間は",total,"分です")
print("平均勉強時間は",average,"分です")

filename="study_log.csv"
if not os.path.exists(filename):
    with open(filename,"w",encoding="utf-8") as f:
        f.write("days,total,average\n")

with open("study_log.csv","a",encoding="utf-8") as f:
    f.write(f"{days},{total},{average}\n")

print("study_log.csvに保存しました！")
