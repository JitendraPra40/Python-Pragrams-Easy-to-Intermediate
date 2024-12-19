import random
import string

def password(pass_len):

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(pass_len))
    return password

pass_len = int(input('Enter desired length of password:'))
print(password(pass_len))