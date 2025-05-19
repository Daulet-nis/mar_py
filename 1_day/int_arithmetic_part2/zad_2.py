# Напишите программу, которая находит полное число метров по заданному числу сантиметров.

## решение

length = int(input())

length_in_meters = length // 100
print(length_in_meters)