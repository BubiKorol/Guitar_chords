'''Каждая функция получает основную ноту аккорда, и возвращает список со значением всех нот.
В словаре содержится соответствие названий аккордов и их значений. Ключи из этого списка вводятся в переменной
chord_position.chord.
Возможно, надо прописать отдельную обработку мажора и минора, вынести во внешнее пространство переменную note2,
что уменьшит количество функций и длину кода.
'''

def power(tonic):
    "Квинт аккорд. Пример C5"
    note2 = tonic + 7
    chord = [tonic, note2]
    return chord

def major(tonic):
    """Обычный мажор. Пример С - до мажор."""
    note2 = tonic+4
    note3 = tonic+7
    chord = [tonic, note2, note3]
    return chord


def minor(tonic):
    """Обычный мажор. Пример Сm - до минор."""
    note2 = tonic + 3
    note3 = tonic + 7
    chord = [tonic, note2, note3]
    return chord

def sus2(tonic):
    """Аккорд с задержанием на второй ступени. Сsus2. Ес-но, нет мажоров и миноров."""
    note2 = tonic+2  #большая секунда вместо терций
    note3 = tonic+7
    chord = [tonic, note2, note3]
    return chord


def sus4(tonic):
    """Аккорд с задержанием на четвертой ступени. Сsus4. Ес-но, нет мажоров и миноров."""
    note2 = tonic + 5  #кварта вместо терций
    note3 = tonic + 7
    chord = [tonic, note2, note3]
    return chord

def aug(tonic):
    """Увеличенный аккорд. Пример: С+ или Сaug или C+5. Есть ли аналогичный минорный?"""
    note2 = tonic+4
    note3 = tonic+8  #малая секста
    chord = [tonic, note2, note3]
    return chord


def dim(tonic):
    """Уменьшенный аккорд. Пример: Сdim. Есть ли аналогичный мажорный?"""
    note2 = tonic+3
    note3 = tonic+6  #тритон
    chord = [tonic, note2, note3]
    return chord


def major_sept(tonic):
    """Мажорный септаккорд. Пример: С7"""
    note2 = tonic + 4
    note3 = tonic + 7
    note4 = tonic + 10
    chord = [tonic, note2, note3, note4]
    return chord


def minor_sept(tonic):
    """Минорный септаккорд. Пример: Сm7"""
    note2 = tonic + 3
    note3 = tonic + 7
    note4 = tonic + 10
    chord = [tonic, note2, note3, note4]
    return chord

def major_sept_plus5(tonic):
    """Мажорный септаккорд c повышенной квинтой. Пример: С7+5"""
    note2 = tonic + 4
    note3 = tonic + 8 #малая секста
    note4 = tonic + 10
    chord = [tonic, note2, note3, note4]
    return chord


def major_sept_minus5(tonic):
    """Мажорный септаккорд c пониженной квинтой. Пример: С7-5"""
    note2 = tonic + 4
    note3 = tonic + 6 #тритон
    note4 = tonic + 10
    chord = [tonic, note2, note3, note4]
    return chord


def minor_sept_minus5(tonic):
    """Минорный септаккорд c пониженной квинтой. Пример: С7-5."""
    note2 = tonic + 3
    note3 = tonic + 6 #тритон
    note4 = tonic + 10
    chord = [tonic, note2, note3, note4]
    return chord


def major_sept_big(tonic):
    """Большой мажорный септаккорд. Пример Сmaj7"""
    note2 = tonic + 4
    note3 = tonic + 7
    note4 = tonic + 11 #большая септа
    chord = [tonic, note2, note3, note4]
    return chord


def minor_sept_big(tonic):
    """Большой минорный септаккорд. Пример Сmmaj7 или Cm+7"""
    note2 = tonic + 3
    note3 = tonic + 7
    note4 = tonic + 11 #большая септа
    chord = [tonic, note2, note3, note4]
    return chord

def major_sekst(tonic):
    """Мажорный секстаккорд. Пример С6. Секстаккорд именно гитарный, в теории музыки это первое
    обращение аккорда"""
    note2 = tonic + 4
    note3 = tonic + 7
    note4 = tonic + 9 #большая секста
    chord = [tonic, note2, note3, note4]
    return chord


def minor_sekst(tonic):
    """Минорный секстаккорд. Пример: Cm6. Секстаккорд именно гитарный, в теории музыки это первое
    обращение аккорда"""
    note2 = tonic + 3
    note3 = tonic + 7
    note4 = tonic + 9 #большая секста
    chord = [tonic, note2, note3, note4]
    return chord

def major_nona_add(tonic):
    """Мажорный аккорд с большой ноной . Пример: Сadd9"""
    note2 = tonic + 4
    note3 = tonic + 7
    note4 = tonic + 14
    chord = [tonic, note2, note3, note4]
    return chord


def minor_nona_add(tonic):
    """Минорный аккорд с большой ноной. Пример: Сmadd9"""
    note2 = tonic + 3
    note3 = tonic + 7
    note4 = tonic + 14
    chord = [tonic, note2, note3, note4]
    return chord

def major_nona(tonic):
    """Мажорный нонаккорд. Пример: С9"""
    note2 = tonic + 4
    note3 = tonic + 7
    note4 = tonic + 10
    note5 = tonic + 14
    chord = [tonic, note2, note3, note4, note5]
    return chord


def minor_nona(tonic):
    """Минорный септаккорд. Пример: Сm9"""
    note2 = tonic + 3
    note3 = tonic + 7
    note4 = tonic + 10
    note5 = tonic + 14
    chord = [tonic, note2, note3, note4, note5]
    return chord




dict = {'power': power,'major': major, 'minor': minor, 'sus2': sus2, 'sus4': sus4, 'aug': aug, 'dim': dim,
        'major_sept': major_sept, 'minor_sept': minor_sept, 'major_sept_plus5': major_sept_plus5,
        'major_sept_minus5': major_sept_minus5,'minor_sept_minus5': minor_sept_minus5, 'major_sept_big':
        major_sept_big, 'minor_sept_big': minor_sept_big, 'major_sekst': major_sekst, 'minor_sekst': minor_sekst,
        'major_nona_add': major_nona_add, 'minor_nona_add': minor_nona_add, 'major_nona': major_nona,
        'minor_nona': minor_nona}