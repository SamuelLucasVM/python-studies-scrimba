#checando se 'Eric' e 'John' existem em 'friends'
#combinando os 2 'sets'
#encontrando nomes comuns nas 2 listas
#encontrando nomes que so tem em 'friends'
#mostrando nomes que aparecem somente em 1 lista
#criando uma lista dos carros sem duplicações

from distutils.command.build_scripts import first_line_re


friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

combined_list = (friends.union(my_friends))
common_names = (friends.intersection(my_friends))
only_friends = (friends.difference(my_friends))
just_one_list_names = (friends.symmetric_difference(my_friends))
cars_without_duplications = set(cars)

print(friends.__contains__('Eric' and 'John'))
print(combined_list)
print(common_names)
print(only_friends)
print(just_one_list_names)
print(cars_without_duplications)