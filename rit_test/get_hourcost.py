from main import hourcost


def get_hourcost():
    cost = hourcost()
    print("Время затраченное на задачу:")
    print(cost)
    print("Среднее время", cost['Hours'].mean())
    print("Медианное время", cost['Hours'].median())

if __name__ == '__main__':
    get_hourcost()