print("こんにちは！")

print("あいうえお")
print("かきくけこ")
print("さしすせそ")

print(1000 + 2000 + 3000 + 4000 + 5000 + 6000 + 7000 + 8000 + 9000)
#数式が長いと読みずらいので、()で囲み、適度に改行
print(1000 + 2000 + 3000 + 4000 + 5000 
 + 6000 + 7000 + 8000 + 9000)

#変数
apple_price = 150
#変数に入れた値は後から変更が可能
#apple_priceの値が150→200に変更
apple_price = 200

#変数のルール
#変数名は全て小文字
#単語同士はアンダーバーで繋げる

print(apple_price)

x = 10
y = 100
x = y
print(x)


#変数の型について

#整数型→int
apple_price = 120
#文字列型→string
name = "小野"
#浮動小数点型→float
weight = 55.5

#変数の型は値が代入されたタイミングで自動で決まる

#型によって出来ることが違う
#同じ命令でも方によって動作が違う
# x = 100
# y = 200
# z = x + y → 300 (足し算)
# x = "100"
# y = "200"
# z = x + y → 100200 (文字列結合)

#変数の型を調べたい→typeを使う
x = 100
x_type = type(x)
print(x_type)

#型を変換する
#int型に変換 int(値・変数)
#string型に変換 str(値・変数)
#float型に変換 float(値・変数)
x = "10"
y = int(x) #数値に変換できない文字(a,b,c等)だった場合はエラー

print(apple_price, name, weight)

a_type = type(apple_price)
n_type = type(name)
w_type = type(weight)

print(a_type,n_type,w_type)

#割り算の余り
print(10%4)

math = 82
japanese = 74
english = 60
avg_score = ( math + japanese + english) / 3
print(avg_score)

surname = "小野"
given_name = "泰照"
full_name = surname + given_name
print(full_name)

#f-string(変数埋め込み)
price = 100
text = f"この商品は{price}円です"
print(text)

student_names = ["斎藤", "小林", "佐々木", "田中"]
print(student_names[3])
a = student_names[1]
b = student_names[-3]
print(a, b)

x = ["a", "b", "c", "d", "e", "f", "g"]
y = x[1:3]
print(y)
y = x[:3]
print(y)
y = x[5:]
print(y)

#リストの長さを取得
y = len(x)
print(y)

#リストの結合(新しいリストが作成される)
x = ["a", "b"]
y = ["A", "B"]
z = x + y
print(z)

#要素の追加(リスト自体が変更される)
z.append("C")
print(z)

#要素の削除
z.remove("b")
print(z)

a = [20, 12, 40]
x = max(a)
y = min(a)
z = sum(a)
print(x, y, z)

#小さい順に並び変えたリストを取得
x = sorted(a)
y = sorted(a, reverse=True)
print(x, y)

scores = [82, 74, 60]
avg_score = sum(scores) / len(scores)
print(avg_score)

scores.append(92)
scores.append(70)
avg_score = sum(scores) / len(scores)
print(avg_score)

#{"key": value}
scores = {"数学": 82,
          "国語": 74,
          "英語": 60,
          "理科": 92,
          "社会": 70}
#keyを指定して、valueの値を取得
# x = 辞書.get(key)
science = scores.get("理科")
print(science)

#要素の値(value)を変更
# 辞書[key] = 新しい値
scores["国語"] = 100
print(scores)

#同じkeyの要素を複数持つことは出来ない
prices = {"いちご": 540, "いちご": 490}
print(prices)
#後に書いたほうが残る　"いちご": 490

x = len(scores)
print(x)

#keyの値だけ取り出す
x = scores.keys()
print(x)
x = list(scores.keys())
print(x)

#valueの値だけ取り出す
y = scores.values()
print(y)


#集合とタプル

#集合　順序を持たない、つまりインデックスがない
x = {1, 2, 4}

#要素を追加
x.add(7)
print(x)

#要素を削除　2つ方法がある
x.discard(7) #指定した値がなくてもエラーにならない
x.remove(4) #指定した値がないとエラーになる
print(x)

x = {0, 1, 3, 6}
y = {0, 2, 5, 6}
z = x | y #和集合
print(z)
z = x - y #差集合
print(z)
z = x & y
print(z)

#タプル 順序を持つ
x = (1, 2, 4)
y = x[2]
print(y)

#インデント
#1インデント→半角スペース4つ

#if 条件式:
#    条件式がTrueの時の処理
login_cnt = 1

if login_cnt == 1:
    print("初回ログインユーザです")

login_cnt = 2

if login_cnt != 1:
    print("初回ログインユーザではないです")


fruits = ["バナナ", "リンゴ", "モモ"]
x = "リンゴ"

if x in fruits:
    print("OK")

age = 20
login_cnt = 1

if age >= 20 and login_cnt == 1:
    print("合格")

age = 19

if age >= 20:
    print("成人です")
elif age >= 18: #ifがFalseの場合に実行
    print("成人ですが、飲酒はできません")
elif age >= 6:
    print("子供です")
else:
    print("乳児・幼児です")


scores = [90, 30, 49]

for x in scores:
    print(x+1)


fruits = {"apple": 130, "banana": 350, 
          "lemon": 100}

for name, price in fruits.items():
    print(name)
    print(price)
    print(f"{name}は{price}円です")


for x in range(1, 6):
    print(f"発射まで{x}秒前です")


numbers = [10, 21, 100, 18, 2]

for n in numbers:
    if n >= 100:
        break
    print(f"{n}:繰り返し")
print("for分の外")

numbers = [10, 21, 32, 65]

for n in numbers:
    print(f"{n}: 前処理")
    if n %2 == 0:
        continue
    print(f"{n}: 後処理")


def print_hello():
    print("こんにちは")

print_hello()


#位置引数での記述
def add_sub_numbers(a, b):
    c = a + b
    d = a-b
    return c, d

added, subed = add_sub_numbers(10, 100)

#キーワード引数での記述
def add_numbers(a, b):
    c = a + b
    return c

added = add_numbers(b=10, a=100)


def is_leap_yeas(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
year = 2025
result = is_leap_yeas(year)
print(result)


class User:
    def __init__(self, name, mail_address, point):
        self.name = name
        self.mail_addess = mail_address
        self.point = point

    def add_point(self, point):
        self.point = self.point + point

user_1 = User("佐藤葵", "sato@example.com", 500)
user_1.add_point(100)
print(user_1.point)

user_2 = User("小林ゆい", "kobayashi@exampke.com", 1000)
user_2.add_point(100)
print(user_2.point)


from my_module import print_module, add_numbers

print("script 開始")
print_module()
print(add_numbers(1,2))
print("script 終了")

from my_packeges.my_module import print_module as pm

print("script 開始")
pm()
print("script 終了")

#標準モジュールの使用
from datetime import datetime

t = datetime.today()
print(t)


import matplotlib.pyplot as plt

label = ["A", "B", "C", "D"]
num = [20, 17, 25, 9]
plt.bar(label, num)
plt.savefig('./bar.png')