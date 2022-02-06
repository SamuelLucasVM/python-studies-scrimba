import string


name = input('Enter your first name:\n')
distance = float(input('Enter the distance in km:\n'))

print(f'Hi {name.capitalize()}! {distance} km is equivalent to {round(distance/1.609,2)} miles.')