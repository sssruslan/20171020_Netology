#Взять из github-репозитория все файлы с новостями в формате json: newsfr.json, newsit.json, newsafr.json, newscy.json.
#Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла.
#Не забываем про декомпозицию и организацию кода в функции. В решении домашнего задания вам могут помочь: split(), sort() или sorted().

#{'rss': {'_version': '2.0',
#         '_xmlns:votpusk': 'https://www.votpusk.ru/news.asp',
#         'channel': {'category': 'ВгаШЧЬ - єШЯа',
#                     'description': 'єШЯа - »ХЭвР вгаШбвШзХбЪШе ЭЮТЮбвХЩ '
#                                    'ЯЮавРЫР І ѕВїГБє.АГ ',
#                     'items': [{'_id': '545166',
#                                'description': 'ІЫРбвШ єШЯаР аРббзШвлТРов '

# функция чтения файлов (ГОТОВО)
def read_files(name):
    import json
    from pprint import pprint
    import chardet
    import locale

    with open(name, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)

    with open(name) as f:
        data = json.load(f)
        data_join = ''
        for i in data['rss']['channel']['items']:
           data_join += ' ' + i['description']
        data_join = data_join.encode(locale.getpreferredencoding())
        original_text = data_join.decode(result['encoding'])
        return original_text

# функция подсчета слов длиннее 6 символов (ГОТОВО)
def count_word(original_text):
    to_list = original_text.split(' ')
    to_set = set()
    for i in to_list: # заполняем множество с уникальными словами длиной больше 6 символов
        if len(i) > 6:
            to_set.add(i)
    word_value = {} # ищем слова из множества в списке, считаем количество, формируем словарь типа слово:количество
    for i in to_set:
        count = 0
        for j in to_list:
            if i == j:
                count += 1
        word_value[i] = count
    return word_value # возвращаем словарь {слово:количество}

# функция сортировки и вывода ТОП-10 
def sort_top(word_value):
    l = lambda word_value: word_value[1]
    sort_list = sorted(word_value.items(), key = l, reverse = True)
    #sort_list = sorted(word_value.items(), key = lambda (key, value): value, reverse = True)
    count = 1
    top_10 = {}
    for i in sort_list:
        top_10[count] = i        
        count += 1        
        if count == 10:
            break
    return top_10

# Первая версия
#def sort_top(word_value):
#    register = list()
#    l_dict = str(len(word_value))
#    for i in word_value.items():
#        l_word = str(i[1])
#        register.append((len(l_dict)-len(l_word))*'0' + str(i[1]) + ' ' + i[0]) # разворачиваем и добавляем нули перед количеством для сортировка, делаем слияние элементов = '00012 слово'
#    register.sort(reverse = True)
#    top_10_list = list()
#    top_10 = {}
#    count = 1
#    for j in register:
#        top_10[count] = j.split(' ') # получаем словарь типа {1: (количество, слово)}          
#        top_10[count][0] = int(top_10[count][0])   
#        if count == 10:
#            break
#        count += 1
#    return top_10 # возвращаем отсортированный словарь ТОП-10 {номер: (количеств, слово)}

# главная функция: запрашивает имя файла, запускает другие функции (ГОТОВО)
def main():
        while True:
            name = input('Введите имя файла: newsfr.json, newsit.json, newsafr.json, newscy.json. Выход - exit: ')
            if name == 'newsfr.json' or name == 'newsit.json' or name == 'newsafr.json' or name == 'newscy.json':
                print('Идет обработка файла ...')
                top_10 = sort_top(count_word(read_files(name)))
                for k in top_10.values():
                    print (k[1], ': ', k[0])
            elif name == 'exit':
                break
            else:
                print('Некорректный ввод, повторите.')
        
main()