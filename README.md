# Набор программ для работы с книгами
## Описание
набор готовых программ для работы с csv файлами, заданного формата.

## Как установить и запустить
Требуется наличие `[python 3.12](https://www.python.org/)` выше
1. клонируем проект
2. Переходим в папку с проектом
   1. Открывам powershell/cmd/IDE (pycharm/vs code/etc...)
   2. запускаем нужный нам файл с помощью команды: `python task_1.py`
## Как использовать проект
Пользователю предоставлены 5 готовых алгоритмов для работы с csv файлами,
определённого формата. Пользователь может отредактировать исходный код, чтобы
данный проект мог выполнить задачу, необходимую пользователю.

Какие алгортмы реализованы:
1. task_1.py - выводит книги с рейтингом больше 8
2. task_2.py - выводит 3 книги с худшим рейтингом
3. task_3.py - ищет книги в файле. Программа продолжает работать, пока пользователь не введёт стоп-слово "хватит"
4. task_4.py - добавляет колонку с рекоменадацией к каждой книге
5. task_5.py - выводит 10 авторов с наибольшим средним рейтингом. Внутри реализована хэш-таблица, где: ключ - автор, значение - средний рейтинг
