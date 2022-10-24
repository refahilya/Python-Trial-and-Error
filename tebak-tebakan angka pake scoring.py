#impor waktu dulu ya ges
import random
import time

#cara biar si lepi generate suatu angka sesuka dia
num = random.randint(1,100)

print("Hi.. my name is Mr. Leppy. I have chosen an integer number between 1-100. Can you guess what it is?")

time.sleep (1)

#masukin variabel
number = 0
score = 100

#nah ini loopingnya
while number != num and score > 0:
    number = int(input("Enter your guess number: "))
    if (number < num):
        print("Sorry, your guess number is too low")
        score -= 5
    elif(number > num):
        print("Sorry, your guess number is too high")
        score -= 5
    else:
        print("Yes, you're right. The number is ", number, "Congratulation!")
        score = score

#dann akhirnya kita rapotan
if (score ==0):
    print("GAME OVER")
    time.sleep (1)
    print("you've reached the limit of the score")
else:
    print("Your score is: ", score) 
