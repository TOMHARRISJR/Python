for i in range(0, 151):
    print(i)

for i in range(5, 1005, 5):
    print(i)

for i in range(1, 101):
    if i % 10 == 0:
        print("Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)


finalSum = 0
for num in range(0, 500000):
    if num % 2 != 0:
        finalSum = finalSum + num
        print(finalSum)

for i in range(2018, 4, -4):
    print(i)


lowNum = 2
mult = 3
highNum = 9
for num in range(lowNum, highNum+1):
    if num % mult == 0:
        print(num)
