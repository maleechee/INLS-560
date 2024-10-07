x = 1
# Using a while loop to print numbers [0:-5].
while x != -5:
    x = x - 1
    print(x)

count = 0
# Using a while loop to count to 5.
while count < 5:
    count += 1
    print(count)

# Using a while loop to empty a list (and print the items being removed).
list_ex = [120, 40, 30, 75, 84]
print(list_ex)

while list_ex.__len__() != 0:
    print(list_ex[0])
    list_ex.remove(list_ex[0])