x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15
print(x)


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]

students[0]['last_name'] = 'Bryant'
print(students)

sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)


z = [{'x': 10, 'y': 20}]
z[0]['y'] = 30
print(z)

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

for i in range(len(students)):
    output = ''
    for key, value in students[i].items():
        output += f' {key} - {value}'
    print(output)

for i in range(len(students)):
    print(students[i]['first_name'])

for i in range(len(students)):
    print(students[i]['last_name'])

dojo = {
    ' locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    ' instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(dict):
    for each_key in dict:
        print(f"{len(dict[each_key])}{each_key.upper()}")
        for value in dict[each_key]:
            print(value)


printInfo(dojo)


# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
