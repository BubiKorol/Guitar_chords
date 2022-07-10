'''В модуле задаются численные значения нот для каждой струны и лада. Можно вручную изменить строй, кол-во струн и
ладов
Импортируются инструменты для конвертации данных и создания числовой последовательности нот для каждой струны.'''
import nv_converter as nv

st6, st5, st4, st3, st2, st1 =['e2'], ['a2'], ['d3'], ['g3'], ['b3'], ['e4'] #ноты при открытой струне
string_values = [st6, st5, st4, st3, st2, st1]
frets_amount = 20 #количество ладов
all_guitar_notes = [[] for i in range(len(string_values))] #пустой список для записи значений нот для каждой струны

for i in string_values:
    i[0] = nv.note_value(i[0]) #конвертируем ноты в численные значения

# st6, st5, st4, st3, st2, st1 = [28],[33],[38],[43],[47],[52] стартовые значения для сверки

def string_list():
    '''Формирует двухуровненвый со значениями нот для каждой струны. Струны идут от 6 до 1. Например,
    all_guitar_notes[0] - список нот на 20 ладах для 6-ой(басовой) струны'''
    for k,i in enumerate(string_values):
        for j in range(frets_amount):
            all_guitar_notes[k].append(i[0]+j)
    return all_guitar_notes

string_list()
