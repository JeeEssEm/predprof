import csv


def qsort(arr: list[list[str | float]], index) -> list[list[str | float]]:
    """ функция быстрой сортировки
        arr - переменная, принимающая на вход список, состоящий из кортежей
        index - индекс элемента, по которому будут сортироваться кортежи
    """
    if len(arr) <= 1:
        return arr

    left = [el for el in arr if el[index] < arr[0][index]]
    right = [el for el in arr if el[index] > arr[0][index]]
    return qsort(left, index) + [arr[0]] + qsort(right, index)


def main():
    with open(r'books.csv', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        # снова оцениваем размер файла и понимаем, что можно не читать построчно файл, а сразу закастить к списку
        # собираем в books только нужные нам колонки + приводим рейтинг к типу float
        books = [[line[2], line[4], float(line[5].replace(',', '.'))] for line in list(reader)[1:]]
        books = qsort(books, 2)  # сортируем книжки по второму индексу - рейтингу
        for i in range(3):
            # сначала приводим все элементы списка к строке, потом при помощи join склеиваем их
            print(' - '.join(map(str, books[i])))


main()
