answer = input('Выберите язык калькулятора(en - английский, русский - ru): ')
if answer == 'en':  
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

elif answer == 'ru':
  a = input('Выберите тип калькулятора(сложение, умножение, вычитание или деление): ')
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
      print(number1 // number2 // number3)
    elif b == 2:
      number1 = int(input('Введите первое число: '))
      number2 = int(input('Введите второе число: '))
      print(number1 // number2)
  input('Нажмите enter...')
