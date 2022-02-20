#1
#found = {'games': 23, 'food': 17, 'translater': 50}
#for a, b in found.items():
#   print("Запросом", a ,"пользуются", b ,"% человек")

#2
#good = {'today' : 'поесть','tomorrow' : 'поспать'}
#print("За сегодня и завтра я хочу", good)

#3
#idents = {1 : 'Макс', 2 : 'zero', 3 : 'Егор', 4 : 'Саша'}
#for a, b in idents.items() :
# if idents[a] == 'zero':
#    print(f"Вітаю друзі")
# else :
#    print(f"Вітаю, {b}")

#4
#things = {'Меч' : 1, 'Артефактов' : 6, 'Монет' : 100}
#for a, b in things.items() :
#   print(f"У вас есть {b} {a}")
   
#5
#n = int(input("n ="))
#a = {}
#for i in range(n + 1) :
#    a[i] = i ** 2
#print(a)

#6
#play = {"shooter": "csgo", "бродилка": "Мастера Меча и Магии", "horror": "Phasmofobia"}
#for a, b in play.items():
#    print(f"{b} это {a}")

#7
#person = {"Бил Гейтс" : "28/10/1955", "Макс" : "18/08/2006", "Сергей Брин" : "21/08/1973"}
#a = input("Кто? ")
#b = person.get(a, "Error")
#print(b)

#8
#food = {"гречка": "есть", "макароны": "есть", "картошка": "есть"}
#a = input("")
#b = food.get(a, "нету")
#print(b)

#9
city = {"Харьков": "город Украины, 2 млн человек, Первая столица Украины",
        "Магадан": "город Росии, 100 тис. человек, Второй по величине морской порт страны",
        "Москва": "столица Росии, 12.6 млн человек, Раньше называлась Кучково."}
for a, b in city.items():
    print(f"{a} - {b}")