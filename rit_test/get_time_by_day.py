from main import get_dates


def get_time_by_day():
    print("Среднее время, затраченное на решение задач каждым из исполнителей в часах:")
    print(get_dates())

if __name__ == '__main__':
    get_time_by_day()