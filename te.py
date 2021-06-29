
#Scopes
'''
num = 10

def some_fun():
	global num # this is done to change value of global global variable 
	num+= 11
	print(f"inside:{num}")


print(f"outside: {num}")
some_fun()

'''


'''
#question 1
b = {"student": 
		[
			{
			"id":1,
			"name" : "Hari", 
			"parents":
					[
						{"relation": "father", "name": "Ram"}, 
						{"relation": "mother", "name": "Sita"},
					],
			},
		]
	}

name = b.get('student')[0].get('name') 
father = b.get('student')[0].get('parents')[0].get('name')
mother = b.get('student')[0].get('parents')[1].get('name')

print(f"{name} father name is {father}")
print(f"{name} mother name is {mother}")



#question 2
a = [1, 2, 4, {"one":[5,6, {"two":{"address": "Kathmandu"}}]}]

address = a[3].get('one')[2].get('two').get('address')

print(f"He lives in {address}")

'''