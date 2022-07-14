'''
Основной модуль, формирует аккорды.
Вводные данные - задаются также в этом модуле - переменные note, chord, fret_max, fret_min.
Формирование аккорда происходит в несколько этапов. Каждый этап представлен отдельной функцией. Отдельные этапы
могут быть опциональными(обращения аккордов,"неиграемые струны").
Активация этапов и их порядок регулируется функцией guitar_chord.
Фунцкция test_all прогоняет через guitar_chord_vers1 все комбинации аккордов.
Функция muted_notes - в разработке

 Из модуля chord_types используются функции задающие тип аккорда: мажор, минор, септ и т.д.
 Из модуля nv_converter используются инструменты для конвертирования данных
 Из модуля strings используется числовая последовательность нот для каждой струны.
 '''

from itertools import product
import chord_types as types
import nv_converter as nv
import strings as st
import datetime


def chord_simple_value(note, chord):
    '''Формирует аккорд в виде численных значений'''
    note = nv.note_value(note + '0')
    for k, v in types.dict.items():
        if k == chord:
            chord_simple = [nv.ignore_oct(i) for i in v(note)]
    return chord_simple


def chord_simple_note():
    '''Представляет аккорд в буквенном виде, без октав. Только для визуализации.'''
    chord_simple = chord_simple_value(note, chord)
    chord_simple = [nv.value_note(i)[:-1] for i in chord_simple]
    return chord_simple


def position_raw():
    '''Из заданного аккорда формирует двухуровневый неоднородный список.
    0 уровень - струны. 1 уровень - ноты входящие в аккорд.
    На разных струнах может оказаться разное количество подходящих нот, отсюда неоднородность.
    Маркирует неиграемые струны, присваивая значение -1.
    Учитывается ограничение по ладам, т.к. есть физические ограничения по разбросу пальцев.
    '''
    pos_raw = [[] for i in range(len(st.string_values))]
    for k, i in enumerate(st.string_list()):  # для каждой струны
        for l, j in enumerate(st.string_list()[k]):  # для каждой ноты на струне
            for elem in chord_simple_value(note, chord):  # ноты аккорда
                if elem == j % 12 and fret_min <= l <= fret_max:
                    # соответствие каждой ноты струны аккорду и ладовому диапазону
                    pos_raw[k].append(j)
        if pos_raw[k] == []:  # если не нашлось нужной ноты
            pos_raw[k] = [-1]  #значение для неиграемой струны
    return pos_raw


def combinations(raw):
    '''Функция выдает однородные комбинации из вариантов полученных от функции position_raw.
      Это уже удобная для игры форма(если конвертировать в ноты или позиции пальцев), однако она содержит
      ошибочные значения.'''
    comb = list(product(*raw))
    return comb


def no_inversion(comb_inp):
    '''Исключает обращения аккордов - комбинации в которых самая низкая нота НЕ тоник'''
    pure_chord = [[] for i in range(len(comb_inp))]
    for k, i in enumerate(comb_inp):
        stop_check = False
        for l, j in enumerate(i):
            if l <= (len(st.string_values)-len(chord_simple_value(note,chord))) and not stop_check :
                #не имеет смысла проверять если играемых струн меньше чем нот в аккорде
                if j%12 != chord_simple_value(note,chord)[0]:
                    pure_chord[k].append(-1)
                    #из-за того, что разные элементы приравниваются к одному значению, возникает задвоение
                else:
                    pure_chord[k].append(j)
                    stop_check = True  #нашли флажок, перестаем проверять на тонику
            else:
                pure_chord[k].append(j)
    pure_chord = [i for k, i in enumerate(pure_chord) if i not in pure_chord[k+1:]] #убираем задвоения
    return pure_chord


def check_chord(comb):
    '''Проверяет каждую комбинацию на наличие в ней всех нот аккорда. Убирает неполноценные комбинации.
    Получает игровой вариант в числовом формате.'''
    checked = [[] for i in range(len(comb))]
    for k, i in enumerate(comb):
        comb[k] = [i % 12 for i in comb[k] if i > 0]  # упрощаем значения нот для сравнения
        if set(comb[k]) == set(chord_simple_value(note, chord)):
            checked.append(i)  #сохраняем комбинации
    checked = [i for i in checked if i != []]
    return checked


def notes_frets(comb_inp):
    '''Переводим числовые значения в ноты и табулатуру.'''
    guitar_notes = [[] for i in range(len(comb_inp))] #создаем пустые списки соответствующей длины
    guitar_frets = [[] for i in range(len(comb_inp))]
    for k, i in enumerate(comb_inp):
        for l, j in enumerate(i):
            if j == -1:  # для неиграемых струн
                guitar_notes[k].append('x')
                guitar_frets[k].append('x')
            else:  # для всех струн
                guitar_notes[k].append(nv.value_note(j))
                guitar_frets[k].append(st.string_list()[l].index(j))
    return guitar_notes, guitar_frets

def muted_notes(comb_inp):
    '''Удаление неиграемые нот, если они не крайние'''
    pass


def guitar_chord_vers0():
    '''Порядок обработки комбинаций.
    Дважды проводит проверку check_chord, до удаления обращений и после'''
    raw = position_raw()
    comb = combinations(raw)
    checked = check_chord(comb)  #здесь проверяем сырой пул комбинаций
    pure = no_inversion(checked)
    checked_pure = check_chord(pure)  #здесь проверяем комбинации без обращений
    notes, frets = notes_frets(checked_pure)
    print('Численные значения: {} \nНоты: {} \nТабулатура: {}'.format(checked_pure, notes, frets))


def guitar_chord_vers1():
    '''Порядок обработки комбинаций. Отличие от прошлой версии: сначала удаляет обращения, потом проводит проверку
    check_chord'''
    raw = position_raw()
    comb = combinations(raw)
    pure = no_inversion(comb)
    checked = check_chord(pure)
    notes, frets = notes_frets(checked)
    print('Численные значения: {} \nНоты: {} \nТабулатура: {}'.format(checked, notes, frets))


def test_all():
    '''Создает все возможные комбинации. Среднее время 2m.'''
    for i in nv.allnotes:
        for k,v in types.dict.items():
            note = i  #локальная переменная
            chord = k  #локальная переменная
            print(note, chord)
            guitar_chord_vers1()

note = 'c' #строчные буквы
chord = 'major_nona' #список аккордов в chord_types
fret_min = 0
fret_max = 3


chord_simple_note()
guitar_chord_vers1()

# start = datetime.datetime.now()
# test_all()
# end = datetime.datetime.now()
# print('totally time is ', end - start)
