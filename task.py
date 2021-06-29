even_list=[]
odd_list=[]
main_list=[]
dup_list=[]

for i in range(10):
	data = int(input("Enter a number:"))
	if data in main_list:
		dup_list.append(data)
		pass
	else:
		main_list.append(data)

for check in main_list:
	if check%2==0:
		even_list.append(check)
	else:
		odd_list.append(check)

print(f"{main_list}:Inputs")
print(f"{dup_list}: Duplicate value")
print(f"{even_list}:Even number")
print(f"{odd_list}:Odd number")



