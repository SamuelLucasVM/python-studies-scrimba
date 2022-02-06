import string


name = input('Enter your first name:\n')
distance = float(input('Enter the distance in km:\n'))

print(f'{name.capitalize()} {distance} km or {distance/1609} miles.')