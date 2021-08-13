from data import get_data
from get_hourcost_by_man import get_hourcost_by_man
from get_profitability import get_new_data_a


def get_late():
    print('Средний вылет работника по каждой задаче:')
    data_a = get_new_data_a()
    _,data_b,_ = get_data()
    grade = data_a.drop(['Date', 'Cost'], axis=1)
    hours_list = []
    for worker, task in zip(grade['Worker'], grade['Task']):
        hours = grade[(grade['Worker'] == worker) & (grade['Task'] == task)]['Hours']
        hours_list.append(hours.sum())
    grade['Hours'] = hours_list
    grade = grade.drop_duplicates()
    grade = grade.reset_index(drop=True)
    grade = grade.merge(data_b, how='left', on=['Task', 'Task'])
    grade['Mean late'] = (grade['Hours'] - grade['Grade']) / grade['Grade'] * 100  # Средний "вылет"
    print(grade.filter(['Worker', 'Task', 'Mean late'],axis=1))

    print('Средний вылет по сотруднику:')
    mean_worker_grade_list = []
    hourcost_by_man = get_hourcost_by_man()
    for worker in hourcost_by_man['Worker']:
        grades = grade[grade['Worker'] == worker]['Mean late']
        mean_worker_grade_list.append(grades.sum() / len(grades))
    hourcost_by_man['Mean worker late'] = mean_worker_grade_list
    print(hourcost_by_man.filter(['Worker', 'Mean worker late'],axis=1))

if __name__ == '__main__':
    get_late()