#1
names = ['Егор', 'Антон', 'Макс', 'Саня']
print("Привет ", names[0])
print("Привет ", names[1])
print("Привет", names[2])
print("Привет", names[3])

#2
machines = ['Самолет', 'Мотоцикл', 'Автобус', 'Велосипед']
print("Я хотел бы купить", machines[0])
print("Я хотел бы купить", machines[1])
print("Я хотел бы купить", machines[2])
print("Я хотел бы купить", machines[3])

#3
years_list = [2006, 2007, 2008, 2009, 2010, 2011]
print("В", years_list[3], 'мне исполнилось 3 года')
years_list.insert(6, 2012)
print(years_list)
print('В',years_list[6],'мне было больше всего лет')

#4
things = ['wallet', 'mirror', 'umbrella']
print(things[2].title(), 'имеет отношение к дождю')
print(things[2].upper())
print(things)
del_things = things.pop(2)
print(things)

#5
languages = ['Georgian', 'Estonian' , 'Ukrainian']
print(languages[2].lower())
print(languages[2][::-1].title())

#6
list = ['Клавиатура', 'Мышка', 'Монитор', 'Блок']
cor = ('Роутер', 'Провод', 'Драйвера')
print('hardware:', list)
print('software:', cor)
list[0]= 'Микрофон'
#cor[0]= 'Wifi'  (нельзя)
print(list)
print(cor)

#7
languages = ['Ukrainian', 'French', 'Bulgarian', 'Norwegian', 'Latvian']
print(languages)
#languages.sorted()
#print(languages)
languages.reverse()
print(languages)
languages.sort()
print(languages)

#8
a = int(input("Число 1 "))
b = int(input("Число 2 "))
c = int(input("Число 3 "))
d = int(input("Число 4 "))
x = [a, b, c, d]
y = x[0] + x[1] + x[2] + x[3]
print(y)

#9
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a = 1
k = 0

while a < 4:
    a=numbers[k]
    print(a)
    k=k+1
    

#10
years=[2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
print(years)