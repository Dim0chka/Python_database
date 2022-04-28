import json


def ДОБАВИТЬ(student: str, year: int, sr_inf: float, sr_math: float, sr_phis: float):
    obj = json.loads(open("date.json", "r").read())  # перевод из строки в массив
    obj[student] = {
        "student": student,
        "year": year,
        "sr_inf": sr_inf,
        "sr_math": sr_math,
        "sr_phis": sr_phis
    }
    file = open("date.json", "w")
    file.write(json.dumps(obj, indent=4))  # перевод из массива в строку, отступ - 4
    file.close()

    print("User added")


def ПОКАЗАТЬ(student: str):
    obj = json.loads(open("date.json", "r").read())

    if student not in obj:  # если в массиве нет такого дочернего обьекта, то выводим "Такого нет"
        print("Такого нет")
    else:
        # иначе выводим данные этого дочернего обьекта
        print(obj[student]["student"], obj[student]["year"], obj[student]["sr_inf"], obj[student]["sr_math"], obj[student]["sr_phis"])


def УДАЛИТЬ(student: str):
    obj = json.loads(open("date.json", "r").read())

    if student not in obj:
        print("Такого нет")
    else:
        obj.pop(student)

    if obj == "":
        file = open("date.json", "w")
        file.write(json.dumps({}))
        file.close()
    else:
        file = open("date.json", "w")
        file.write(json.dumps(obj, indent=4))
        file.close()


def СВОДКА(number: int):
    #сводка
    summary = {
        0: "student",
        1: "year",
        2: "sr_inf",
        3: "sr_math",
        4: "sr_phis"
    }

    # obj.items() - получает все элементы словаря и возращает обьект, который отображает список пар по ключу и их значению
    # [(key, value), (key, value), (key, value)]
    obj = json.loads(open("date.json", "r").read())
    obj_sort = sorted(obj.items(), key=lambda x: x[1][summary[number]])

    for x in obj_sort:
        student = x[0]
        ПОКАЗАТЬ(student)


def СОХРАНИТЬ(name_file: str):
    obj = json.loads(open("date.json", "r").read())
    arr = []  # массив, в котором хранятся данные о дочерних обьектах obj из json

    for student in obj:
        arr.append(f'{obj[student]["student"]} {obj[student]["year"]} {obj[student]["sr_inf"]} {obj[student]["sr_math"]} {obj[student]["sr_phis"]}')

    open(name_file, "w").write("\n".join(arr))


def ЗАГРУЗИТЬ(name_file: str):
    file = (open(name_file, "r").read()).split("\n")

    for x in file: #проходимя по каждому элементу в массиве
        arr_student = x.split() #переводим в массив данные об ученике
        ДОБАВИТЬ(arr_student[0], arr_student[1], arr_student[2], arr_student[3], arr_student[4])

    #     obj[arr_student[0]] = {
    #         "student": arr_student[0],
    #         "year": arr_student[1],
    #         "sr_inf": arr_student[2],
    #         "sr_math": arr_student[3],
    #         "sr_phis": arr_student[4]
    #     }
    #
    # open("date.json", "w").write(json.dumps(obj, indent=4))


while True:
    query = input().split(" ")

    if query[0] == "ДОБАВИТЬ":
        ДОБАВИТЬ(str(query[1]), int(query[2]), float(query[3]), float(query[4]), float(query[5]))
        # print((open("date.json", "r").read()))

    elif query[0] == "ПОКАЗАТЬ":
        ПОКАЗАТЬ(str(query[1]))

    elif query[0] == "УДАЛИТЬ":
        УДАЛИТЬ(str(query[1]))

    elif query[0] == "СВОДКА":
        СВОДКА(int(query[1]))

    elif query[0] == "СОХРАНИТЬ":
        СОХРАНИТЬ(str(query[1]))

    elif query[0] == "ЗАГРУЗИТЬ":
        ЗАГРУЗИТЬ(str(query[1]))

    else:
        break

