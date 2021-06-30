'''
class Games:
    def __init__(self, name, players):
        self.game_name = name
        self.num_of_player = players

    def a_message(self):
        print(f"Playing {self.game_name} is fun!!")

class Football(Games):
    def __init__(self, name, players):
        super().__init__(name, players)


    def num_of_players(self):
        print(f"In {self.game_name} there are {self.num_of_player} players in each team")

class Basketball(Games):
    def __init__(self,name, players):
        super().__init__(name, players)

    def num_of_players(self):
        print(f"In {self.game_name} there are {self.num_of_player} players in each team")


first_game = Football("Football", 11)
second_game = Basketball("Basketball", 5)
first_game.a_message()
first_game.num_of_players()
second_game.a_message()
second_game.num_of_players()
'''

'''
#overloading
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, object):
        return self.price == object.price

    def __add__(self, object):
        return self.price + self.price


pant = Product("Pant", 2000)
Tshirt = Product("Tshirt", 2000)

print(pant == Tshirt)
print(pant + Tshirt)
print(dir(int))
'''


'''
#Overriding

class Person:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking in child class")

class Teacher(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school #adding new attribute

    def walk(self):
        super().walk() #this code initilize walk function of parent class
        print(f"{self.name} is walking in parent class")

    def teaching(self):
        print(f"{self.name} is teaching at {self.school} for 10 years now")

t1 = Teacher("Bob", "xyz")
t1.walk()
t1.teaching()
'''

#Multilevel / multiple inheritance 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print(f"{self.name} is also studing  Physics from person class")

class Tutor(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def Teach(self):
        print(f"{self.name} also conducts home Tuition")

class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def work(self):
        print(f"{self.name} is {self.age} and work as part-time teacher.")

class Student(Teacher, Tutor): #multiple inheritance
    def __init__(self,name, age):
        super().__init__(name, age)

p1 = Student("Bob", 21)
p1.work()
p1.study()
p1.Teach()