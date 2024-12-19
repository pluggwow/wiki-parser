# functions - модуль для импорта функций для решения задачи
# TODO - добавить импорты внешних зависимостей 
# import <название зависимости>


def get_response(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})
    return table


def extract_currency_data(table):
    # Списки для хранения данных
    codes = []
    nums = []
    currencies = []

    # Проходим по всем строкам таблицы, начиная со второй (пропускаем заголовок)
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        if len(cols) >= 3:  # Убедимся, что в строке достаточно столбцов
            codes.append(cols[0].text.strip())  # Код валюты
            nums.append(cols[1].text.strip())    # Номер валюты
            currencies.append(cols[2].text.strip())  # Название валюты

    return codes, nums, currencies

# Пример вызова функции
# codes, nums, currencies = extract_currency_data(table)