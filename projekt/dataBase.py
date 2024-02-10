import os
import sqlite3
import json
import csv

# tworzenie bazy danych, nawiązywanie połączenia z bazą o nazwie media.db
def createDatabase():
    connection = sqlite3.connect('media.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                title TEXT,
                director TEXT,
                genre TEXT,
                year INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            genre TEXT,
            year INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            artist TEXT,
            genre TEXT,
            year INTEGER
        )
    ''')

    connection.commit()
    connection.close()

# dodawanie elementów do tabel w dynamiczny sposób
def insertMedia(tableName, title, creator, genre, year):
    conn = sqlite3.connect('media.db')
    cursor = conn.cursor()

    try:
        if tableName == 'movies':
            cursor.execute("INSERT INTO movies (title, director, genre, year) VALUES (?, ?, ?, ?)",
                           (title, creator, genre, year))
        elif tableName == 'books':
            cursor.execute("INSERT INTO books (title, author, genre, year) VALUES (?, ?, ?, ?)",
                           (title, creator, genre, year))
        elif tableName == 'records':
            cursor.execute("INSERT INTO records (title, artist, genre, year) VALUES (?, ?, ?, ?)",
                           (title, creator, genre, year))
        else:
            print("Wrong table name! You can choose: movies, books or records!")

        conn.commit()
        print("Element added!", tableName)
    except sqlite3.Error as e:
        print("Error during adding the element!", e)
    finally:
        conn.close()


#usuwanie elementów z określonej bazy danych
def deleteMedia(tableName, mediaId):
    connection = sqlite3.connect('media.db')
    cursor = connection.cursor()

    cursor.execute(f'DELETE FROM {tableName} WHERE id = ?',
        (mediaId,))

    connection.commit()
    connection.close()

#szukanie elementów w określonej tabeli
def searchMedia(tableName, title):
    connection = sqlite3.connect('media.db')
    cursor = connection.cursor()

    cursor.execute(f'SELECT * FROM {tableName} WHERE title LIKE ?',
                   ('%' + title + '%',))

    result = cursor.fetchall()
    connection.close()
    return result

#pobieranie wszystkich elementów z określonej bazy danych
def listMedia(tableName):
    connection = sqlite3.connect('media.db')
    cursor = connection.cursor()

    cursor.execute(f'SELECT * FROM {tableName}')

    result = cursor.fetchall()
    connection.close()
    return result

# zapisanie danych do pliku w formacie JSON
def saveJson(data, fileName):
    with open(fileName, 'w') as file:
        json.dump(data, file, indent=4)

# menu z listą opcji
def menu():
    print("\nChoose the option: ")
    print("1. Add the new element")
    print("2. Delete the element")
    print("3. Search the element.")
    print("4. List all elements")
    print("5. Save the database")
    print("0. Exit")
    return input("\nEnter your choice: ")

