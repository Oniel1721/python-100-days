import random


letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!@#$%^&*()_+'
numbers = '1234567890'

def take(count, source):
    result = []
    while count > 0:
        index = random.randint(0, len(source)-1)
        result.append(source[index])
        count-=1
    return result

print("Welcome to the PyPassword Generator!")
print("How many letters would you like in your password?")
letters_count = int(input())
print("How many symbols would you like?")
symbols_count = int(input())
print("How many numbers would you like?")
numbers_count = int(input())

chars = take(letters_count, letters)
chars.extend(take(symbols_count, symbols))
chars.extend(take(numbers_count, numbers))
random.shuffle(chars)
password = ''.join(chars)
print(f"Here is your password: {password}")