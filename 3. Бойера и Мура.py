def input_data():
    global template, path_to_text, string
    template = input("Введите шаблон: " + "\n")
    path_to_text = input("Введите путь к файлу (по умолчанию 'D:\Учёба\\7 семестр -\- Технологии обработки информации (Экз)\Лабораторная работа №1\Testing text 3')" + "\n")
    string = ""


def get_text():
    while True:
        try:
            global path_to_text, string
            file = open(path_to_text, "r")

            for line in file:
                string += line
            file.close()
            break

        except:
            path_to_text = input("Не найден указанный путь. Попробуйте еще раз, или введите 'NO', чтобы завершить: " + "\n")
            if path_to_text.upper() == "NO":
                break


def build_table(template):
    table = {}
    table["other"] = len(template)
    i = 1
    while i < len(template):
        if template[~i] in table:
            i += 1
            continue
        else:
            table[template[~i]] = i
        i += 1
    if not(template[len(template) - 1] in table):
        table[template[len(template) - 1]] = len(template)
    # print(table)
    return table


def search_template(string, template, table):
    i = len(template) - 1       # начальный ИНДЕКС СТРОКИ
    while i < len(string):      # выполняем проход по циклу пока ИНДЕКС СТРОКИ меньше ДЛИНЫ СТРОКИ
        index = i               # ИНДЕКС ШАБЛОНА
        counter = 0             # число на которое нужно сдвигаться счётчик
        while counter < len(template):                      # пока счётчик  меньше длины шаблона
            element = string[index - counter]               # значение элемента на позиции строки
            if element == template[~counter]:
                # print('counter: ' + str(counter))
                # print('element: ' + element)
                # print('position: ' + str(index - counter))
                counter += 1
                if counter == len(template):
                    return index - counter + 1
                continue
            else:
                # print('элемент конечный: ' + element + '. Его индекс: ' + str(i))
                if element in table:
                    i = i - counter + table[string[index - counter]]
                else:
                    i = i - counter + table["other"]
                    # print('следующий элемент: ' + str(i))
                index = i
                counter = 0
                break
    return -1


def algorithm_complexity(string, template):
    # O(n+m), n - строка, m - подстрока
    n = len(string)
    m = len(template)
    complexity = m + n
    print("Сложность алгоритма: " + str(complexity))


input_data()
get_text()
table = build_table(template)
result = search_template(string, template, table)
if result == -1:
    print("Совпадений не обнаружено")
else:
    print("Совпадение обнаружено на позиции " + str(result) + " исходной строки")
algorithm_complexity(string, template)
