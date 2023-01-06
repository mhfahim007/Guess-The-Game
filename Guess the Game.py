import random 

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    win=False
    for count in range(10,-1,-1):
        if count !=0 and win==False:
            while guess != random_number:
                guess=int(input(f"Please guess a number from 1 to {x}:"))
                if guess>random_number:
                    print(f"You guessed {guess} which is too high.")
                elif guess<random_number:
                    print(f"You guessed {guess} which is too low.")
                else:
                    print(f"Congrats!! You guessed the correct number : {random_number}")  
                    win=True
                    break
                count -=1
                print(f"You have {count} times left.")
                break
        elif win:
            break
        else:    
            print(f"Sorry you have crossed the limits and cannot guess anymore!")
          

guess(100)