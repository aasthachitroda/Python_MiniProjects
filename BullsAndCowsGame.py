import random

print('''Welcome to Bulls and Cows Game! 
How to play: 
There is a secret 4 digit code that you have to guess 
After each guess you\'ll be given 2 hints: 
1)Bulls: number of correct digits in correct place 
2)Cows: number of correct digits in wrong place 
You have 10 tries to guess the secret code 
Good luck! \n''')

def NumToList(num):
    numList = [int(i) for i in str(num)]
    return numList

def checkRepetition(numList):
    return len(numList)==len(set(numList))

def secretCodeGenerate():
    while True:
        secret_code = random.randint(1000,9999)
        secret_code_List = NumToList(secret_code)
        if checkRepetition(secret_code_List)==True:
            break
    return secret_code, secret_code_List

def BullsAndCows(secret_code,input_code):
    bull_cow = [0,0]
    for i,j in zip(secret_code,input_code): 
        if j in secret_code: 
            if j==i:
                bull_cow[0] += 1 
            else:
                bull_cow[1] += 1 
    return bull_cow

play_again = 'y'
while play_again == 'y':
    noOfGuesses = 10
    input_code = 0000
    secret_code, secret_code_List = secretCodeGenerate()
    while noOfGuesses != 0 and input_code != secret_code:
        try:
            input_code = int(input('\nEnter your guess: '))
            input_code_List = NumToList(input_code)

            if input_code<1000 or input_code>9999:
                print('Enter a 4 digit number only \nTry again')
                continue
    
            if checkRepetition(input_code_List)!=True:
                print('The digits should not be repeated \nTry again')
                continue
    
            noOfGuesses = noOfGuesses - 1
            hintList = BullsAndCows(secret_code_List,input_code_List)
            print('Bulls:', hintList[0],'\nCows:', hintList[1], '\nGuesses left:',noOfGuesses)
        except(ValueError):
            print('Enter an integer only')

    if secret_code_List == input_code_List:
        print('\nYou Win! \nThe sceret code was:', secret_code)
    else:
        print('\nYou Lose \nOut of tries \nThe sceret code was:', secret_code)
    
    print('\nDo you want to play again? y/n')
    play_again = input()