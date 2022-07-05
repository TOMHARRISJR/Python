
# JS - Array [ item,item,item]: Python - lists

grades = [ 9.4, 9.0 ,7.9 ]
#           0    1    2
print( grades )
print( len( grades ))

# Add an element to a list JS - .push(element): Python .append()
grades.append( 10.0)
print( grades )

grades_copy = grades #Reference to the previous array

grades_copy[0] = 4.5

grades_copy = grades[:]

print( grades_copy )
print( grades )

#Objects in Js are Dictionaries in Python

student = {
    "first_name" : "Tom",
    "last_name" : "Harris",
    "age" : 33,
}

print( student["first_name"])
l_n = "last_name"
print( student[l_n])

print(student)

# Tuple
course = ("Python", "5 weeks", "Tom Harris" )
print( course )





