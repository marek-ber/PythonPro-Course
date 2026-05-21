import sqlite3

DATABASE_NAME = "todo_raw.db"


def init_db():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS zadania (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            opis TEXT NOT NULL,
            zrobione BOOLEAN NOT NULL CHECK (zrobione IN (0, 1)),
            priorytet INTEGER DEFAULT 1
        )
        """)
        conn.commit()


def dodaj_zadanie(opis: str, priorytet: int = 1):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO zadania (opis, zrobione, priorytet) VALUES (?, ?, ?)",
            (opis, False, priorytet)
        )
        conn.commit()


def pobierz_zadania():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, opis, zrobione, priorytet FROM zadania")
        return cursor.fetchall()


def oznacz_jako_zrobione(id_zadania: int):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE zadania SET zrobione = ? WHERE id = ?",
            (True, id_zadania)
        )
        conn.commit()


def usun_zadanie(id_zadania: int):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM zadania WHERE id = ?", (id_zadania,))
        conn.commit()


def wyszukaj_zadania(fraza: str):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, opis, zrobione, priorytet FROM zadania WHERE opis LIKE ?",
            (f"%{fraza}%",)
        )
        return cursor.fetchall()


def edytuj_zadanie(id_zadania: int, nowy_opis: str):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE zadania SET opis = ? WHERE id = ?",
            (nowy_opis, id_zadania)
        )
        conn.commit()