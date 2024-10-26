def print_params(a = 1, b  = "строка", c = True):
    print(a, b, c)
#1
print_params()
print_params(1, 2, 3)
print_params(b = 25)
print_params(c  = [1, 2, 3])
#2
value_list = [False, 23, "String"]
value_dict = {"a": 23, "b": True, "c": "Line"}
print_params(*value_list)
print_params(**value_dict)
#3
values_list_2 = [2, "abc"]
print_params(*values_list_2, 42)
