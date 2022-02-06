import string


name = input('Enter your first name:\n')
distance = float(input('Enter the distance in km:\n'))

print(name.capitalize() + ', ' + str(distance) + ' ' + 'km or ' + str(distance/1609) + ' miles.')