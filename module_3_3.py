# Домашнее задание по уроку "Распаковка позиционных параметров"

def print_params(a = 2, b = 25, c = [1,2,3]):
    print(a, b, c)

values_list = [1, 'two', True]
values_dict = {'a': 3, 'b':'five', 'c': False}
values_list_2 = ['four', 8]

print(print_params())
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, [- 1])

