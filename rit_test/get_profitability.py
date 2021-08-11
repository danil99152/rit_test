from main import profitability

def get_profitability():
    prof,_ = profitability()
    print("Рентабельность проекта =", prof)

if __name__ == '__main__':
    get_profitability()