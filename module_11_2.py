from pprint import pprint
from time import sleep
import requests as rq
import pandas as pd
import numpy as np


# Библиотека requests
print("Библиотека requests:\n")

print("№1  Напишите программу, которая отправляет GET-запрос на сайт http://httpbin.org/get\nи выводит на экран статус-код ответа и содержимое ответа в формате JSON.\n")

response = rq.get("http://httpbin.org/get")
print(f"Статус кода: {response.status_code}")
print("Содержимое ответа:")
pprint(response.json())

print()
sleep(1.5)

print("№2 Напишите программу, которая отправляет POST-запрос на сайт http://httpbin.org/post с данными формы,\nсодержащими имя и возраст (например, {name: Ivan, age: 30}), и выводит на экран статус-код ответа и содержимое ответа в формате JSON.\n")

data_bin = {
    "name": "Ivan",
    "age": 30
}

response = rq.post("http://httpbin.org/post", json=data_bin)
print(f"Статус кода: {response.status_code}")
print("Содержимое ответа:")
pprint(response.json())

print()
sleep(1.5)

print("№3 Создайте программу, которая выполняет следующее:\nОтправляет GET-запрос на сайт https://jsonplaceholder.typicode.com/posts для получения списка постов.\nИзвлекает заголовки всех постов и сохраняет их в текстовый файл post_titles.txt.\nОбрабатывает возможные ошибки, такие как тайм-аут или недоступность сервера, и выводит соответствующее сообщение.\n")

try:
    response = rq.get("https://jsonplaceholder.typicode.com/posts")
    response.raise_for_status()
    response_titles = [title["title"] for title in response.json()]

    with open("response_titles.txt", "w", encoding='utf-8') as file:
        for line in response_titles:
            file.write(f"{line}\n")

except rq.exceptions.Timeout:
    print("Запрос превысил время ожидания.")
except rq.exceptions.RequestException as e:
    print("Произошла ошибка при выполнении запроса:", e)
print("Задание выполнено!")

print()
print()
sleep(1.5)

# Библиотека pandas
print("Библиотека pandas:\n")

print("№1 Создайте DataFrame из словаря, содержащего данные о студентах (имя, возраст и оценка).\nЗатем выведите на экран весь DataFrame и среднюю оценку студентов.\n")

data = {
    'Имя': ['Алексей', 'Мария', 'Иван', 'Екатерина'],
    'Возраст': [20, 21, 19, 22],
    'Оценка': [85, 90, 78, 95]
}

daraframe = pd.DataFrame(data)
average = daraframe["Оценка"].mean()

print(daraframe)
print(f"Средняя оценка студентов: {average}")

print()
sleep(1.5)

print("№2 Загрузите CSV-файл с информацией о продажах (например, sales_data.csv). Затем выполните следующие действия:\nВыведите на экран первые 5 строк DataFrame.\nНайдите и выведите общую сумму продаж по всем записям.\n")

dataframe = pd.read_csv("sales_data.csv")

print(dataframe.head(5))
print(f"Общая сумма продаж по всем записям: {sum(dataframe["Price"])}")

print()
sleep(1.5)

print("№3 Создайте DataFrame с данными о товарах (название, категория, цена, количество). Затем выполните следующие действия:\nДобавьте новый столбец Стоимость (цена * количество).\nОтфильтруйте товары, стоимость которых превышает 1000, и выведите отфильтрованный DataFrame.\nСохраните отфильтрованный DataFrame в новый CSV-файл expensive_products.csv.\n")
print()
dataframe = pd.read_csv("sales_data.csv")
dataframe["Cost"] = dataframe["Quantity"] * dataframe["Price"]
dataframe_2 = dataframe[dataframe["Cost"] > 1700]
dataframe_2.to_csv("expensive_products.csv", index=False)
print("Задание выполнено!")

print()
print()
sleep(1.5)


# Библиотека numpy
print("Библиотека numpy:\n")

print("№1 Создайте одномерный массив numpy из списка целых чисел (например, от 1 до 10).\nЗатем выведите на экран сам массив и его размер (количество элементов).\n")

arr = np.array([i for i in range(10)])
print(f"Массив: {arr}")
print(f"Размер массива: {arr.size} элементов")

print()
sleep(1.5)

print("№2  Создайте двумерный массив numpy размером 3x3, заполненный случайными числами от 0 до 1.\nЗатем найдите и выведите сумму всех элементов массива и максимальный элемент.\n")

arr = np.random.rand(3, 3)
print(f"Двумерный массив размером 3x3:\n{arr}")
print()
print(f"Сумма всех элементов: {arr.sum()}\nМаксимальный элемент: {arr.max()}")

print()
sleep(1.5)

print("№3  Создайте двумерный массив numpy размером 4x4, заполненный числами от 1 до 16. Затем выполните следующие действия:\nТранспонируйте массив.\nВычислите определитель матрицы.\nНайдите собственные значения матрицы.\n")

arr =  np.arange(1, 17).reshape(4, 4)
print(f"Двумерный массив размером 4x4, заполненный числами от 1 до 16:\n{arr}")
print(f"Транспонированный массив:\n{arr.T}")
print(f"Определитель матрицы: {np.linalg.det(arr)}")
np.set_printoptions(suppress=True)
print(f"Cобственные значения матрицы:\n{np.linalg.eigvals(arr)}")