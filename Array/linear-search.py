# linear search O(n), to get the maximal and minimal number
numbers = [2, 6, 7.8, 9, 10, -12, 10.5]

# Get maxmimal number from the array
max = numbers[0]
for num in numbers:
    if num > max:
        max = num
print('The maximal number is ' + str(max))

# Get the minimal number from the array
min = numbers[0]
for num in numbers:
    if num < min:
        min = num
print('The maximal number is ' + str(min))
