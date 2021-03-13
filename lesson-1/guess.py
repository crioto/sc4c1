import random

# maximumattempts
# maximumAttempts
# maximum_attempts
# maximum-attempts
# maximumattemptsandretries

def more(number):
    print("Нет, мое число больше, чем " + str(number))

def less(number):
    print("Нет, мое число меньше, чем " + str(number))

attempts = 0
maximum_attempts = 5
victory = 0

answer = random.randint(0, 100)

print("Привет, я загадал число от 0 до 100. Сможешь угадать его?")
print("У тебя будет всего " + str(maximum_attempts) + " попыток")

while attempts < maximum_attempts:
    print("Введи свое число:")
    my_answer = int(input())
    if answer == my_answer:
        victory = 1
        break
    if my_answer > answer:
        less(my_answer)
    if my_answer < answer:
        more(my_answer)
    attempts = attempts + 1

if victory == 1:
    print("Ура, ты победил!")
else:
    print("Ты не смог угадать мое число. Это было число " + str(answer))

