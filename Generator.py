import pyperclip

try:
    attributes =  input('Insira o nome das propriedades separados por ",": \n').replace(" ",'').lower().split(',')
    # atributos da classe

    getters_and_setters = ""

    init = "\tdef __init__(self,"

    init += str(attributes).replace("'", "").replace("[", '').replace("]", '')

    init += '):\n'
    for i in attributes:
        init += f'\t\tself.__{i} = {i}\n'
        getters_and_setters += f'\t@property\n' \
                               f'\tdef {i}(self):\n' \
                               f'\t\treturn self.__{i}\n\n' \
                               f'\t@{i}.setter\n' \
                               f'\tdef {i}(self,new_{i}):\n' \
                               f'\t\tself.__{i} = new_{i}\n\n'

    pyperclip.copy(init+getters_and_setters)

    print("Seja Feliz!\n O seus atributos e setters estão no no seu CTRL + V")
    input("Pressione Enter para sair")
except Exception as e:
    print(e)
    input()
