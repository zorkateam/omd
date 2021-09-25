import csv


def csv_dict_reader(file_obj, delimiter=";"):
    """
    Read a CSV file using csv.DictReader
    """
    result = []
    reader = csv.DictReader(file_obj, delimiter=delimiter)
    for row in reader:
        result.append(row)
    return result


def csv_dict_writer(result: dict, path='report.csv', delimiter=";"):
    """
    Write a CSV file using csv.DictWriter
    """
    my_file = open(path, 'w')
    with my_file:
        headers = ['Департамент', 'Число работников', 'Вилка зарплат', 'Средняя зарплата']
        writer = csv.DictWriter(my_file, fieldnames=headers, delimiter=delimiter)
        writer.writeheader()
        for dep in result:
            writer.writerow(result[dep])
    print('Отчет успешно сохранен!')


def print_menu():
    """
    Print main menu
    """
    dict_menu = {'1': '1. Вывести иерархию команд',
                 '2': '2. Вывести сводный отчёт по департаментам',
                 '3': '3. Сохранить сводный отчёт',
                 '4': '4. Выход'}
    choice_id = ''
    while choice_id not in dict_menu:
        print('\n')
        print('Выберите пункт меню:')
        for key in dict_menu:
            print(dict_menu[key])
        choice_id = input()
    return int(choice_id)


def create_report(employers_data: list) -> dict:
    """
    Create report from employers list
    """
    result = {}
    for employee in employers_data:
        dep = employee['Департамент']
        salary = int(employee['Оклад'])

        if dep not in result:
            result[dep] = {'Департамент': dep,
                           'Число работников': 1,
                           'Вилка зарплат': {'min': salary,
                                             'max': salary},
                           'Средняя зарплата': salary}
        else:
            emp_count = result[dep]['Число работников']
            avg_salary = result[dep]['Средняя зарплата']
            min_salary = result[dep]['Вилка зарплат']['min']
            max_salary = result[dep]['Вилка зарплат']['min']

            result[dep]['Вилка зарплат']['min'] = min(min_salary, salary)
            result[dep]['Вилка зарплат']['max'] = max(max_salary, salary)
            result[dep]['Средняя зарплата'] = (avg_salary * emp_count + salary) / (emp_count + 1)
            result[dep]['Число работников'] = emp_count + 1
    return result


def format_report(result: dict) -> list:
    """
    Formatting report for pretty print
    """
    string_width = 75
    max_word_length = 16
    formatted_result = []
    headers = ['Департамент', 'Число работников', 'Вилка зарплат', 'Средняя зарплата']

    def format_string(item, max_length=max_word_length):
        """
        Formatting item for report
        """
        word = item
        if type(item) == dict:
            word = '{0:,}'.format(item['min']).replace(',', ' ') + ' - ' \
                 + '{0:,}'.format(item['max']).replace(',', ' ')
        elif type(item) == float:
            word = '{0:,}'.format(round(item)).replace(',', ' ')

        res = f'| {word}' + (max_length - len(str(word))) * ' '
        return res

    formatted_result.append('-' * string_width)
    formatted_result.append(''.join(format_string(header) for header in headers))
    for dep in result:
        formatted_result.append('-' * string_width)
        formatted_result.append(''.join(format_string(word) for word in result[dep].values()))
    return formatted_result


def print_hierarchy(employers_data: list):
    """
    Print hierarchy of departments
    """
    hierarchy = {}
    for employee in employers_data:
        dep = employee['Департамент']
        team = employee['Отдел']

        if dep not in hierarchy:
            hierarchy[dep] = [team]
        elif team not in hierarchy[dep]:
            hierarchy[dep].append(team)

    for dep in hierarchy:
        print(f'Департамент: {dep}')
        print('-' * 30)
        for team in hierarchy[dep]:
            print(f'| {team}')
        print('-' * 30)


if __name__ == "__main__":
    csv_data_path = "Corp Summary.csv"
    csv_report_path = "Report.csv"

    with open(csv_data_path, "r") as f_obj:
        employers = csv_dict_reader(f_obj)

    while 1:
        choice = print_menu()
        if choice == 1:
            print_hierarchy(employers)
        elif choice == 2:
            report = format_report(create_report(employers))
            for row in report:
                print(row)
        elif choice == 3:
            report = create_report(employers)
            csv_dict_writer(report, csv_report_path)
        else:
            exit()
