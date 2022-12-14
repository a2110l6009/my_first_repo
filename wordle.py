
import random

with open("words.txt") as f:
    dictionary = f.read().splitlines()


answer = random.choice(dictionary)

print(answer)

count = 5
while count > 0:
    
    guess = input(f"Type your guess: ")

    result = ""
    for i in range(5):
        #print(guess[i], answer[i])
        if guess[i] == answer[i]:
            #print("A", end=" ") #是否存在
            result = result + "A"
        elif guess[i] in answer:
            #print("B", end=" ")
            result = result + "B"
        else: #都不存在
            #print("X", end=" ")
            result = result + "X"
    
    if result == "AAAAA":
        print("Correct!")
        break
    
    print(result)

    
    
    count -= 1


