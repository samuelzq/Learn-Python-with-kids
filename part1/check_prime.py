'''
Program to check whether a number is a prime
'''

number = int(input('Please input an integer: '))

if number == 1:
    print('1 is neither a prime nor a composite number.\n')
    exit()

remainder = 1
for factor in range(2, number):
    remainder = number % factor
    if remainder == 0:
        break;

if remainder == 0:
    print('Number %s is a composite number.\n' %number)
else:
    print('Number %s is a prime number.\n' %number)
