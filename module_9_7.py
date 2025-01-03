def is_prime(func):
    def wrapper(a, b, c):
        count = 0
        func_res = func(a, b, c)
        for i in range(2, func_res // 2):
            if func_res % i == 0:
                count += 1
        if count != 0: print("Составное")
        else: print("Простое")
        return func_res
    return wrapper


@is_prime
def sum_three(a, b, c):
    res = a + b + c
    return res


result = sum_three(0, 0, 18)
print(result)