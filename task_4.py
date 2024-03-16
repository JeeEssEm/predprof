import csv


def set_mark(line):
    """ функция, добавляющая рейтинг к строке
     line - переменная, содержащая исходную строку
     """

    rating = float(line[5].replace(',', '.'))  # вытаскивам рейтинг и приводим к float
    if rating < 5:
        line.append('не рекомендовать')
    elif 5 <= rating < 8:
        line.append('рекомендовать после')
    elif rating >= 8:
        line.append('рекомендовать в первую очередь')
    return line


def main():
    path = input()  # получаем путь до исходного файла
    flag = True
    res = []
    with open(rf'{path}', encoding='utf-8') as rf:
        for line in csv.reader(rf, delimiter=';'):
            if flag:  # костыль для пропуска чтения первой строки
                flag = False
                res.append(line + ['recommend'])  # записываем заголовок
                continue
            res.append(set_mark(line))
    with open('books_grade.csv', 'w', encoding='utf-8') as wf:
        for row in res:
            wf.write(';'.join(row) + '\n')


main()
