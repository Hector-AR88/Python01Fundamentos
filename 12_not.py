#not

print(not True)
print(not False)

print('not True and True =>', not (True and True))
print('not True and False =>', not (True and False))
print('not False and True =>', not (False and True))
print('not False and False =>', not (False and False))

# ejemplo practico
stock = int(input('Ingrese el numero de stock => '))
print(not (stock >= 100 and stock <=1000))



