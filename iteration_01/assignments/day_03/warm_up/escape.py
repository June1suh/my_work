def escape_the_loop():
    x=10
    while True:
        import random
        ask=input("Which action would you like to choose?: ")
        if ask=="rest":
            x+=2
            print(f"You've earned 2 energy points, your current energy point is {x}")
        elif ask=="guess":
            random=random.randint(1,5)
            ask_guess=input("What is your guess between 1 to 5?: ")
            if ask_guess==random:
                x+=5
                print(f"You've earned 5 energy points, your current energy point is {x}")
            else:
                x-=2
                print(f"You've lost 2 energy points, your current energy point is {x}")
        elif ask=="move":
            roll=random.randint(1,100)
            if roll<=50:
                x-=2
                print(f"You've lost 2 energy points, your current energy point is {x}")
            elif roll>50 and roll<=80:
                print(f"Nothing Happened, your current energy point is {x}")
            else:
                x+=3
                print(f"You've found food and earned 3 energy points, your current energy point is {x}")
        else:
            x-=1
            print(f"Invalid Action: You've lost 1 energy point, your current energy point is {x}")
        
        if x>=20:
            print("You've reached 20 energy points, congratulations!")
            break
        elif x<=0:
            print("Your energy point dropped to 0, you lost!")
            break


escape_the_loop()




        
