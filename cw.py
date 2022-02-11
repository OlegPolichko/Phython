# кортежи
#dimensions = (200, 50)
#print(dimensions)
#dimensions = (250, 170)
#print(dimensions)

# словари (dict)
#dict = {'key' : 'value'}
#user = {
 #   'user_1' : 'супергероем',
  #  'user_2' : 'человек',
   # 'user_3' : 'волк'
#}
#print(user)
#y = user['user_1']
#print(y)
#message = f"Я буду {y} в этой игре"
#print(message)

#user['user_4'] = 'Гоблин'
#user['user_5'] = 'Пинокио'
#print(user)

#user['user_1'] = 'супергерой2.0'
#print(user)
   
   
#speed = int(input("Какую скорость ты предпочитаешь?"))   
#massiv = {'x': 0, 'y': 25, 'speed': speed}
#print(f"Оригиналная позиция игрока {massiv['x']}")

#if massiv['speed'] == 'slow':
#    x_inc = 1
#elif massiv['speed'] == 'medium':
#    x_inc = 2
#else:
#    x_inc = 3
    
#massiv['x'] += x_inc
#print(f"Новая позиция игрока {massiv['x']}")


#massiv = {'x': 0, 'y': 25, 'speed': 'medium'}
#print(massiv)
#del massive['speed']
#print(massiv)


#lang = {
#    'Sanchoz' : 'JavaScript',
#    'Makson' : 'Python',
#    'Bogdan' : 'C++',
#    'Mary' : 'Pascal'
#}

#for i in lang.values():
#  print(f"Я люблю язык програмирования --> {i}")
 
 
#lang = {
#    'Sanchoz' : 'JavaScript',
#    'Makson' : 'Python',
#    'Bogdan' : 'C++',
#    'Mary' : 'Pascal'
#}

#for i in lang.keys():
#  print(f"Я, {i}, люблю язык програмирования")


#lang = {
#    'Sanchoz' : 'JavaScript',
#    'Makson' : 'Python',
#    'Bogdan' : 'C++',
#    'Mary' : 'Pascal'
#}

#for i,j in lang.items():
#  print(f"Я ,{i}, люблю язык програмирования --> {j}")
  

#user = {'color': "green", 'points': 5, 'speed': 250}
#player_speed = user.get("speed", "У вас нет этой скорости")
#print(player_speed)

#user1 = {'color': "green", 'points': 5, 'speed': 250}
#user2 = {'color': "green", 'points': 5, 'speed': 250}
#user3 = {'color': "green", 'points': 5, 'speed': 250}
#player = [user1, user2, user3]
#print(player)
#for i in player:
#    print(i)


player = []
for i in range(30):
    user1 = {'color': "green", 'points': 5, 'speed': 250}
    player.append(user1)
print(player)
for i in player:
    print(i)
a = len(player)
print("-"*30)
print(f"Количество игроков {a}")

    



