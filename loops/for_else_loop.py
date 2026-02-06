numbers=[10,20,30,40]

f_number=int(input("Enter the number you want to search: "))

for x in numbers:
    if x == f_number:
        print(f"Number {f_number} is found in the list")
        break

else :
    print(f"Number {f_number} is not found in the list")

