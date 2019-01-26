import random
def guess():
    n=random.randint(1,100)
    print("Guess a number from 1 to 100")
    inp=-1
    guesses=[]
    while True:
        inp=int(input())
        guesses.append(inp)
        if inp==n:
            print("Your right")
            break
        elif inp>n:
            print("Guess lower")
        else:
            print("guess higher")

    for i in range(len(guesses)):
        if inp == n:
            print("Your guess",i+1,'was',guesses[i],'which was correct number!')

        elif inp > n:
            print("Your guess", i + 1, 'was', guesses[i], 'which was higher than',n)
        else:
            print("Your guess", i + 1, 'was', guesses[i], 'which was lower than', n)



