# This program calculate how many tiles you will need
# when tiling a wall or floor in m2.

lenght = float(input('Enter lenght: '))
width = float(input('Enter width: '))

area = lenght * width

tiles = area * 1.05
print('You need', tiles, 'tiles in m2.')