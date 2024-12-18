# main - стартовый модуль проекта

 # импорты из модуля
from parse import func1, extract_currency_data, get_response

# функция запуска импортированных функций 
def main():
    url = 'https://en.wikipedia.org/wiki/ISO_4217'
    print(extract_currency_data(get_response(url)))

# инициализонный скрипт 
if __name__ == '__main__':
    main()