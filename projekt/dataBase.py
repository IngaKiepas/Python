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
def insertMovie(title, director, genre, year):
    connection = sqlite3.connect('media.db')
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO movies (title, director, genre, year)
        VALUES (?, ?, ?, ?)
    ''', (title, director, genre, year))

    connection.commit()
    connection.close()

def insertBook(title, author, genre, year):
    connection = sqlite3.connect('media.db')
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO books (title, author, genre, year)
        VALUES (?, ?, ?, ?)
    ''', (title, author, genre, year))

    connection.commit()
    connection.close()

def insertRecord(title, artist, genre, year):
    connection = sqlite3.connect('media.db')
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO  records (title, artist, genre, year)
        VALUES (?, ?, ?, ?)
    ''', (title, artist, genre, year))

    connection.commit()
    connection.close()

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

# zapisanie danych do pliku tekstowego
def saveTxt(data, fileName):
    with open(fileName, 'w') as file:
        for record in data:
            file.write(str(record) + '\n')

# zapisanie danych do pliku w formacie JSON
def saveJson(data, fileName):
    with open(fileName, 'w') as file:
        json.dump(data, file, indent=4)

# zapisanie danych do pliku w formacie CSV
def saveCsv(data, fileName, headers=None):
    with open(fileName, 'a', newline='') as file:
        csvWriter = csv.writer(file)

        if os.stat(fileName).st_size == 0 and headers:
            csvWriter.writerow(headers)

        for record in data:
            csvWriter.writerow(record)
