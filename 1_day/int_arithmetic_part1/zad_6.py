# Напишите программу, которая считает стоимость трёх компьютеров, состоящих из монитора, системного блока, клавиатуры и мыши.

## решение

monitor_price = int(input())
system_unit_price = int(input())
keyboard_price = int(input())
mouse_price = int(input())

all_computer_total_price = (monitor_price + system_unit_price + keyboard_price + mouse_price) * 3

print(all_computer_total_price)