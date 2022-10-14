import pyperclip


class GeneratorClass:
    def __init__(self):
        self.__constructor = ""
        self.__get_and_set = ""

    @property
    def get_and_set(self):
        return self.__get_and_set

    @get_and_set.setter
    def get_and_set(self, new_attributes: list[str]):
        self.__get_and_set = ''
        for i in new_attributes:
            self.__get_and_set += f'\t@property\n' \
                                  f'\tdef {i}(self):\n' \
                                  f'\t\treturn self.__{i}\n\n' \
                                  f'\t@{i}.setter\n' \
                                  f'\tdef {i}(self,new_{i}):\n' \
                                  f'\t\tself.__{i} = new_{i}\n\n'

    @property
    def constructor(self):
        return self.__constructor

    @constructor.setter
    def constructor(self, new_attributes: list[str]):
        self.__constructor = "\tdef __init__(self,"
        self.__constructor += str(new_attributes).replace("'", "").replace("[", '').replace("]", '')
        self.__constructor += '):\n'

    def get_class_prop(self):
        return self.__constructor + self.__get_and_set


try:
    attributes = input('Insira o nome das propriedades separados por ",": \n').replace(" ", '').lower().split(',')
    # atributos da classe

    generator = GeneratorClass()
    generator.constructor = attributes
    generator.get_and_set = attributes
    pyperclip.copy(generator.get_class_prop())

    print("Seja Feliz!\n O seus atributos e setters estão no no seu CTRL + V")
    input("Pressione Enter para sair")
except Exception as e:
    print(e)
    input()
