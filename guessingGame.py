#Number guessing name by Andrew Owen


import random
number = random.randint(1,20)
#number = 10

def start():
    name = input("Hello there, what is your name? ")
    print ("Nice to meet you", name + '.')

    play = input('Would you like to play a game with me? Yes/No ')
    if play.startswith('n'):
        print ('No? Listen', name + ' I was joking when I said there was an option. Here we go. ')
        print ("I'm thinking of a number between 1 and 20. ")
        game(name)
    elif play.startswith('y'):
        print ('Good thinking. ')
        print ("I'm thinking of a number between 1 and 20. ")
        game(name)
    else:
        print ("That wasn't an option. We're playing anyway. ")
        print ("I'm thinking of a number between 1 and 20. ")
        game(name)

def game(name):
    guess = 0
    tries = 0
    while number != guess:
        guess = int(input("What is your guess? "))
        tries = tries + 1
        if (guess > number):
            low = ['Go lower', 'Lower', 'It is lower', "I'm thinking lower", "You're too high"]
            print(random.choice(low))
            
        elif (guess < number):
            high = ['Go higher', 'Higher', 'It is higher', "I'm thinking higher", "You're too low"]
            print(random.choice(high))

        elif tries == 1:
            print ('WOW! First guess! I was thinking of the number', number,'.')
            print ("Number of tries:", tries)
            playAgain = input('Play again? Yes/No ')
            if playAgain.startswith('n'):
                print ('Good, you were boring me anyway.')
                return
            elif playAgain.startswith('y'):
                start2(name)
             
        else:
            print ("That's it", name + '! I was thinking of the number', number,'.')
            print ("Number of tries:", tries)
            playAgain = input('Play again? Yes/No ')
            if playAgain.startswith('n'):
                print ('Good, you were boring me anyway.')
                return
            elif playAgain.startswith('y'):
                start2(name)

def start2(name):
    print ("I knew you would. You know the drill", name, '.')
    game(name)

start()