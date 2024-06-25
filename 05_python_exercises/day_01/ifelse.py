weight = int(input("Enter Weight: "))
unit = input("(K)g or (L)bs: ")

if unit == "K" or "k":
    print(f"weight in Kg: {weight}")
elif unit == "L" or "l":
    print(f"weight in Lbs is: ")
else:
    print("input a valid weight")
