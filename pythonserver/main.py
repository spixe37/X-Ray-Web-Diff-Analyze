datadb = {
    "Анатаз TiO2": [
        (3.508, 10),
        (2, 425, 1),
        (2.372, 5),
        (1.887, 9),
        (1.696, 7),
        (1.662, 7),
        (1.447, 7),
        (1.361, 6),
        (1.335, 6),
        (1.261, 7),
        (1.247, 2),
        (1.163, 6),
        (1.158, 1),
        (1.054, 1),
        (1.048, 5),
        (1.041, 5),
        (1.0155, 5),
        (1.004, 2),
        (0.994, 1),
        (0.953, 7),
        (0.944, 6),
        (0.917, 7),
        (0.911, 7)
    ],
    "Бадделеит ZrO2": [
        (3.667, 3),
        (3.159, 10),
        (2.826, 8),
        (2.611, 6),
        (2.535, 4),
        (2.329, 3),
        (2.201, 5),
        (2.003, 4),
        (1.845, 6),
        (1.807, 6),
        (1.690, 5),
        (1.654, 5),
        (1.607, 2),
        (1.538, 4),
        (1.507, 3),
        (1.472, 3),
        (1.447, 3),
    ],
    "Микроклин K2O·Al2O3·6SiO2": [
        (4.18, 6),
        (3.95, 2),
        (3.81, 4),
        (3.70, 2),
        (3.58, 4),
        (3.46, 4),
        (3.35, 4),
        (3.22, 10),
        (3.04, 4),
        (2.94, 2),
        (2.88, 4),
        (2.77, 4),
        (2.63, 4),
        (2.58, 4),
        (2.51, 4),
        (2.34, 2)
    ],
    "Мелилит Са2· (Al, Mg, Si)·Si2O7": [
        (4.228, 2),
        (3.712, 4),
        (3.468, 2),
        (3.074, 5),
        (2.858, 10),
        (2.742, 2),
        (2.522, 2),
        (2.452, 7),
        (2.409, 3),
        (2.399, 4),
        (2.300, 5),
        (2.291, 3),
        (2.205, 2),
        (2.114, 2),
        (2.040, 5),
        (1.988, 2),
        (1.939, 5),
        (1.881, 4),
        (1.853, 3),
        (1.828, 5),
        (1.762, 8),
        (1.758, 8),
        (1.734, 3),
        (1.718, 3),
        (1.682, 2),
        (1.640, 4),
        (1.636, 4),
        (1.608, 3),
        (1.543, 2),
        (1.513, 7),
        (1.48, 3)
    ],
    "Анортит (кальцинированный полевой шпат) CaO·Al2O3 ·2SiO2": [
        (4.08, 3),
        (3.80, 3),
        (3.63, 2),
        (3.37, 2),
        (3.26, 1),
        (3.20, 10),
        (3.15, 2),
        (2.948, 4),
        (2.832, 4),
        (2.648, 2),
        (2.509, 6),
        (2.135, 6),
        (2.097, 3),
        (2.021, 3),
        (1.926, 3),
        (1.877, 2),
        (1.836, 5),
        (1.762, 5),
        (1.714, 2),
        (1.626, 3),
        (1.532, 2),
        (1.480, 4),
        (1.451, 3),
        (1.410, 2),
        (1.385, 4),
        (1.360, 3),
        (1.342, 3),
        (1.317, 2),
        (1.274, 2),
        (1.211, 3),
        (1.166, 4),
        (1.127, 2),
        (1.079, 3),
        (1.064, 4)
    ]
}

info = [
    (4.18, 6),
    (3.95, 2),
    (3.81, 4),
    (3.7, 2),
]


def findNearest(number, array):
    list1 = []
    for i in array:
        if number[1] == i[1]:
            # print(str(number) + " | " + str(i))
            list1.append(i)
    if len(list1) > 0:
        return get_nearest_value((i[0] for i in list1), number[0])
    return None


def compare(data, info):
    for i in data:
        x = findNearest(i, info)
        if x != None:
            if i[0] < x:
                # print(i[0]/x*100)
                yield i[0]/x*100
            else:
                # print(x/i[0]*100)
                yield x/i[0]*100



def get_nearest_value(iterable, value):
    return min(iterable, key=lambda x: abs(x - value))

def find(inf):
    for i in datadb:
        dataInfo = datadb[i]
        if len(inf) < 1:
            continue
        out = list(compare(dataInfo, inf))[0:len(inf)]
        s = 0
        for j in out:
            s += j
        if len(out) < 1:
            continue
        s /= len(out)
        yield (i, s)


# print(list(find(info)))


# Входные - массив из расстояния и номера
# Выходные данные - (вещество, процентная вероятность)