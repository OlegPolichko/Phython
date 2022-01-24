import math;
r=float(input('Введите радиус'))
a = 2 * r * math.sqrt(3);
b = (a**2*math.sqrt(3))/4
print("Сторона -", a)
print("Площадь -", b)



a = input("Ваше имя? ")
print("Здравствуйте,",a, "приятно познакомиться)))")
b = input("А лет сколько? ")
print(a,",","тебе ",b," лет ")



name=f"Привет!"
print(name)
a = input("Откуда ты? ")
b = f"Ух ты, прикольно, что ты из {a}а"
print(b)


x = int(input("Угадай число"))
y = 49
if x == y:
    print("Ты угадал")

elif x > y:
    print("меньше")

elif x < y:
    print("больше")
    
else:
    print("Ты не угадал")