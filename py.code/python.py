import random
a = random.randrange(100) + 1
print("Давай мыграем в игру Угадай число")
guest = int(input("Какое число я загадал ? "))
while guest != a:
    if guest > a:
        print("Меньше...")
    else:
        print("Больше...")
    guest = int(input("Подумай еще раз и напиши число : "))
print ("Ты молодец! Я загадал число ", a)