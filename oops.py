 #oop is programming representation of real life objects/entity
 #class are bluprint for objects.
 #objects are entity that has state and behaviour.


'''
 #example for classs and object

class AnimeChar:
#class/static variables
	country= "Japanese"

	#initialization
	def __init__(self, name, anime, age):
		self.name = name
		self.anime = anime
		self.age = age   #this are instance variables

	def charDetails(self):
		#instance method
		print(f"{self.name} is {self.age} years, {self.country} character from {self.anime}")


onePiece = AnimeChar("Luffy", "One Piece", "19")
naruto = AnimeChar("Naruto", "Naruto",32)
rentG = AnimeChar("Chizuru Ichinose", "Rent a girlfriend", "20")
Hana = AnimeChar("Hana", "Hana Shirosaki", "15")

 #to print all data we can do 
print(onePiece.__dict__)
naruto.charDetails()
onePiece.charDetails()
rentG.charDetails()
Hana.charDetails()
'''

'''
#example for encapsulation, access modifer, accesser(getter), mutator(setter)

class Student:
	school = "XYZ Int"

	def __init__(self, _id, name, age, _class, parents, title, relation):
		self._id = _id
		self.name = name
		self.age = age
		self._class = _class 
		self.__parents = parents #name mangelling
		self.__title = title
		self._relation = relation #"-" this is protected

		#here we are using access modifer "__" to make private variable 


	#getter and setter for parent name
	def  get_std_parent(self):
		return self.__parents

	def set_std_parent(self, parents):
		self.__parents = parents


	#getter and setter for parent title
	def get_title(self):
		return self.__title

	def set_title(self, title):
		if title == "Mr" or title == "Mrs":
			self.__title = title
		else:
			print("Make use of proper title [Mr/Mrs]")

################################This is actually the corret way to use getter and setter function#################
####For relation#######

	@property
	def relation(self):
		return self._relation


	@relation.setter
	def relation(self, nRelation):
		self._relation = nRelation



	def stdDetails(self):
		print(f"{self.name} is {self.age} years old. He goes to {self.school} and study in class {self._class }. {self.get_title()} {self.get_std_parent()} is his {self.relation}.")



s1 = Student("010", "Bekam", 16, "X", "David", "Mr", "Father")


print("---------------------First Outcome-----------------------------")
s1.stdDetails()


s1.set_title("Mrs")
s1.set_std_parent("Joya")
s1.relation("Mother")
print("--------------------------Changing parent name-------------------")
s1.stdDetails()

'''


#abstract 
from abc import ABC, abstractmethod

class Shape(ABC):
	@abstractmethod
	def no_of_sides(self):
		pass

class Rectangle(Shape):
	def no_of_sides(self):
		print("I have 4 sides")


class Triangle(Shape):
	def no_of_sides(self):
		print("I have 3 Sides")


t1 = Triangle()
r1 = Rectangle()

t1.no_of_sides()
r1.no_of_sides()