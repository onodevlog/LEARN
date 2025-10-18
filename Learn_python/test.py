#問題1-1
scores = {"数学": 82, "国語": 74, "英語": 60, 
          "理科": 92, "社会": 70}

point_difference = scores["社会"] - scores["理科"]

answer = f"理科は社会より{point_difference}点高いです"
print(f"{point_difference}点")

#問題1-2
avg_score = sum(scores.values()) / len(scores)
print(f"{avg_score}点")

#問題2-1
year = 2025

if year % 400 == 0:
    print("閏年です")
elif year % 100 == 0:
    print("平年です")
elif year % 4 == 0:
    print("閏年です")
else:
    print("平年です")


#問題2-2
for number in range(1,101):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


#問題3-1
class Item:
    def __init__(self, id, name, price, purchase_price):
        self.id = id
        self.name = name
        self.price = price
        self.purchase_price = purchase_price
    
    def cost_rate(self):
        rate = self.purchase_price / self.price
        return rate

item_1 = Item("A001", "半袖クールTシャツ", 5000, 2250)
rate_1 = item_1.cost_rate()
print(rate_1)

item_2 = Item("A001", "半袖クールTシャツ", 6000, 2250)
rate_2 = item_2.cost_rate()
print(rate_2)