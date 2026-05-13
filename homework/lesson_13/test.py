import sqlite3

connection = sqlite3.connect('kurs.db')

cursor = connection.cursor()

# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS miasta (id INTEGER PRIMARY KEY, nazwa NOT NULL, populacja INTEGER); 
#               """)

# cursor.execute("""
#                 INSERT INTO miasta (nazwa, populacja) VALUES (?, ?)
#                """,
#                ("Warszawa", 2000000)
#                )

# cities_to_add = [
#     ('Płock', 12000),
#     ('Hajnówka', 10000),
#     ('Londyn', 100000000)
# ]

# cursor.executemany("""
#                 INSERT INTO miasta (nazwa, populacja) VALUES (?,?)
#                    """,
#                    cities_to_add)

# cursor.execute("SELECT * FROM miasta;")

# all_cities = cursor.fetchall()

# print(all_cities)

# cursor.execute("SELECT * FROM miasta WHERE populacja > 100000;")

# cities_over_100k = cursor.fetchall()

# print(cities_over_100k)

cursor.execute("""
                UPDATE miasta SET populacja = ? WHERE nazwa = ?
                """,
                (99999, "Płock"))

connection.commit()

print(f"Zmieniono {cursor.rowcount} rekordów")

cursor.execute("""
            SELECT * FROM miasta WHERE nazwa= 'Płock';
               """)

print(f"Zmieniony rekord {cursor.fetchone()}")

connection.close()