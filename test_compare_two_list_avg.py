"""
Модуль для тестирования метода compare_avg класса CompareTwoListsAvg
"""


from compare_two_list_avg import CompareTwoListsAvg


def test_compare_avg():
    """
    Функция для тестирования метода compare_avg
    :return:
    """
    assert (CompareTwoListsAvg.compare_avg([1, 2, 3, 4, 5], [1, 2, 3])
            == "Среднее значение первого списка больше среднего значения второго списка")
    assert (CompareTwoListsAvg.compare_avg([1, 2, 3], [1, 2, 3, 4, 5])
            == "Среднее значение первого списка меньше среднего значения второго списка")
    assert (CompareTwoListsAvg.compare_avg([1, 2, 3], [1, 2, 3])
            == "Средние значения двух списков равны")
