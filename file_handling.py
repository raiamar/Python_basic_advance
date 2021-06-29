#There are three mode of file handling
#"r" = read
#"w" = write /also create new file if doesnot exit
#"a" = append 

'''
#write example
try:
	f = open("text.txt", "w")
except FileNotFoundError as err:
	print("File doesn't exist")
else:
	print(f.write("I have created a new file"))
finally:
	f.close()
'''

'''
#read example
try:
	f = open("text.txt", "r")
except FileNotFoundError as err:
	print("File doesn't exist")
else:
	print(f.read())
	#can also use print(f.readline()) to read only first line
	#or f.lines() to get lines in list
finally:
	f.close()
'''

'''
#append example
try:
	f = open("text.txt", "a")
except FileNotFoundError as err:
	print("File doesn't exist")
else:
	print(f.write("I have  added a new text."))
finally:
	f.close()
'''