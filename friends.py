#Separando nomes de uma lista bagunçada

csv = 'Kaike,Caio,Raul,Leo,Davi:Francisco;Douglas'

csv = (csv.replace(':', ',')).replace(';', ',')

friends_list = [', '.join(csv.split(','))]

print(friends_list)