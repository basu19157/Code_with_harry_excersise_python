# import random
# # user=input('choose any of the following:snake,water,gun:')
# no_of_tries=1
# score_user=0
# score_com=0

# while no_of_tries<9:
#     com=random.choice(["snake","water","gun"])
#     # print(com)
#     user=input('choose any of the following:snake,water,gun:')
#     if user=="snake":
#         if com=="water":
#             print (f"{user} wins")
#             score_user+=1

#         elif com==("gun"):
#             print(f"{com}wins")
#             score_com+=1
#         else:
#             print("draw")
#     elif (user=="gun"):
#         if com=="water":
#             print (f"{com} wins")
#             score_com+=1

#         elif com==("snake"):
#             print(f"{user}wins")
#             score_user+=1
#         else:
#             print("draw")
#     elif (user=="water"):
#         if com =="snake":
#             print (f"{com} wins")
#             score_com+=1

#         elif com==("gun"):
#             print(f"{user}wins")
#             score_user+=1
#         else:
#             print("draw")
#     no_of_tries+=1

import random
lst = ['s','w','g']

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print(" \t \t \t \t Snake,Water,Gun Game\n \n")
print("s for snake \nw for water \ng for gun \n")

# making the game in while
while no_of_chance < chance:
    _input = input('Snake,Water,Gun:')
    _random = random.choice(lst)

    if _input == _random:
        print("Tie Both 0 point to each \n ")

    # if user enter s
    if _input == "s" and _random == "g":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "s" and _random == "w":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter w
    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "w" and _random == "g":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter g

    elif _input == "g" and _random == "s":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")


    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    else:
        print("you have input wrong \n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game over")

if computer_point > human_point:
    print("Computer wins and you loose")

if computer_point < human_point:
    print("you win and computer loose")

print(f"your point is {human_point} and computer point is {computer_point}")


