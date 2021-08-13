import pandas as pd
import os

def get_data():
    path = 'C:/Users/KomyshevDA/Downloads/Тестовое для РИТ/'
    data_a = pd.read_table(os.path.join(path, 'Приложение А')).rename(
        columns={"Дата": "Date", "Исполнитель": "Worker", "Задача": "Task", "Часы": "Hours"})
    data_a['Date'] = pd.to_datetime(data_a['Date'], infer_datetime_format=True, format="%Y-%m-%d", errors='coerce')
    data_b = pd.read_table(os.path.join(path, 'Приложение B')).rename(columns={"Задача": "Task", "Оценка": "Grade"})
    data_c = pd.read_table(os.path.join(path, 'Приложение C')).rename(columns={"Исполнитель": "Worker", "Ставка": "Rate"})
    return data_a, data_b, data_c