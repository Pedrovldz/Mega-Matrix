num = [[], [], []]
pares = []
cont = cont2 = cont3 = 0
for c in range(0,3):
    n1 = int(input(f'Input a number for position [0, {cont}] '))
    num[0].append(n1)
    if n1 % 2 == 0:
        pares.append(n1)
    cont += 1

for v in range(0, 3):
    n2 = int(input(f'Input a number for position [1, {cont2}] '))
    num[1].append(n2)
    if n2 % 2 == 0:
        pares.append(n2)
    cont2 += 1

for b in range(0, 3):
    n3 = int(input(f'Input a number for position [2, {cont3}] '))
    num[2].append(n3)
    if n3 % 2 == 0:
        pares.append(n3)
    cont3 += 1

print('-=' * 10)
print('Matrix:')
print('-=' * 10)
print(f'[ {num[0][0]} ] [ {num[0][1]} ] [ {num[0][2]} ]')
print(f'[ {num[1][0]} ] [ {num[1][1]} ] [ {num[1][2]} ]')
print(f'[ {num[2][0]} ] [ {num[2][1]} ] [ {num[2][2]} ]')

print('-=' * 10)
if len(pares) == 0:
    print('There is no even numbers!')
else:
    print(f'The sum of the even values is {sum(pares)}')
print(f'The sum of the itens in the third collum is {num[0][2] + num[1][2] + num[2][2]}')
print(f'The largest value of the third row is {max(num[1])}')

