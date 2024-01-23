from dataBase import *

createDatabase()

while True:
    print("\nChoose the option: ")
    print("1. Add the new film")
    print("2. Add the new book")
    print("3. Add the new record")
    print("4. Delete the element")
    print("5. Search the element.")
    print("6. List all elements")
    print("7. Save the database")
    print("0. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        title = input("Title: ")
        director = input("Director: ")
        genre = input("Genre: ")
        publicationYear = int(input("PublicationYear: "))
        insertMovie(title, director, genre, publicationYear)
        print("New film added!")

    elif choice == "2":
        title = input("Title: ")
        author = input("Author: ")
        genre = input("Genre: ")
        publicationYear = int(input("PublicationYear: "))
        insertBook(title, author, genre, publicationYear)
        print("New book added!")

    elif choice == "3":
        title = input("Title: ")
        artist = input("Artist: ")
        genre = input("Genre: ")
        publicationYear = int(input("PublicationYear: "))
        insertRecord(title, artist, genre, publicationYear)
        print("New record added!")

    elif choice == "4":
        tableChoice = input("Choose the table (movies/books/records): ").lower()
        mediaId = int(input("Give the element ID to delete: "))
        deleteMedia(tableChoice, mediaId)
        print("Element deleted!")

    elif choice == "5":
        tableChoice = input("Choose the table (movies/books/records): ").lower()
        searchTitle = input("Give the title to search: ")
        result = searchMedia(tableChoice, searchTitle)
        print("Searching results: ")
        for result in result:
            print(result)

    elif choice == "6":
        tableChoice = input("Choose the table (movies/books/records): ").lower()
        allMedia = listMedia(tableChoice)
        print(f"List of all elements ({tableChoice}): ")
        for media in allMedia:
            print(media)

    elif choice == "7":
        tableChoice = input("Choose the table (movies/books/records): ").lower()
        saveChoice = input("Choose the saving format (TXT/CSV/JSON): ").lower()
        fileName = f'media{tableChoice}.{saveChoice}'

        if tableChoice == 'movies':
            data = listMedia('movies')
        elif tableChoice == 'books':
            data = listMedia('books')
        elif tableChoice == 'records':
            data = listMedia('records')
        else:
            print("Wrong table. Choose movies, books or records.")
            continue

        if saveChoice == 'txt':
            saveTxt(data, fileName)
            print(f"Database saved to file {fileName}")
        elif saveChoice == 'csv':
            headers = ["ID", "Title", "Author", "Genre", "Year"]
            saveCsv(data, fileName, headers=headers)
            print(f"Database saved to file {fileName}")
        elif saveChoice == 'json':
            saveJson(data, fileName)
            print(f"Database saved to file {fileName}")
        else:
            print("Wrong saving format. Choose txt, csv or json.")

    elif choice == '0':
        confirmExit = input("Do you want to exit? (y/n): ")
        if confirmExit.lower() == 'y':
            print("Goodbye!")
            break
        else:
            print("Continue...")

    else:
        print("Wrong choice. Try again!")

    #pytanie o kontynuacje
    continueChoice = input("Do you want to continue? (y/n): ")
    if continueChoice != 'y':
        break

