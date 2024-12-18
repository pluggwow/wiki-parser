# functions - модуль для импорта функций для решения задачи
# TODO - добавить импорты внешних зависимостей 
# import <название зависимости>
import requests
import bs4

def get_response(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на успешность запроса
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'wikitable'})
        if table is None:
            raise ValueError("Таблица не найдена")
        return table
    except Exception as e:
        print(f"Ошибка при получении данных: {e}")
        return None

def extract_currency_data(table):
    codes = []
    nums = []
    currencies = []

    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        if len(cols) >= 3:
            codes.append(cols[0].text.strip())
            nums.append(cols[1].text.strip())
            currencies.append(cols[2].text.strip())

    return codes, nums, currencies

# Пример вызова функции
url = 'https://en.wikipedia.org/wiki/ISO_4217'
table = get_response(url)
if table:
    codes, nums, currencies = extract_currency_data(table)
else:
    print("Не удалось получить данные.")
