import sqlite3
import pandas as pd
import time

# Створюємо великий DataFrame для тесту
data = {
    'id': range(1, 1000001),
    'name': ['Name_' + str(i) for i in range(1, 1000001)],
    'value': [i % 100 for i in range(1, 1000001)],
    'category': ['Category_' + str(i % 10) for i in range(1, 1000001)]
}
df = pd.DataFrame(data)

# Підключаємося до SQLite
conn = sqlite3.connect('example.db')

# Записуємо DataFrame у SQL таблицю
start = time.time()
df.to_sql('my_table', conn, if_exists='replace', index=False)
print(f"Data written in {time.time() - start:.2f} seconds")

# Додаємо індекси для оптимізації запитів
conn.execute('CREATE INDEX IF NOT EXISTS idx_id ON my_table (id);')
conn.execute('CREATE INDEX IF NOT EXISTS idx_category ON my_table (category);')
conn.commit()

print("Indexes created successfully.")

# Оптимізоване читання
start = time.time()
query = "SELECT * FROM my_table WHERE category = 'Category_5' AND value > 50;"
result = pd.read_sql_query(query, conn)
print(f"Query executed in {time.time() - start:.2f} seconds")

# Закриваємо підключення
conn.close()
