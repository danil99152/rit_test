import pandas as pd

from data import get_data


def get_hourcost_by_man():
    data_a, _, data_c = get_data()
    hourcost_by_man = pd.DataFrame(data={'Worker': [], 'Hours': [], 'Mean time': []})
    for project in data_a['Worker'].unique():
        task = data_a[data_a['Worker'] == project]['Worker']
        hours = data_a[data_a['Worker'] == project]['Hours'].sum()
        mean_hours = hours / len(data_a[data_a['Worker'] == project]['Hours'])
        hourcost_by_man = hourcost_by_man.append({'Worker': task.values[0], 'Hours': hours, 'Mean time': mean_hours},
                                                 ignore_index=True)
    hourcost_by_man = hourcost_by_man.merge(data_c, on=['Worker', 'Worker'], how='left')
    hourcost_by_man['Salary'] = hourcost_by_man['Hours'] * hourcost_by_man['Rate']
    return hourcost_by_man

def print_hourcost_by_man():
    hourcost_by_man = get_hourcost_by_man()
    print("Среднее время, затраченное каждым исполнителем:")
    print(hourcost_by_man.filter(['Worker',  'Hours',  'Mean time'], axis=1))

if __name__ == '__main__':
    print_hourcost_by_man()