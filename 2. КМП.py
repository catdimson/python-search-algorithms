def input_data():
    global template, path_to_text, string
    template = input("Введите шаблон: " + "\n")
    path_to_text = input("Введите путь к файлу (по умолчанию 'D:\Учёба\\7 семестр -\- Технологии обработки информации (Экз)\Лабораторная работа №1\Testing text 2')" + "\n")
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


def prefix_function(template):
    length = len(template)
    prefix_func = [0] * length
    i = 1
    while i < length:
        k = 1
        while k <= i:
            if template[:k] == template[i-k+1:i+1]:
                prefix_func[i] = k
            k += 1
        i += 1
    return prefix_func


def search_template(string, template, prefix_f):
    i, index = 0, 0
    length_string = len(string)
    length_template = len(template)
    while i < length_string:
        if string[i] == template[index]:
            index += 1
            if index == length_template:
                return i - index + 1
        elif index == 0:
            i += 1
            continue
        else:
            index = prefix_f[index - 1]
        i += 1
    return -1


def algorithm_complexity(string, template):
    # O(n+m), n - строка, m - подстрока
    n = len(string)
    m = len(template)
    complexity = m + n
    print("Сложность алгоритма: " + str(complexity))


input_data()
get_text()
prefix_f = prefix_function(template)
result = search_template(string, template, prefix_f)
if result == -1:
    print("Совпадений не обнаружено")
else:
    print("Совпадение обнаружено на позиции " + str(result) + " исходной строки")
algorithm_complexity(string, template)
