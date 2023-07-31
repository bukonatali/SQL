# book_id   INT PRIMARY KEY AUTO_INCREMENT
# title     VARCHAR(50)
# author    VARCHAR(30)
# price     DECIMAL(8, 2)
# amount    INT

import sqlite3

conn = sqlite3.connect('book.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY AUTOINCREMENT, 
col_1 TEXT,col_2 TEXT, col_3 text, col_4  INTEGER) ''')
cursor.execute('''INSERT INTO Book (title, author, price, amount) 
VALUES ('VARCHAR(50)', 'VARCHAR(30)', 'DECIMAL(8, 2)', 500 )''')
conn.commit()

cursor.execute('''SELECT*FROM Book''')
k = cursor.fetchall()
print(k)
for i in k:
    i = list(i)
    h = 0
    print(' '.join(str(h) for h in i))