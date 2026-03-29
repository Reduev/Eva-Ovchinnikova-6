def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, (int, float)):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)
if __name__ == "__main__":

    assert average_num([1, 1]) == 1, "Тест 1 не пройден" # список из двух одинаковых целых чисел

    assert average_num([2.5, 3.5]) == 3, "Тест 2 не пройден" # список из двух чисел с плавающей точкой

    assert average_num([1, 2, 3]) == 2, "Тест 3 не пройден" # список из трёх целых чисел

    assert average_num([40, 44]) == 42, "Тест 4 не пройден" # если среднее из двух чисел = 42

    assert average_num([-1, -2, 3]) == 0, "Тест 5 не пройден" # список с отрицательными числами

    assert average_num([1, 2.5, 3]) == 2.17, "Тест 6 не пройден" # список со смешанными типами (целые и float)

    assert average_num(['a', 1, 2]) == "Bad request", "Тест 7 не пройден" # список с нечисловым значением (строка)

    assert average_num([0, 0, 0]) == 0, "Тест 8 не пройден" # список с нулевым значением

    assert average_num([1.5, 2.5, 3.0]) == 2.33, "Тест 9 не пройден" # список с дробными числами, дающими целое среднее
    
    assert average_num([100, 200, 300]) == 200, "Тест 10 не пройден" # список с большими числами

    print("Все тесты пройдены!")