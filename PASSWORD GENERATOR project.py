import random
import string

def get_random_password(length):
       letters = string.ascii_lowercase
       result_password = ''.join(random.choice(letters) for i in range(length))
       print(result_password)
   
get_random_password(8)



















