file_size = 25.2
file_size2 = 25
file_name = 'Фильм'
file_id = ('id', '12345')
play_list = ['Фильм1', 'Фильм2']
hashtags = {'teg_tipa':'movie', 'geo_teg': 'Russia'}
spisok = [file_size, file_size2, file_name, file_id, play_list, hashtags]
for t in spisok:
    print(f'{t} is {type(t)}')
# 2 задание
spisok_pokupok = input('Введите список через запятую или пробел: ')
spisok_pokupok = spisok_pokupok.split()
if len(spisok_pokupok) % 2 == 0:
    i = 0
    while i < len(spisok_pokupok):
        vvodnaya_peremennaya = spisok_pokupok[i]
        spisok_pokupok[i] = spisok_pokupok[i+1]
        spisok_pokupok[i+1] = vvodnaya_peremennaya
        i += 2

else:
    i = 0
    while i < len(spisok_pokupok) - 1:
        vvodnaya_peremennaya = spisok_pokupok[i]
        spisok_pokupok[i] = spisok_pokupok[i + 1]
        spisok_pokupok[i + 1] = vvodnaya_peremennaya
        i += 2
print(spisok_pokupok)
#
mesyats = int(input('Введите число: '))
zima = [12,1,2]
vesna = [3,4,5]
leto = [6,7,8]
osen = [9,10,11]
if mesyats == zima:
    print('Зима')
