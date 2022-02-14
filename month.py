#Codigo do Exercicio:
#def num_days(month):

##    if month == 'jan':
##        print('number of days in',month,'is',31)
##    elif month == 'feb':
##        print('number of days in',month,'is',28)
##    elif month == 'mar':
##        print('number of days in',month,'is',31)
##    elif month == 'apr':
##        print('number of days in',month,'is',30)
##    elif month == 'may':
##        print('number of days in',month,'is',31)
##    elif month == 'jun':
##        print('number of days in',month,'is',30)
##    elif month == 'jul':
##        print('number of days in',month,'is',31)
##    elif month == 'aug':
##        print('number of days in',month,'is',31)
##    elif month == 'sep':
##        print('number of days in',month,'is',30)
##    elif month == 'oct':
##        print('number of days in',month,'is',31)
##    elif month == 'nov':
##        print('number of days in',month,'is',30)
##    elif month == 'dec':
##        print('number of days in',month,'is',31)

#num_days('oct')

# Comando do exercicio:
## optimize/shorten the code in the function
## try to reduce the number of conditionals 

#Meu código:

def num_days(month):

    if month in {'jan','mar','may','jul','aug','oct','dec'}:
        days = 31
    elif month == 'feb':
        days = 28
    elif month in {'apr','jun','sep','nov'}:
        days = 30
    print(f'number of days in {month} is {days}')

num_days(str(input('What is the month?\n')))