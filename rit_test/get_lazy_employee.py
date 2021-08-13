from get_time_by_day import get_dates


def get_lazy_employee():
    print("Недоработки в будни (меньше 8 часов:")
    dates = get_dates()
    print(dates[(dates['Hours'] < 8) & (dates['Day of week'] < 5)])

if __name__ == '__main__':
    get_lazy_employee()