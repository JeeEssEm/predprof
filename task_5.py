import csv


def main():
    res = {}
    with open(r'books.csv', encoding='utf-8') as f:
        # снова оцениваем размер файла и понимаем, что можно не читать построчно файл, а сразу закастить к списку
        lines = list(csv.reader(f, delimiter=';'))[1:]
        for line in lines:
            author = line[2]
            rating = float(line[5].replace(',', '.'))  # приводим к типу float
            if res.get(author):  # если автор существует в словаре, то добавляем одно из значений его рейтинга
                res[author].append(rating)
            else:
                res[author] = [rating]  # иначе создаем список с одним значением рейтинга
    lst = []
    for author, rating in res.items():
        res[author] = sum(rating) / len(rating)  # находим среднее арифметическое рейтинга
        lst.append((author, res[author]))  # добавляем в список
    lst.sort(key=lambda pair: pair[1], reverse=True)  # сортируем по рейтингу
    for i in range(10):
        print(f'Автор: {lst[i][0]}, Средний рейтинг: {lst[i][1]}')  # форматированный вывод автора с рейтингом


main()
