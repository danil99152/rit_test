def help():
    print(
        "Справка о командах:\n"
        "gethourcost: Общие трудозатраты на проект в часах;\n"
        "Среднее время, затраченное на решение задач в часах;\n"
        "Медианное время, затраченное на решение задач в часах;\n"
        "gethourcostbyman: Среднее время, затраченное на решение задач каждым из исполнителей в часах\n"
        "getprofability: Рентабельность\n"
        "gettimebyday: среднее количество часов, отрабатываемое каждым сотрудником за день\n"
        "getlazy: Получить недорабатывающих сотрудников в будние дни\n"
        "getabsenteeism: Получить все пропуски\n"
        "getlate: Получить все 'вылеты'\n"
        "generategraph: сгенерировать сводный график"
)

if __name__ == '__main__':
    help()