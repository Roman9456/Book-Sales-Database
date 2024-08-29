# Book Sales Database

## English

### Description
This project is a part of a homework assignment for the "Python and Databases. ORM" lecture. The goal is to create an SQLAlchemy model for a book sales database that stores information about publishers (authors), their books, and sales records.

### Task 1: Create SQLAlchemy Models
Develop the SQLAlchemy models based on the provided schema. The models should include:
- Publisher (author)
- Book
- Sale

The models should have appropriate field types and relationship definitions.

### Task 2: Implement a Query for Targeted Publisher
Write a Python script that:
1. Connects to a database of your choice (e.g., PostgreSQL).
2. Imports the necessary data models.
3. Prompts the user for a publisher name or ID.
4. Retrieves and prints the following information for each book sold by the targeted publisher:
   - Book title
   - Store name where the book was purchased
   - Purchase price
   - Purchase date

Example output (if the user entered "Pushkin" as the publisher):

The Captain's Daughter | Bookvoed     | 600 | 09-11-2022
Ruslan and Ludmila     | Bookvoed     | 500 | 08-11-2022
The Captain's Daughter | Labyrinth    | 580 | 05-11-2022
Eugene Onegin         | Book House | 490 | 02-11-2022
The Captain's Daughter | Bookvoed     | 600 | 26-10-2022

### Task 3 (Optional)
Fill the database with test data. The test data can be obtained from the "fixtures" folder, where the data is stored in a JSON file.

A possible implementation: read the JSON file, create the corresponding model instances, and save them to the database.

### General Advice
- Store the database connection parameters (login, password, database name, etc.) in separate variables.
- Load the values from the OS environment, for example, using os.getenv().
- You can either manually fill the data or complete the optional Task 3.

## Russian

### Описание
Этот проект является частью домашнего задания к лекции "Python и БД. ORM". Цель - создать модель SQLAlchemy для базы данных продаж книг, которая хранит информацию об издателях (авторах), их книгах и записях о продажах.

### Задание 1: Создать модели SQLAlchemy
Разработать модели SQLAlchemy на основе предоставленной схемы. Модели должны включать:
- Издатель (автор)
- Книга
- Продажа

Модели должны иметь подходящие типы полей и определение связей.

### Задание 2: Реализовать запрос для целевого издателя
Напишите Python-скрипт, который:
1. Подключается к базе данных по вашему выбору (например, PostgreSQL).
2. Импортирует необходимые модели данных.
3. Запрашивает имя или идентификатор издателя у пользователя.
4. Получает и печатает следующую информацию для каждой проданной книги целевого издателя:
   - Название книги
   - Название магазина, где была куплена книга
   - Цена покупки
   - Дата покупки

Пример вывода (если пользователь ввёл "Пушкин" в качестве издателя):

Капитанская дочка | Буквоед     | 600 | 09-11-2022
Руслан и Людмила  | Буквоед     | 500 | 08-11-2022
Капитанская дочка | Лабиринт    | 580 | 05-11-2022
Евгений Онегин    | Книжный дом | 490 | 02-11-2022
Капитанская дочка | Буквоед     | 600 | 26-10-2022

### Задание 3 (необязательное)
Заполните базу данных тестовыми данными. Тестовые данные можно получить из папки "fixtures", где данные хранятся в файле JSON.

Возможная реализация: прочитать файл JSON, создать соответствующие экземпляры моделей и сохранить их в базу данных.

### Общие советы
- Храните параметры подключения к базе данных (логин, пароль, название базы данных и т.д.) в отдельных переменных.
- Загружайте значения из окружения ОС, например, с помощью os.getenv().

