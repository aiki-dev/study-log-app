days=int(input("何日分入力しますか？→"))
total=0
for i in range(days):
    time=int(input(f"{i+1}日目の勉強時間（分）を入力してください→"))
    total+=time
average=total/days
print("合計勉強時間は",total,"です")
print("平均勉強時間は",average,"です")
