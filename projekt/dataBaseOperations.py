from dataBase import *

createDatabase()

while True:

    choice = menu()

    if choice == "1":
        tableChoice = input("Choose the table (movies/books/records): ").lower()
        title = input("Enter the title: ")
        creator = input("Enter the creator: ")
        genre = input("Enter the genre: ")
        year = int(input("Enter the year: "))
        insertMedia(tableChoice, title, creator, genre, year)
        print("Element inserted!")

    elif choice == "2":
        tableChoice = input("Choose the table (movies/books/records): ").lower()
        mediaId = int(input("Give the element ID to delete: "))
        deleteMedia(tableChoice, mediaId)
        print("Element deleted!")

    elif choice == "3":
        tableChoice = input("Choose the table (movies/books/records): ").lower()
        searchTitle = input("Give the title to search: ")
        result = searchMedia(tableChoice, searchTitle)
        print("Searching results: ")
        for result in result:
            print(result)

    elif choice == "4":
        tableChoice = input("Choose the table (movies/books/records): ").lower()
        allMedia = listMedia(tableChoice)
        print(f"List of all elements ({tableChoice}): ")
        for media in allMedia:
            print(media)

    elif choice == "5":
        tableChoice = input("Choose the table (movies/books/records): ").lower()
        fileName = f'media{tableChoice}.json'

        # pętla dla wyboru tabeli
        if tableChoice == 'movies':
            data = listMedia('movies')
        elif tableChoice == 'books':
            data = listMedia('books')
        elif tableChoice == 'records':
            data = listMedia('records')
        else:
            print("Wrong table. Choose movies, books or records.")
            continue

        saveJson(data, fileName)
        print(f"Database saved to file {fileName}")

    elif choice == '0':
        confirmExit = input("Do you want to exit? (y/n): ")
        if confirmExit.lower() == 'y':
            print("Goodbye!")
            break
        else:
            print("Continue...")

    else:
        print("Wrong choice. Try again!")


