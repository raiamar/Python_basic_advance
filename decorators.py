#example 1
#This type of function in Clouser
"""
def mult(n):
	def times(a):
		return n*a
	return times

times = mult(5)
print(times(5))


Output=25
"""


#example 2
'''
def login(username):
	name = username
	if name:
		print('welcome!', name)
	else:
		print('Try Aganin!')

def home_page(fun):
	fun(input("Enter your name:"))
	
home_page(login)
'''


##Starting decorators 
'''
def decorators_funs(func):
	def wrapper():
		print('This is before function')
		func()
		print('this is after function')
	return wrapper

def example():
	print("This is an example")

a =  decorators_funs(example) #=> wrapper
a()
'''

#Other way to use decorator
'''
def decorator_func(fun):
	def wrapper():
		print('This is before function')
		fun()
		print('this is after function')
	return wrapper

@decorator_func
def example():
	print('this is other example!!!')

example()
'''


#next example
def smart_division(div):
	def wrapper(dividend, divisor):
		if divisor == 0:
			return "cannot Divide"
		else:
			return div(dividend, divisor)

	return wrapper

@smart_division
def division(dividend, divisor):
	return dividend/divisor

print(division(23,78))
print(division(23,0))