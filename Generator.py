from typing import List


class GeneratorClass:
    def __init__(self, name: str, new_attributes: List[str]):
        self.__name = name
        self.get_and_set = new_attributes
        self.constructor = new_attributes

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def get_and_set(self):
        return self.__get_and_set

    @get_and_set.setter
    def get_and_set(self, new_attributes: List[str]):
        self.__get_and_set = ''
        for i in new_attributes:
            self.__get_and_set += f'\t@property\n' \
                                  f'\tdef {i}(self):\n' \
                                  f'\t\treturn self.__{i}\n\n' \
                                  f'\t@{i}.setter\n' \
                                  f'\tdef {i}(self, new_{i}):\n' \
                                  f'\t\tself.__{i} = new_{i}\n\n'

    @property
    def constructor(self):
        return self.__constructor

    @constructor.setter
    def constructor(self, new_attributes: List[str]):
        self.__constructor = f"class {self.__name}:\n" \
                             "\tdef __init__(self, "
        self.__constructor += str(new_attributes).replace("'", "").replace("[", '').replace("]", '')
        self.__constructor += '):\n'
        for i in new_attributes:
            self.__constructor += f'\t\tself.{i} = {i}\n'

    def get_class_prop(self):
        return self.__constructor + self.__get_and_set

    def write_on_file(self):
        f = open(f'{self.__name}.py', 'w')
        f.write(self.get_class_prop())
        f.close()


def main():
    try:
        name = input("Qual o nome da sua classe? ").replace(" ", '')
        attributes = input('Insira o nome das propriedades separados por ",": \n').replace(" ", '').lower().split(',')
        # atributos da classe

        generator = GeneratorClass(name, attributes)
        generator.write_on_file()

        print("Seja Feliz!\n A sua class foi criada, basta arrastar para os seus arquivos e dar import")
        input("Pressione Enter para sair")
    except Exception as e:
        print(e)
        input()


if __name__ == "__main__":
    main()
