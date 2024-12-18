# main - стартовый модуль проекта

 # импорты из модуля
from functions import func1, extract_currency_data

# функция запуска импортированных функций 
def main():
    table = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <table>
            <th>Artur</th>
            <tr>Altunyan</tr>
        </table>
    </body>
    </html>
    """ 
    print(extract_currency_data(table))

# инициализонный скрипт 
if __name__ == '__main__':
    main()