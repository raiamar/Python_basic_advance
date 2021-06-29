print(""" -------------Welcome to simple python quiz game---------------------
		###Rules to follow 
			!Answer must be according to question
			!Right answer to Each question is 2Points
			!No points for wrong answer
	""")

name = input("Enter Your name:")
q1 = """Print 'Hello World' Using Python"""
q2 = """ if a = '1234abc'. What is output of a.isalnum()? """
q3 = """Is python a server-side programming language"""
q4 = """write syntax for a function with function name example"""
q5 = """if a = "aeiou". What is output of "-".join(a)? """
E = "Thank You!!!"
total = 0
correct = 0
wrong = 0
q_list= [q1, q2, q3, q4, q5, E]

while True:
	def calculate(q_list, total, correct, wrong):
		for i in q_list:	
			if i == q_list[0]:
				print(q_list[0])
				ans = input("Your Answer:")
				if ans == "print('Hello World')":
					print("You are Correct")
					total+=2
					correct+=1
					pass
				else:
					wrong+=1
					print("Wrong Answer")
					print("Answer: print('Hello World')")

			elif i == q_list[1]:
				print(q_list[1])
				ans = input("Your Answer:")
				if ans == "True" or ans == "true":
					print("You are Correct")
					total+=2
					correct+=1
					pass
				else:
					wrong+=1
					print("Wrong Answer")
					print("Answer: True")

			elif i == q_list[2]:
				print(q_list[2])
				ans = input("Your Answer:")
				if ans == "Yes" or ans == "yes":
					print("You are Correct")
					total+=2
					correct+=1
					pass
				else:
					wrong+=1
					print("Wrong Answer")
					print("Answer: Yes")

			elif i == q_list[3]:
				print(q_list[3])
				ans = input("Your Answer:")
				if ans == "def example():":
					print("You are Correct")
					total+=2
					correct+=1
					pass
				else:
					wrong+=1
					print("Wrong Answer")
					print("Answer: def example():")

			elif i == q_list[4]:
				print(q_list[4])
				ans = input("Your Answer:")
				if ans == "a-e-i-o-u":
					print("You are Correct")
					total+=2
					correct+=1
					pass
				else:
					wrong+=1
					print("Wrong Answer")
					print("Answer: a-e-i-o-u")

			elif i == q_list[5]:
				print(f"{E} {name} Your total Score is: {total}")
				print(f"You Have right answer to {correct} question")
				print(f"You Have wrong answer to {wrong} question")
				exit()

	Answer = calculate(q_list, total, correct, wrong)

