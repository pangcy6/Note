# aliens是列表, 列表中的元素是字典, 这种数据类型称为嵌套.

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 修改字典元素
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:2]:
    if alien['color'] != 'red':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print('.' * 30)

print('\nTotal number of aliens: ' + str(len(aliens)))


# 将列表存储在字典中
print("\n")
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra chesse']
}


print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
