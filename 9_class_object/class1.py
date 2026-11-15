#class-> class is a blueprint of object
#object-> object is an instance of class
#attribute
#class attribute-> class attribute is a variable that is shared among all instances of a class
#instance attribute-> instance attribute is a variable that is unique to each instance of a class



class Student:
    school_name= "ABC School"  # class attribute
    shoe_color='black'

    def __init__(self,name,roll_no):
        self.name= name  # instance attribute
        self.roll_no= roll_no  # instance attribute


s1= Student('john',20)  # object creation
s2= Student('jane',22)  # object creation

print(s1.name)
print(s2.roll_no)