#class-> class is a blueprint of object
#object-> object is an instance of class
#attribute
#class attribute-> class attribute is a variable that is shared among all instances of a class
#instance attribute-> instance attribute is a variable that is unique to each instance of a class
#method-> method is a function that is defined inside a class
#constructor-> constructor is a special method that is called when an object is created. It is used to initialize the attributes of the object.

#point to remember about self
#all instance methods must have self as their first parameter
#all instance attributes must be accessed using self
#all class attributes must be accessed using the class name



class Student:
    school_name= "ABC School"  # class attribute
    shoe_color='black'

    def __init__(self,name,roll_no):
        self.name= name  # instance attribute
        self.roll_no= roll_no  # instance attribute


    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, School Name: {Student.school_name}, Shoe Color: {Student.shoe_color}")



# s1= Student('john',20)  # object creation
# s2= Student('jane',22)  # object creation

# print(s1.name)
# print(s2.roll_no)

# s1.display()
# s2.display()


class Circle:
    pi=3.14

    def __init__(self,radius):
        self.radius=radius
    
    def calcualte_area(self):
        return self.pi * (self.radius**2)

    def calculate_circumference(self):
        return 2 * self.pi * self.radius


c1=Circle(5)
c2=Circle(10)

area1=c2.calcualte_area()
area1=Circle.calcualte_area(c2)  # class method calling using class name
print(area1)


"you"