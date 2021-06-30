'''
#example 1
#abstract method should always be overriding
#concreat method are commen and no need overriding
from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self): #abstract method 
        pass

    def work(self):
        print("Working") #concreat method

class Student(Father):
    def disp(self):
        print("Displaying in child class")

st = Student()
st.work()
st.disp()
'''

'''
#example 2
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def no_of_sides(self):
        pass
class Rectangle(Shape):
    def  no_of_sides(self):
        print("I am retangle and I have 4 sides")


class Triangle(Shape):
    def  no_of_sides(self):
        print("I am triangle and I have 3 sides")

t1 = Triangle()
r1 = Rectangle()
t1.no_of_sides()
r1.no_of_sides()
'''
#example 3
from abc import ABC, abstractmethod

class Defence(ABC):
    @abstractmethod
    def area(self):
        pass

    def gun(self):
        print("Gun: AKM")

class Army(Defence):
    def area(self):
        print("This is land defence")

class Navy(Defence):
    def area(self):
        print("This is sea defeance")

class Air_force(Defence):
    def area(self):
        print("This is air defence")

A = Army()
N = Navy()
AF = Air_force()
A.area()
A.gun()
N.area()
N.gun()
AF.area()
AF.gun()