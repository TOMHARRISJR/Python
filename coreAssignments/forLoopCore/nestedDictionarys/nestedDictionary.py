# x = [ [5,2,3], [10,8,9] ] 
# x[1][0] = 15
# print(x)

# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]

# students[0]['last_name'] = 'Bryant'
# print(students)




# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)

# z = [ {'x': 10, 'y': 20} ]
# z[0]['y'] = 30
# print(z)


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

for i in range(len(students)):
    output=''
    for k,v in students[i].items():
        output += f" {k} - {v}"
    print(output)
    











































































































































# def iterateDictionary(some_list):
#     for i in range(len(students)):
#         print(i)
#         print('\n'.join("{}: {}".format(k, v) for k, v in students[i].items()))
        




# iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# firsohn, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
# t_name - J

# def iterateDictionary2(key_name, some_list):
#     for i in range(len(some_list)):
#         print(students[i]['first_name'])
# iterateDictionary2('first_name',students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
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