class CompareTwoListsAvg:
    @staticmethod
    def compare_avg(data_1: list, data_2: list) -> str:
        avg_1 = sum(data_1) / len(data_1)
        avg_2 = sum(data_2) / len(data_2)
        if avg_1 > avg_2:
            return "Среднее значение первого списка больше среднего значения второго списка"
        elif avg_1 < avg_2:
            return "Среднее значение первого списка меньше среднего значения второго списка"
        else:
            return "Средние значения двух списков равны"
