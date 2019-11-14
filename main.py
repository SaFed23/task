string = input("Введите строку из 0 и 1: ")
with open("./data.txt", "r") as file:
    arr = file.readline().split(",")
print("Начальный массив: ", arr)
result_arr = list(filter(lambda element: string[arr.index(element)] == "1", arr))
print("Результат:", result_arr)
