from random import randint

randomNum = randint(1,100)
user = int(input("Enter the number: "))
guesses = 1

while(user != randomNum):
    if(user > randomNum):
        print("Lower number please")
        guesses += 1
    elif(user < randomNum):
        print("higher number please")
        guesses += 1
    user = int(input("Enter the number again: "))

print(f"OK so you have won and your total number of guesses is {guesses}")