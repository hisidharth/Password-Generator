import random, string, os
password_length = int(input("How long is the password?Tell me in numbers"))
password_characters = string.ascii_letters + string.digits + string.punctuation
password = []
for x in range(password_length):
    password.append(random.choice(password_characters))
print(''.join(password))
os.system('pause')

