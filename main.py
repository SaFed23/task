string = input("Введите строку из 0 и 1: ")
arr = []
for char in string:
    arr.append(input("Введите элемент: "))
result_arr = list(filter(lambda element: string[arr.index(element)] == "1", arr))
print("Результат:", result_arr)
