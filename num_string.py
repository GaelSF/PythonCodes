import random
import string
for i in range(100):

	account_number = ''.join(random.choice(string.digits) for _ in range(16))
	print(account_number)
	
