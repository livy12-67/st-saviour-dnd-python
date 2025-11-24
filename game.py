import random
import time

from draw import draw_d20, draw_d6, draw_d4

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    # create character by collecting user input (name + class)
    # print character sheet
    # specify roll that must be beat and enemy initiative by collecting user input
    # any buffs / debuffs?
    # any critical success / failure?

  
    print_dramatic_text('Welcome to my trivia game!') 
    answer = input('Name:')

    answer = input('Question 1: What is the largest animal on earth?')
    if answer == 'Whale':
        print('Correct good job!')
        score += 2 # type: ignore
    else: 
        print ('Sorry... that is wrong.')

    answer = input('Question 2: What is the tallest mountain in the world?')
    if answer == 'Mount Everest':
        print ('Correct... great thinking!')
        score += 3 
    else: 
        print ('Sorry that is wrong.. maybe next time.')

    answer = input('Question 3: Which element has the chemical symbol O?')
    if answer == 'Oxygen':
        print ('Correct... On to the next!')
        score += 1
    else: 
        print ('Sorry... thats incorecct')

    answer = input('Question 4: In which year did the titantic sink?')
    if answer == '1912':
        print ('Correct... your smart!')
        score += 3
    else:
        print ('Sorry... try again')

    answer = input('Question 5: Who wrote the play "Romeo and Juilet"?')
    if answer == 'William Shakespeare':
        print ('Correct... great thinking!')
        score += 3 
    else:
        print ('Sorry... that is incorrect')

    answer = input ('Question 6: What is the capital city of France?')
    if answer == 'Paris':
        print ('Correct... good job!')
        score += 2 
    else: 
        print ('Sorry... maybe next time.')

    answer = input ('Question 7: What planet is known as the Red Planet?')
    if answer == ' Mars':
        print ('Correct... good job!')
        score += 4 
    else:
        print ('Sorry.. not this time')

    answer = input ('Question 8: Which planet is closest to the Sun?')
    if answer == ' Mercury': 
        print ( 'Correct... your smart!')
        score += 3
    else: 
        print ('Sorry ... try again')
   
    answer = input ('Question 9: What is the main ingredient in guacamole?')
    if answer == 'Avacado': 
        print ('Correct... im impressed')
        score += 2 
    else:
        print ('Sorry... you are wrong')

    answer = input ('Question 10: What is the name of the fairy in Peter Pan?')
    if answer == 'Tinkerbell': 
        print ('Correct... great thinking!')
        score += 2 
    else:
        print ('Sorry... maybe next time')

    answer = input ('Question 11: What is the main gas found in the earths atmosphere?')
    if answer == 'Nitrogen': 
        print ('Correct... your awesome!')
        score += 3 
    else: 
        print ('Sorry... maybe next time')

    answer = input ('Question 12: What is the worlds largest dessert?')
    if answer == 'Sahara dessert':
        print ('Correct... your intelligent')
        score += 2 
    else:
        print ('Sorry... good thinking though')

    answer = input ('Question 13: Which holiday is Jesus ressurection?')
    if answer == 'Easter': 
        print ('Correct... im impressed')
        score += 4 
    else: 
        print ('Sorry... dont lose hope')

    answer = input ('Question 14: Who is Jesus the son of?')
    if answer == 'God': 
        print ('Correct... nice!')
        score += 3 
    else: 
        print ('Sorry... maybe next time')

    answer = input ('Question 15: Who is Jesus mom?')
    if answer == 'Mary':
        print ('Correct... great job!')
        score += 4 
    else: 
        print ('Sorry... that is wrong')

    




    



    
      