if len(num) >= 3:
    if num[0][0] == 1:
        num[0][0] = '!'
    elif num[0][0] == 2:
        num[0][0] = '@'
    elif num[0][0] == 3:
        num[0][0] = '#'
    elif num[0][0] == 4:
        num[0][0] = '$'
    elif num[0][0] == 5:
        num[0][0] = '%'
    elif num[0][0] == 6:
        num[0][0] = '¨'
    elif num[0][0] == 7:
        num[0][0] = '&'
    elif num[0][0] == 8:
        num[0][0] = '*'
    elif num[0][0] == 9:
        num[0][0] = '('
    elif num[0][0] == 0:
        num[0][0] = ')'

    if num[0][1] == 1:
        num[0][1] = '!'
    elif num[0][1] == 2:
        num[0][1] = '@'
    elif num[0][1] == 3:
        num[0][1] = '#'
    elif num[0][1] == 4:
        num[0][1] = '$'
    elif num[0][1] == 5:
        num[0][1] = '%'
    elif num[0][1] == 6:
        num[0][1] = '¨'
    elif num[0][1] == 7:
        num[0][1] = '&'
    elif num[0][1] == 8:
        num[0][1] = '*'
    elif num[0][1] == 9:
        num[0][1] = '('
    elif num[0][1] == 0:
        num[0][1] = ')'

    if num[0][2] == 1:
        num[0][2] = '!'
    elif num[0][2] == 2:
        num[0][2] = '@'
    elif num[0][2] == 3:
        num[0][2] = '#'
    elif num[0][2] == 4:
        num[0][2] = '$'
    elif num[0][2] == 5:
        num[0][2] = '%'
    elif num[0][2] == 6:
        num[0][2] = '¨'
    elif num[0][2] == 7:
        num[0][2] = '&'
    elif num[0][2] == 8:
        num[0][2] = '*'
    elif num[0][2] == 9:
        num[0][2] = '('
    elif num[0][2] == 0:
        num[0][2] = ')'

    if num[1][0] == 1:
        num[1][0] = '!'
    elif num[1][0] == 2:
        num[1][0] = '@'
    elif num[1][0] == 3:
        num[1][0] = '#'
    elif num[1][0] == 4:
        num[1][0] = '$'
    elif num[1][0] == 5:
        num[1][0] = '%'
    elif num[1][0] == 6:
        num[1][0] = '¨'
    elif num[1][0] == 7:
        num[1][0] = '&'
    elif num[1][0] == 8:
        num[1][0] = '*'
    elif num[1][0] == 9:
        num[1][0] = '('
    elif num[1][0] == 0:
        num[1][0] = ')'

    if num[1][1] == 1:
        num[1][1] = '!'
    elif num[1][1] == 2:
        num[1][1] = '@'
    elif num[1][1] == 3:
        num[1][1] = '#'
    elif num[1][1] == 4:
        num[1][1] = '$'
    elif num[1][1] == 5:
        num[1][1] = '%'
    elif num[1][1] == 6:
        num[1][1] = '¨'
    elif num[1][1] == 7:
        num[1][1] = '&'
    elif num[1][1] == 8:
        num[1][1] = '*'
    elif num[1][1] == 9:
        num[1][1] = '('
    elif num[1][1] == 0:
        num[1][1] = ')'

    if num[1][2] == 1:
        num[1][2] = '!'
    elif num[1][2] == 2:
        num[1][2] = '@'
    elif num[1][2] == 3:
        num[1][2] = '#'
    elif num[1][2] == 4:
        num[1][2] = '$'
    elif num[1][2] == 5:
        num[1][2] = '%'
    elif num[1][2] == 6:
        num[1][2] = '¨'
    elif num[1][2] == 7:
        num[1][2] = '&'
    elif num[1][2] == 8:
        num[1][2] = '*'
    elif num[1][2] == 9:
        num[1][2] = '('
    elif num[1][2] == 0:
        num[1][2] = ')'

    if num[2][0] == 1:
        num[2][0] = '!'
    elif num[2][0] == 2:
        num[2][0] = '@'
    elif num[2][0] == 3:
        num[2][0] = '#'
    elif num[2][0] == 4:
        num[2][0] = '$'
    elif num[2][0] == 5:
        num[2][0] = '%'
    elif num[2][0] == 6:
        num[2][0] = '¨'
    elif num[2][0] == 7:
        num[2][0] = '&'
    elif num[2][0] == 8:
        num[2][0] = '*'
    elif num[2][0] == 9:
        num[2][0] = '('
    elif num[2][0] == 0:
        num[2][0] = ')'

    if num[2][1] == 1:
        num[2][1] = '!'
    elif num[2][1] == 2:
        num[2][1] = '@'
    elif num[2][1] == 3:
        num[2][1] = '#'
    elif num[2][1] == 4:
        num[2][1] = '$'
    elif num[2][1] == 5:
        num[2][1] = '%'
    elif num[2][1] == 6:
        num[2][1] = '¨'
    elif num[2][1] == 7:
        num[2][1] = '&'
    elif num[2][1] == 8:
        num[2][1] = '*'
    elif num[2][1] == 9:
        num[2][1] = '('
    elif num[2][1] == 0:
        num[2][1] = ')'

    if num[2][2] == 1:
        num[2][2] = '!'
    elif num[2][2] == 2:
        num[2][2] = '@'
    elif num[2][2] == 3:
        num[2][2] = '#'
    elif num[2][2] == 4:
        num[2][2] = '$'
    elif num[2][2] == 5:
        num[2][2] = '%'
    elif num[2][2] == 6:
        num[2][2] = '¨'
    elif num[2][2] == 7:
        num[2][2] = '&'
    elif num[2][2] == 8:
        num[2][2] = '*'
    elif num[2][2] == 9:
        num[2][2] = '('
    elif num[2][2] == 0:
        num[2][2] = ')'
print('-=' * 10)
print('Matriz converted to symbols:')
print('-=' * 10)
print(f'[ {num[0][0]} ] [ {num[0][1]} ] [ {num[0][2]} ]')
print(f'[ {num[1][0]} ] [ {num[1][1]} ] [ {num[1][2]} ]')
print(f'[ {num[2][0]} ] [ {num[2][1]} ] [ {num[2][2]} ]')
