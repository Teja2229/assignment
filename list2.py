list2 = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    list2.append(numbers)
print("Maximum element in the list is :", max(list2), "\nMinimum element in the list is :", min(list2))
