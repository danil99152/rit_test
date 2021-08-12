from data import get_data
import pandas as pd

def get_hourcost():
    data_a, _, _ = get_data()
    hourcost = pd.DataFrame(data={'Task': [], 'Hours': []})
    for project in data_a['Task'].unique():
        task = data_a[data_a['Task'] == project]['Task']
        hours = data_a[data_a['Task'] == project]['Hours'].sum()
        hourcost.append({'Task': task.values[0], 'Hours': hours}, ignore_index=True)
    return hourcost

def print_hourcost():
    hourcost = get_hourcost()
    print("Время затраченное на задачу:")
    print(hourcost)
    print("Среднее время", hourcost['Hours'].mean())
    print("Медианное время", hourcost['Hours'].median())

if __name__ == '__main__':
    print_hourcost()