#Markshit of Student
print("Pass Mark for all subject is 32")

nepali = float(input("Obtained marks in Nepali:"))
eng = float(input("Obtained marks in English:"))
maths = float(input("Obtained marks in Maths:"))


total_mark_obt = nepali+eng+maths
percent_obt = float(total_mark_obt/3)

#Checking if student passed or failed
if nepali < 32 and eng < 32 and maths < 32 :
	print ("You failed All subject")
	pass
elif nepali < 32 and eng < 32 or eng < 32 and maths < 32 or nepali <32 and maths <32:
	print ("You failed in two subject")
	pass
elif nepali < 32:
	print("Fail in Nepali") 
	pass
elif eng < 32:
	print ("Fail in English")
	pass
elif maths < 32:
	print("Fail in Maths")
	pass
else:
	print("Congralution you passed all subject")

#checking divisions
if percent_obt >= 80:
	print("Distinction:" , percent_obt, "%")
elif percent_obt <= 79 and percent_obt>=50:
	print("Frist division", percent_obt, "%")
elif percent_obt <=49 and percent_obt >= 30:
	print("Third division", percent_obt, "%")
else:
	print("you have very low grades", percent_obt, "%")

print("Total Marks Obtained:", total_mark_obt)



