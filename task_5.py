import csv

errors = []
errors_by_date = {}
with open('game.csv', encoding='utf-8') as file:
    data = list(csv.reader(file))[1:]
    for game_name, characters, name_error, date in data:
        errors.append(game_name)
        try:
            errors_by_date[date] += ',' + name_error
        except:
            errors_by_date[date] = ''
            errors_by_date[date] += name_error

with open('error.txt', "w+", encoding='utf-8') as file:
    message = 'Игры с ошибками:\r'
    for game in errors:
        message += f'{game}\r'
    file.write(message)

    message = '\rСписок ошибок по датам:\r'
    for k,v in errors_by_date.items():
        message += f'{k}:{v}\r'

    file.write(message)