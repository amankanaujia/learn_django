import random

print('Welcome to the password generator\n')
chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM`~1234567890-=!@#$%^&*()_+[];\'\,./{}:"|<>?'
number = int(input('Amount of passwords to generate : '))
length = int(input('length of password : '))
print('Here are your passwords: \n')
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
