import random

pwd = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?";:<>/{}[]()-_!@#$%^&*+=~|'

number = input('How many random passwords do you need: ')
number = int(number)

length = input('\nHow many characters of you password do you need: ')
length = int(length)

print('\nHere are some random passwords...\n')

for password in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(pwd)
    print(passwords)
