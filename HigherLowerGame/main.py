import random
from art import logo,vs
from game_data import data


def assign():
    return random.choice(data)

def compare(country1,country2,user_input):
    area1 = country1['area']
    area2 = country2['area']
    max_area = max(area1,area2)
    
    if user_input==max_area:
        return True
    else:
        return False

print(logo)
score = 0
count = 0

while True:
    country1 = assign()
    country2 = assign()
    while country2 == country1:
        country2 = assign()
    
    print('\n',country1['country'].lower())
    print(vs)
    print(' ',country2['country'].lower())

    input_country = input('Enter the country with higher area: ')
    input_area = 0
    for dict in data:
        if dict['country'].lower() == input_country.lower():
            input_area = dict['area']

    if compare(country1,country2,input_area) == True:
        score += 1

    count += 1
    continueplaying = input('Do you want to continue playing y/n? ')
    if continueplaying != 'y':
        break

print('Your score is: ',score,'/',count,' \nThankyou for playing!')