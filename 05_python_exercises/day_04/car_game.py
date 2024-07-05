# prices = [10, 20, 30]

# total = 0
# for price in prices:
#     total += price
# print(f"total is: {total}")

# printing the largest number in a list
# numbers = [1,2,3,5,6]
# max = numbers[0]

# for number in numbers:
#    if number > max:
#        max = number
# print(max) 

# || remove duplicates in a list

numbers = [1,1,1,1,3,44,5,6,7]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)