import csv

characters_rating = {}
error = str(input())
while error != 'game':
    with open('game.csv', encoding='utf-8') as file:
        data = list(csv.reader(file))[1:]
        for game_name, characters, name_error, date in data:
            if name_error == error:
                print(f"Ошибка {name_error} встречается в игре {game_name} у персонажа {characters}.")
                break
        else:
            print('Этой ошибки не существует')
        error = str(input())