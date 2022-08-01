# 1. Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(num):  # created a function called countdown and gave it a parameter called (num)
    number = []    # created an empty list []
    for i in range(num, -1, -1):
        number.append(i)
    return number


print(countdown(5))

# 2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

list1 = [1, 2]


def print_return(list):
    print(list1[0])
    return list1[1]


print_return(list1)

list2 = [3, 5, 9]


def print_1(list):
    print(list2[0])
    print(list2[1])
    return(list2[2])


print_1(list2)


# 3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

x = [1, 2, 3, 4, 5]  # gave variable x  a list value [1,2,3,4,5]


def return_sum(list):
    return x[0] + len(x)


print(return_sum(x))

# 4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value.
# Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False.
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False


x = [5, 2, 3, 2, 1, 4]


def values_greater_than_second(list):
    list1 = []
    for i in range(len(x)):
        if x[i] > x[1]:
            list1.append(x[i])
    print(len(list1))
    return list1


print(values_greater_than_second(x))


# 5.This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size,
# and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]


# created a function named length_and_value and gave it the parameters (size,value)
def length_and_value(size, value):
    list1 = []                     # created an empty list[]
    for i in range(0, size):        # created a for loop and gave the range parameters(0,size)
        list1.append(value)        # adding value to list 1
    return list1                   # returning to list1


print(length_and_value(4, 7))
print(length_and_value(6, 2))
