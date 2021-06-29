#using Lambda function
'''
sol1 = (lambda a, b: a**2 +2*a*b +b**2)

print(sol1(4,6))
'''



#using map to find @..mail only
'''
email_list = ["abc@gmail.com", "abc@yahoo.com", "abc@hotmail.com"]


a = list(map(lambda g:g.split('@')[1], email_list))
print(a)
'''


#Filter

email_list = ["a@gmail.com", "a@yahoo.com", "a@hotmail.com", "b@gmail.com", "c@gmail.com"]

ans = list(filter(lambda mail:mail.endswith('@gmail.com'), email_list))
print(ans)
