#modules

import random
import time

#functions

def dots():
    for i in range(3):
        time.sleep(1)
        print('.')

def symbols():
    for j in range(20):
        time.sleep(0.25)
        list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        random = random.choice(list)
        print(random)

#Introduction

print("Hello, I'm Joe, and we'll play for money!")
time.sleep(2)
print()
char_name = input('Type your name: ')
print()
print('Nice to meet you,' ,char_name )
time.sleep(1)
print('Let me tell you the rules: Here we will play with cubes. I will roll the dice once, and you will have 5 attempts to get my number. There is no logic here, only randomness')
time.sleep(4.50)

#Joe's cube

jo_cube = random.randint(1,5)
time.sleep(1)
print('Joe drops cube')
time.sleep(1)
print("Joe's number: " ,jo_cube )
time.sleep(1)

#First

cube1 = input('Do you want drop cube?(yes or yes): ')
if cube1 == "yes" or cube1 == "Yes":
    ran1 = random.randint(1,5)
    time.sleep(1)
    print(char_name,' drops cube')
    time.sleep(1)
    symbols()
    time.sleep(1)
    print('Your number: ' ,ran1 )
    if ran1 == jo_cube:
        print('Good Job!')
    else:
        print('You loose')
else:
    dots()
    time.sleep(1)

#Second

cube2 = input('Do you want drop cube?(yes or yes): ')
if cube2 == "yes" or cube2 == "Yes":
    ran2 = random.randint(1,5)
    time.sleep(1)
    print(char_name,' drops cube')
    time.sleep(1)
    symbols()
    time.sleep(1)
    print('Your number: ' ,ran2 )
    if ran2 == jo_cube:
        print('Good Job!')
    else:
        print('You loose')
else:
    dots()
    time.sleep(1)
    

#Third

cube3 = input('Do you want drop cube?(yes or yes): ')
if cube3 == "yes" or cube3 == "Yes":
    ran3 = random.randint(1,5)
    time.sleep(1)
    print(char_name,' drops cube')
    time.sleep(1)
    symbols()
    time.sleep(1)
    print('Your number: ' ,ran3 )
    if ran3 == jo_cube:
        print('Good Job!')
    else:
        print('You loose')
else:
    dots()
    time.sleep(1)

#Fourth

cube4 = input('Do you want drop cube?(yes or yes): ')
if cube4 == "yes" or cube4 == "Yes":
    ran4 = random.randint(1,5)
    time.sleep(1)
    print(char_name,' drops cube')
    time.sleep(1)
    symbols()
    time.sleep(1)
    print('Your number: ' ,ran4 )
    if ran2 == jo_cube:
        print('Good Job!')
    else:
        print('You loose')
else:
    dots()
    time.sleep(1)

#Fifth

cube5 = input('Do you want drop cube?(yes or yes): ')
if cube5 == "yes" or cube5 == "Yes":
    ran5 = random.randint(1,5)
    time.sleep(1)
    print(char_name,' drops cube')
    time.sleep(1)
    symbols()
    time.sleep(1)
    print('Your number: ' ,ran5 )
    if ran5 == jo_cube:
        print('Good Job!')
    else:
        print('You loose')
else:
    dots()
    time.sleep(1)
    
#Final

if ran1 == jo_cube or ran2 == jo_cube or ran3 == jo_cube or ran4 == jo_cube or ran5 == jo_cube:
    print('You beat me..')
    time.sleep(1)
    print('You quickly take the gun from the table and shoot Joe.')
    time.sleep(1)
    print('Good End')
    time.sleep(1)
    g_end = ['You won the round, not the game...', 'Live happily', 'Forget everything that happened to you']
    g_rand = random.choice(g_end)
    print(g_rand)
else:
    print('You loose')
    time.sleep(2)
    print('A bullet hit you')
    time.sleep(1)
    print('Bad End')
    time.sleep(1)
    b_end = ["Everything ends where it begins', 'It's a vicious circle, you know?', 'You're always under threat"]
    b_rand = random.choice(b_end)
    print(b_rand)

input('Press "Enter" to exit')
