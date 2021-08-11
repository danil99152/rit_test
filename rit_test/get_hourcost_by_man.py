from main import mean_worktime


def get_hourcost_by_man():
    print("Среднее время, затраченное каждым исполнителем:")
    print(mean_worktime())

if __name__ == '__main__':
    get_hourcost_by_man()