from operator import le
#Preço de Venda de Limonadas

lemonades_sold_first_week = [3, 1, 5, 6, 2, 7, 8]
lemonades_sold_second_week = [1, 2, 2, 1, 4, 5]
new_day = input('How many leomandes were sold in sunday?\n')

lemonades_sold_second_week.append(int(new_day))

sales = lemonades_sold_first_week + lemonades_sold_second_week

print(f'You sold, on two weeks, {sales} lemonades respectively')

sales.sort()

worst_day = sales[0]
best_day = sales [-1]

print(f'You earned {worst_day*1.5} dolars on your worst day seeling lemonades')
print(f'You earned {best_day*1.5} dolars on your best day seeling lemonades')
print(f'You earned {worst_day*1.5 + best_day*1.5} dolars in the both days')