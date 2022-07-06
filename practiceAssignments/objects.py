from inspect import Attribute



class Student:
    
    def __init__( self, first_name, last_name, age, instructor,course ):  # Constructor -purpose of constructor is to build an object.(students characteristics)                              
        #attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.instructor = instructor
        self.course = course
    
    def print_info( self, message ):
        #Method
        print( message )                                                 
        print( f"name: {self.first_name}")
        print( f"age: {self.age}")
        print(f"instructor: {self.instructor}")
        print( f"course {self.course}")    

class Course:
    def __init__(self, data): 
        self.name = data["name"]
        self.instructors = data["intructors"]
        self.program = data["program"]

python = {
    "name" : " Python/Flask",
    "instructors" : ["Alfred","Tom", "Tyler"],
    "program": "full stack"
}

course_python = Course( python )        



student_alex = Student( "Alex", "Miller", 20, "Nichole","Web Fundamentals" ) #Creating an object/ making an instance of the student class                           
student_martha = Student( "Martha", "Miller", 29, "Nichole","Web Fundamentals" )

student_alex.print_info( "Hey there!")

student_martha.print_info("Hello!")

list_students = []
list_students.append( student_alex )
list_students.append( student_martha )

for student in list_students:
    student.print_info( "Hey there!" )


