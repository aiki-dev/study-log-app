#　何日分入力するか聞いて、数字に変換
days=int(input("何日分入力しますか？→"))

#　0以下だと計算できないので止める
if days <=0:
    print("１以上を入力してください")
    exit()

#　合計を入れるために最初は0にしておく
total=0

for i in range(days):
    #　iは0から始まるので+1して表示
    time=int(input(f"{i+1}日目の勉強時間（分）を入力してください→"))
    total+=time

average=total/days
print("合計勉強時間は",total,"です")
print("平均勉強時間は",average,"です")
