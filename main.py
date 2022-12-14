#print("hello hello NTUE!")

import random

low_bound = 1
up_bound = 100

answer = random.randint(low_bound, up_bound)

count = 5
while count:
    
    guess = int(input(f"Type your guess({low_bound}~{up_bound}): "))

    if guess < answer:
        low_bound = guess
    elif guess > answer:
        up_bound = guess
    else:
        print("You're corrects!")
        break
    
    count -= 1
