# Напишите программу, которая рассчитывает сумму и произведение цифр положительного трёхзначного числа и выводит текст в следующем формате:
# Сумма цифр = <сумма цифр>
# Произведение цифр = <произведение цифр>

## решение

number = int(input())

digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10

digit_sum = digit1 + digit2 + digit3
digit_product = digit1 * digit2 * digit3

print("Сумма цифр =", digit_sum)
print("Произведение цифр =", digit_product)