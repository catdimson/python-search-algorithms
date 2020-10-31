def input_data():
    global template, path_to_text, string
    template = input("Введите шаблон: " + "\n")
    path_to_text = input("Введите путь к файлу (по умолчанию 'D:\Учёба\\7 семестр -\- Технологии обработки информации (Экз)\Лабораторная работа №1\Testing text 1')" + "\n")
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


def verification(subsrting, template):
    flag = True
    k = 0
    while k < len(template):
        if template[k] != subsrting[k]:
            flag = False
            break
        k += 1
    return flag


def search_template(string, template):
    i = 0
    length_template = len(template)
    length_string = len(string)
    while True:
        if i + length_template > length_string:
            print("Совпадений не обнаружено")
            break

        if verification(string[i:(i + length_template)], template):
            print("Совпадение обнаружено на позиции " + str(i) + " исходной строки")
            break
        i += 1


def algorithm_complexity(string, template):
    # O((n-m+1)*m), n - строка, m - подстрока
    n = len(string)
    m = len(template)
    complexity = ((n - m + 1) * m)
    print("Сложность алгоритма: " + str(complexity))


input_data()
get_text()
search_template(string, template)
algorithm_complexity(string, template)


