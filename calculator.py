print("------------Guide to use calculator----------------")
print(''' 
	How to choose your option
		+[For-Addition]
		-[For-Subtraction]
		*[For-Multiplication]
		/[For-Division]
		exit[To-Exit-Program]
		''')

while True:
	num1 = int(input("Enter a number:"))
	num2 = int(input("Enter another number:"))
	op_list = ['+', '-', '*', '/', 'exit']
	option = input("Your option:")
	def calculate(num1, num2, option):
		if option in op_list:
			if option == '+':
				return (num1 + num2)
			elif option == '-':
				return(num1 - num2)
			elif option == '*':
				return(num1 * num2)
			elif option == '/':
				return(num1/num2)
			else:
				exit()
		else:
			print("Operation Not Possible")
			print("Try Again!!")
	Output = calculate(num1, num2, option)
	print("Answer:", Output)




 

'''a_list = ['+', '-', '/', '*']
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))

def cal_fun(num1, num2):
	for i in a_list:
		if i == '-':
			if num1 > num2:
				print("Difference:",num1-num2) 
			else:
				print("Difference:", num2 -num1)
		elif i == '+':
			print("Addition:", num1+num2)
		elif i == '/':
			print("Division:", num1/num2)
		else:
			print("Multiplication:",num1 * num2)

cal_fun(num1, num2)'''