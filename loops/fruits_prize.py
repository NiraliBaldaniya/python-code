fruits = ["Apple", "Banana", "Orange", "Grapes"]
prices = [30, 10, 25, 40]

for fruits, price in zip(fruits, prices):
    print(f"{fruits} costs {price} rupees")
