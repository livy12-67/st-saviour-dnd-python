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
    answer = input('Question 1: What is the largest animal on earth?')
    if answer == 'Whale':
        print('Correct good job!')
        score += 1
    else: 
        print ('Sorry... that is wrong.')

    answer = input('Question 2: What is the tallest mountain in the world?')
    if answer == 'Mount Everest':
        print ('Correct... great thinking!')
        score +=3 
    else: 
        print ('Sorry that is wrong.. maybe next time.')

    answer = input('Question 3: Which element has the chemical symbol 'O'?')
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
        print ('Correct.. =. great thinking!')
        score += 3 
    else:
        print ('Sorry... that is incorrect')
        




    
      
