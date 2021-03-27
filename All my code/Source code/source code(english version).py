a = input('Select the calculator type(addition, multiplication, subtraction or division): ')
b = int(input('Enter the number of numbers that you need to perform operations with(up to 3): '))

if a == 'multiplication':
  if b == 3:
    number1 = int(input('Enter the first number: '))
    number2 = int(input('Enter the second number: '))
    number3 = int(input('Enter the third number: '))
    print(number1 * number2 * number3)
  elif b == 2:
    number1 = int(input('Enter the first number: '))
    number2 = int(input('Enter the second number: '))
    print(number1 * number2)
  else:
    print('NO')
elif a == 'addition':
  if b == 3:
    number1 = int(input('Enter the first number: '))
    number2 = int(input('Enter the second number: '))
    number3 = int(input('Enter the third number: '))
    print(number1 + number2 + number3)
  elif b == 2:
    number1 = int(input('Enter the first number: '))
    number2 = int(input('Enter the second number: '))
    print(number1 + number2)
  else:
    prin('NO')
elif a == 'subtraction':
  if b == 3:
    number1 = int(input('Enter the first number: '))
    number2 = int(input('Enter the second number: '))
    number3 = int(input('Enter the third number: '))
    print(number1 - number2 - number3)
  elif b == 2:
    number1 = int(input('Enter the first number: '))
    number2 = int(input('Enter the second number: '))
    print(number1 - number2)
  else:
    print('NO')
elif a == 'division':
  if b == 3:
    number1 = int(input('Enter the first number: '))
    number2 = int(input('Enter the second number: '))
    number3 = int(input('Enter the third number: '))
    print(number1 // number2 // number3)
  elif b == 2:
    number1 = int(input('Enter the first number: '))
    number2 = int(input('Enter the second number: '))
    print(number1 // number2)
input('Press enter...')
