import pandas as pd


class TextLoader:
    def __init__(self, name):
        self.name = name

    def load_txt(self, path):
        my_file = open(path, "r")
        content = my_file.read()
        return content

    def load_csv(self, path):
        my_file = pd.read_csv(path)
        return my_file
