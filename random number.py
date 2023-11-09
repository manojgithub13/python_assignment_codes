import random

min_num = 1
max_num = 100
random_number = random.randint(min_num, max_num)
attempts = 0

while True:

        guess = int(input('Enter your guess: '))
        attempts += 1

        if guess > random_number:
            print('Too high!')
        elif guess < random_number:
            print('Too low!')
        elif guess==random_number:
            print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")
            break
        else:
            print('invalid error')
   
