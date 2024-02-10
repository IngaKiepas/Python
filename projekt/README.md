Tematem projektu jest baza książek, płyt i filmów. Znajdują się w niej 3 tabele, w każdej jest jeden ze 
wspomnianych wyżej typów. Baza jest zapisywana do pliku JSON. Operacjami, które można wykonać na bazie są:
wstawianie, usuwanie, wyszukiwanie, listowanie. Do wykonania programu została użyta biblioteka SQLite.

1. Opis algorytmu:
- Tworzenie bazy danych: 
Funkcja createDatabase() tworzy bazę danych o nazwie 'media.db' oraz trzy tabele:
'movies','books','records'. 
Każda tabela ma kolumny id, title, director lub author, genre i year.
- Wstawianie elementów:
Funkcja insertMedia(tableName, title, creator, genre, year) służy do dodawania nowych rekordów do odpowiednich tabel 
w bazie danych.
- Usuwanie elementów:
Funkcja deleteMedia(tableName, mediaId) pozwala na usunięcie elementu z wybranej tabeli na podstawie podanego identyfikatora (id).
- Wyszukiwanie elementów:
Funkcja searchMedia(tableName, title) umożliwia wyszukiwanie elementów w wybranej tabeli na podstawie podanego tytułu.
- Listowanie elementów:
Funkcja listMedia(tableName) zwraca listę wszystkich elementów w wybranej tabeli.
- Zapisywanie danych do plików:
funkcja saveJson(data, fileName) zapisuje dane do pliku JSON w formie sformatowanej;

2. Opis interfejsu:
Program rozpoczyna się od wyświetlenia menu głównego, gdzie użytkownik może wybrać różne opcje związane z zarządzaniem 
bazą danych.
- Dodawanie nowych elementów:
Użytkownik może dodać nowy film, książkę lub płytę, podając odpowiednie informacje, takie jak tytuł, reżysera, autora, 
gatunek i rok wydania.
- Usuwanie elementów:
Użytkownik może wybrać opcję usunięcia elementu, podając identyfikator (id) oraz wybierając tabelę (movies/books/records).
- Wyszukiwanie elementów:
Użytkownik może wyszukać element w wybranej tabeli, podając tytuł.
- Listowanie elementów:
Użytkownik ma możliwość wylistowania wszystkich elementów w wybranej tabeli.
- Zapisywanie bazy danych do pliku:
Użytkownik może zapisać wybraną bazę danych do pliku JSON.
- Wyjście z programu:
Użytkownik może zakończyć program, wpisując "0" i potwierdzając chęć wyjścia.

Dodatkowo, funkcja menu() jest odpowiedzialna za wyświetlenie menu opcji w konsoli. Po wywołaniu tej funkcji, 
użytkownik może wybierać między różnymi operacjami dostępnymi w programie, wprowadzając odpowiedni numer. 
Funkcja ta zwraca wybór użytkownika, który jest przekazywany do dalszej części programu, 
gdzie wykonywane są odpowiednie operacje w zależności od wyboru.

3. Implementacja
- Modularność:
Implementacja została podzielona na dwa pliki: dataBase.py i dataBaseOperations.py. To podejście jest korzystne, 
gdyż oddziela logikę bazodanową od samego interfejsu użytkownika, co ułatwia utrzymanie i rozwijanie kodu.
- Baza danych:
Użyty został tutaj SQLite do obsługi baz danych.
Wprowadzanie, czy też usuwanie danych zostało zaimplementowane poprzez funkcje, co przyczynia się do czytelności kodu.
- Obsługa różnych typów mediów:
Kod uwzględnia trzy różne typy mediów (filmy, książki, płyty) poprzez trzy oddzielne tabele w bazie danych. 
To umożliwia zorganizowanie danych.
- Menu interakcyjne:
Menu interakcyjne dla użytkownika jest czytelne i łatwe do zrozumienia. Poszczególne opcje są jasno opisane, 
co ułatwia obsługę programu.
- Obsługa formatu zapisu:
Implementacja umożliwia zapis bazy danych do pliku w formacie JSON.
- Potwierdzenie kontynuacji:
Dodane potwierdzenie przed zakończeniem programu, może pomóc w uniknięciu przypadkowego wyjścia z programu.

4. Podsumowanie
Projekt to prosty system zarządzania informacjami o filmach, kiążkach i płytach. Skupia się na interakcji z użytkownikiem
poprzez tekstowe menu, pozwalając na dodawanie, usuwanie, wyszukiwanie, listowanie i zapisywanie danych w formacie JSON.

5. Uruchomienie: 
Aby uruchomić program należy wpisać: python dataBaseOperations.py
    