import csv


def linear_search(arr: list[list[str]], value: str, index: int):
    """ Функция линейного поиска по списку
     arr - список с книгами
     value - значение, которое ищем
     index - индекс, который показывает на каком месте должно находиться искомое значение
     """
    res = []
    for line in arr:  # бежим по всем строкам
        if value in line[index]:  # в задании не уточнено, нужно ли делать точный поиск, поэтому я решил проверять так
            if len(res) == 5:
                return res
            res.append(line)
    return res


def main():

    # был использован файл 'books.csv', т.к. организаторы не смогли предоставить books.txt
    with open(r'books.csv', encoding='utf-8') as f:
        # снова оцениваем размер файла и понимаем, что можно не читать построчно файл, а сразу закастить к списку
        lines = list(csv.reader(f, delimiter=';'))[1:]
        book = input()
        while book != 'хватит':  # проверяем, закончили ли поиск
            search = linear_search(lines, book, 4)
            if search:
                for bk in search:
                    print(f'{bk[4]} - {bk[1]} - {bk[0]} - {bk[5]}')  # используем форматированный вывод
                if len(search) == 5:
                    print('и др.')
            else:
                print('Данной книги в этой библиотеке нет')

            book = input()


main()
