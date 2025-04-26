def Task():
    input_array = input("Введите числа через пробел: ")
    numbers = list(map(int, input_array.split()))

    positive_sum = sum(num for num in numbers if num > 0)

    max_value = max(numbers)
    min_value = min(numbers)
    max_index = numbers.index(max_value)
    min_index = numbers.index(min_value)

    if max_index < min_index:
        start_index = max_index +1
        end_index = min_index
    else:
        start_index = min_index +1
        end_index = max_index

    figure = 1
    for i in range(start_index, end_index):
        figure *= numbers[i]

    return positive_sum, figure

sum_positive, product_between = Task()
print(f"Сумма положительных элементов: {sum_positive}")
print(f"Произведение элементов между минимальным и максимальным: {product_between}")