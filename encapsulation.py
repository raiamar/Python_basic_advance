'''
#Encapsulation with access modifier (public, private, protected), getter and setter
#by default public, '-' protected, '--'private
class Student:
    __school = "abc academy"
    def __init__(self, name, age):
        self.newName = name
        self.__age = age

###################getter and setter for age##########################################
    @property
    def age(self):
        return self.__age

    @age.setter
    def age (self, newAge):
        self.__age = newAge

##########################getter and setter for new school##############################
    @property
    def school(self):
        return self.__school
    
    @school.setter
    def school(self, newSchool):
        self.__school = newSchool
    
###########################Instance method######################################################
    def currentAge(self):
        print(f"{self.newName} is {self.age} years old & goes to {self.school}")
    
    def previousAge(self):
        print(f"10 years back he was {self.age} years old & went to {self.school}")


s1 = Student("Bob", 20)
s1.currentAge()
s1.age = s1.age-10
s1.school = "XYZ School"
s1.previous Age()



###Inbulit decorators####

#@staticmethod
class Calculate:
    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor


    def divide(self):
        if Calculate.check_for_zero(self.divisor):
            return "Cannot use divisor as Zero"
        else:
            return self.dividend/ self.divisor
            pass

    @staticmethod
    def check_for_zero(num):
        return num == 0


value = Calculate(7, 0)
print(value.divide())

'''
#@classmethod

from datetime import date

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @classmethod #inbuilt decorators
    def birthYear(cls, name, yob):
        #return Student("Bob", 67)
        return cls(name, date.today().year - yob)


s1 = Student("Bob", 67)
print(s1.__dict__)

s2 = Student.birthYear("Mike", 1995)
print(s2.__dict__)
