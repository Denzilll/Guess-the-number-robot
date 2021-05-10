import random
print('Привет! Загадай число от 1 до 100, а робот попробует угадать это число!')
number = int(input("Введите любое число от 1 до 100: "))
bot = random.randint(1, 100)
cont = 0
while bot != number:
	cont += 1
	bot = random.randint(1, 100)
	if number > bot:
		print('Число больше')		
		
	elif number < bot:
		print('Число меньше')
	print('Угадываю')
	print(bot)
print("Я угадал! Это число", bot)
print("Мне нужно было затратить", cont, "попыток!")
input()