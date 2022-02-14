#Execicio:
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

#Meu Código:
first_number = float(input('Choose a number\n'))
operation = str(input('Choose a operation\n'))
second_number = float(input('Choose another number\n'))

if operation == '+':
    print(f'The result is {first_number + second_number}')

if operation == '-':
    print(f'The result is {first_number - second_number}')

if operation == '*':
    print(f'The result is {first_number * second_number}')

if operation == '/':
    print(f'The result is {first_number / second_number}')

#Bonus:
celcius = float(input('Choose a temperature in Celcius\n'))
farenheit = float(celcius*9/5 + 32)

print(f'The temperature in fareinheit is {farenheit}')