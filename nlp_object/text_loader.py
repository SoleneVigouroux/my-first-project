class TextLoader:
    def __init__(self, name):
        self.name = name

    def load(self, path):
        my_file = open(path, "r")
        content = my_file.read()
        return content
