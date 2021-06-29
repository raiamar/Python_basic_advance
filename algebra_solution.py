from algebra_module import sol1

try:	
	a = float(input("Enter Value for a:"))
	b = float(input("Enter Value for b:"))

	print(sol1(a,b))
except ValueError as err:
	print("Use numbers, not alphabets")


