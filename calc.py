# Taking input from users
num1 = input ("Enter a number: ")
num2 = input ("Enter another number: ")

# Convert string input to int
n1 = int(num1)
n2 = int(num2)

#checking type
print(type(n1), type(n2))

#performing calculation
add=n1+n2
sub=n1-n2
div=n1/n2
mul=n1*n2

#Output
print("Sum of two numbers:", add, "\n" "Difference of two numbers:", sub, "\n"
	"Product of two numbers:", mul, "\n" "Division of two numbers:", div)


