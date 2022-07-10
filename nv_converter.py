'''В модуле расположены инструменты для конвертирования нот в численные значения и обратно. Нулевое значение присвоено
'с0' - 'До' субконтроктавы. Каждый последующий тон равен n+1'''
allnotes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']  # список возможных нот, порядок важен


def note_value(inp_note):
    '''Конвертируем ноты в численные значения.'''
    note = ''.join([i for i in inp_note if not i.isdigit()]) #отделяем ноту и октаву
    octa = [int(i) for i in inp_note if i.isdigit()][0]
    value = allnotes.index(note) + (octa * 12) #12 - количество полутонов на октаву
    return value


def value_note(inp_value):
    '''Конвертируем численные значения в ноты'''
    octa = str(inp_value // 12)
    value = str(allnotes[inp_value % 12])
    note = value + octa
    return note

def ignore_oct(value):
    '''Упрощаем численное значение ноты. По сути, получаем числовое значение субконтроктавы.'''
    value = value % 12
    return value
