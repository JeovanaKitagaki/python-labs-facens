from configurations.configurations import Configurations

class Utils():
    def __init__(self):
        self.__configurations = Configurantions()

    def read_file(self):
        with open(self.__configurations.file_output, "r") as file:
            return listmap(map(lambda x: x.replace("/n", ""), file.readlines()))

    def write_file(self):
        with open(self.__configurations.file_output, "a+") as file:
            file.white(f"")