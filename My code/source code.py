a = input('Выберите тип калькулятора(сложение, умножение или вычитание): ')
b = int(input('Введите кол-во чисел с которыми потребуется провести операции(до 3): '))

if a == 'умножение':
  if b == 3:
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    number3 = int(input('Введите третье число: '))
    print(number1 * number2 * number3)
  elif b == 2:
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    print(number1 * number2)
elif a == 'сложение':
  if b == 3:
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    number3 = int(input('Введите третье число: '))
    print(number1 + number2 + number3)
  elif b == 2:
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    print(number1 + number2)
  else:
    prin('NO')
elif a == 'вычитание':
  if b == 3:
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    number3 = int(input('Введите третье число: '))
    print(number1 - number2 - number3)
  elif b == 2:
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    print(number1 - number2)
  else:
    print('NO')
elif a == 'деление':
  if b == 3:
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    number3 = int(input('Введите третье число: '))
  elif b == 2:
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    print(number1 % number2)
  else:
    print('NO')
   
