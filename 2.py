# Создать 2 таблицы в Базе Данных. Одна будет хранить текстовые данные(1 колонка)
# Другая числовые(1 колонка)
# Есть список, состоящий из чисел и слов.
# Если элемент списка слово, записать его в соответствующую таблицу,
# затем посчитать длину слова и записать её в числовую таблицу
# Если элемент списка число: проверить, если число чётное записать его в таблицу чисел,
# если нечётное, то записать во вторую таблицу слово: «нечётное»
# Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице.
# Если меньше, то обновить 1 запись в первой таблице на «hello»

import sqlite3

conn = sqlite3.connect("2.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS WORD(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT) ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS NUMBER(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER) ''')
conn.commit()
a = ['Natasha', 'hello', 2,1,2]

for i in a:
    if isinstance(i, str):
        cursor.execute('''INSERT INTO WORD(col_1) VALUES (?)''', (i,))
        cursor.execute(f'''INSERT INTO NUMBER(col_1) VALUES ('{len(i)}')''')
    elif i % 2:
        cursor.execute('''INSERT INTO WORD(col_1) VALUES ("нечетное")''')
else:
    cursor.execute('''INSERT INTO NUMBER(col_1) VALUES (?)''', (i,))
    conn.commit()
    cursor.execute('''SELECT col_1 FROM WORD''')
k = cursor.fetchall()
print(k)
cursor.execute('''SELECT col_1 FROM NUMBER''')
f = cursor.fetchall()
print(f)
print(len(f))
if len(f) > 5:
    cursor.execute('''DELETE FROM WORD WHERE id = 1''')
else:
    cursor.execute('''UPDATE WORD SET col_1 = 'hello' WHERE id = 1''')
cursor.execute('''SELECT col_1 FROM WORD''')
k = cursor.fetchall()
print(k)
cursor.execute('''SELECT col_1 FROM NUMBER''')
f = cursor.fetchall()
print(f)
