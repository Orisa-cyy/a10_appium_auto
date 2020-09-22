import os
import yaml


def analyze_file(filename, data_key):
    with open("." + os.sep + "data" + os.sep + filename, "r")as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        data_dict = data[data_key]
        data_list = []
        for i in data_dict.values():
            data_list.append(i)
        return data_list
