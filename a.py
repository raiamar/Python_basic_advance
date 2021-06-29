email_list = ["abc@gmail.com", "abc@yahoo.com", "abc@hotmail.com"]


a = list(map(lambda g:g.split('@'), email_list))
print(a)

'''
email_list = ["abc@gmail.com", "abc@yahoo.com", "abc@hotmail.com"]


a = list(map(lambda g:g.split('@')[1], email_list))
print(a)
'''