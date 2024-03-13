import csv

characters_rating = {}
with open('game.csv', encoding='utf-8') as file:
    data = list(csv.reader(file))[1:]
    for game_name, characters, name_error, date in data:
        try:
            characters_rating[characters] += 1
        except:
            characters_rating[characters] = 0
            characters_rating[characters] += 1

sorted_rating = sorted(characters_rating.items())
with open('sorted.txt', "w+", encoding='utf-8') as file:
    for rating in sorted_rating:
        file.write(f'Персонаж {rating[0]} - количество багов: {rating[1]}\r')