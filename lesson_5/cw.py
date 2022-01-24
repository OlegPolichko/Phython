while True:
    name = input("Введите имя:")
    surname = input("Введите фамилию:")
    out = input("Не хотите ли Вы выйти ?")
    if out == "хватит":
        break
    print(f"Привет, {name} {surname}. Я очень рад тебя видеть! Меня зовут BOT")
    
    
    
print("y=x**2")
print("x=1,2,3,...,10")
ARR = [1,2,3,4,5,6,7,8,9,10]
for x in ARR:
    y=x**2
    print(f"{x} --> {y}")
    
    
    

print("y=x**2")
print("x=1,2,3,...,10")
for x in range(1,11):
    y=x**2
    print(f"{x} --> {y}")