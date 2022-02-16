#Comandos do Execercício:
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
# Three Loop Questions:
#1. What do I want to repeat?
#  -> 
#2. What do I want to change each time?
#  -> 
#3. How long should we repeat?
#  ->

#Meu Código:
correct_number = int(5)

guesses = 3
while guesses > 0:
    if guesses == 3:
        number = int(input('Enter a number betwen 0 and 10: '))
    else:
        number = int(input('Enter another number: '))
    if number > 10:
        print(f'This is more than 10, try again!')
        break
    if number < 0:
        print(f'This is below 0, try again!')
        break
    if number is correct_number:
        print(f'Congratulations, {number} is a correct number!')
        break
    else:
        guesses = guesses - 1
        if guesses == 2:
          print(f'Wrong! You have {guesses} more chances!')
        elif guesses == 1:
          print(f'Wrong again! You have only {guesses} more chance!')   
        else:
          print('You do not have more chances. You lose!')


#Modificação 1:
correct_number = int(33)

guesses = 5
while guesses > 0:
    if guesses == 5:
        number = int(input('Enter a number between 0 and 100: '))
    else:
        number = int(input('Enter another number: '))
    
    if number is correct_number:
        print(f'Congratulations, {number} is a correct number!')
        break
    elif number > 100:
        print(f'This is more than 100, try again!')
        break
    elif number < 0:
        print(f'This is below 0, try again!')
        break
    else:
        guesses = guesses - 1
        if guesses == 1 and number > correct_number:
          print(f'Too high! You have only {guesses} more chance!')
        elif guesses == 1 and number < correct_number:
          print(f'Too low! You have only {guesses} more chance!')
        elif 1 < guesses <= 4 and number > correct_number:
          print(f'Too high! You have {guesses} more chances!')
        elif 1 < guesses <= 4 and number < correct_number:
          print(f'Too low! You have {guesses} more chances!')
    if guesses == 0:
      print('You do not have more chances. You lose!')
