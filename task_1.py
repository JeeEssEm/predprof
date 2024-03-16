import csv


def main():
    with open(r'books_rowling.csv', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        # открываем csv файл при помощи библиотеки csv
        for line in list(reader)[1:]:
            # примерно понимаем объём файла, поэтому смело кастим к типу список и читаем строки без первой
            # (без заголовка)
            book_id, author, orig_title, rating = line  # вытаскиваем данные
            rating = float(rating.replace(',', '.'))  # замечаем, что в дробных числах используется запятая вместо точки
            if rating > 8:
                print(f'{author} - {orig_title}\t {rating}')  # форматированный вывод


main()
