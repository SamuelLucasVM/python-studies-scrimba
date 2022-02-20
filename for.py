#O que o exercicio me deu:
names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']

#Objetivos:
##Organizar os nomes para ficarem formais;
##Juntar as 2 listas;
##Adicionar uma input box para colocar mais 2 nomes na lista
##Printar convites para um aniversario com essas listas com 'for loops'.

added = [input('What is the guest is name?\n'), input('What is the another guest is name?\n')]
guest = (names.__add__(names1)).__add__(added)

for name in guest:
    print(f'Hello {name.title()}, you were invited to my birthday party!')