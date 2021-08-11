from main import dates


def get_lazy_employee():
    print("Недоработки в будни (меньше 8 часов:")
    print(dates[(dates['Hours'] < 8) & (dates['Day of week'] < 5)])