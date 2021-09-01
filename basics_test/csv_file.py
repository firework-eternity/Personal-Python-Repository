import csv
import os


def csv_read(csv_name):
    # csv_path = "../test_data/" + csv_name
    dir_path = os.path.dirname(__file__)
    csv_path = dir_path.replace("basics_test", "test_data/" + csv_name)
    re_table = []
    # file = open(csv_path)
    with open(csv_path) as file:    # 文件自动关闭
        table = csv.reader(file)
        initial_variable = True
        for row in table:
            if initial_variable:
                initial_variable = False
            else:
                re_table.append(row)
    return re_table
