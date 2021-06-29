#scopes [Global & Local]
'''
#scope using global
num = 10
def outer_fun():
	global num
	num+=num
	return num
outer_fun()
print("outer", num)



#scope using nonlocal 
def outer_function():
	num=4
	def inner_fun():
		nonlocal num
		num+=2
		print("inner local:", num)
	inner_fun()
	
outer_function()
'''

#clouserrs 
'''
example1
def login(username):
	user = username
	if user:
		print(f"Welcome! {user}")

def home_page(fun):
	login(input("enter user name:"))
	print("home page>>>>..")

home_page(login)
'''


