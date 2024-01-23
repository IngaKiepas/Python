Tematem projektu jest baza książek, płyt i filmów. 
Znajdują się w niej 3 tabele, w każdej jest jeden ze wspomnianych wyżej typów.
Baza jest zapisywana do pliku txt, CSV oraz JSON.
Operacjami, które można wykonać na bazie są: wstawianie, usuwanie, wyszukiwanie, listowanie.
Do wykonania programu została użyta biblioteka SQLite

1. Opis algorytmu:
a) Tworzenie bazy danych:
Funkcja createDatabase() tworzy bazę danych o nazwie 'media.db' oraz trzy tabele:
- 'movies', 
- 'books'
- 'records'. 
Każda tabela ma kolumny id, title, director lub author, genre i year.
b) Wstawianie elementów:
Funkcje insertMovie(title, director, genre, year), insertBook(title, author, genre, year)
i insertRecord(title, artist, genre, year) służą do dodawania nowych rekordów do odpowiednich tabel w bazie danych.
c) Usuwanie elementów:
Funkcja deleteMedia(tableName, mediaId) pozwala na usunięcie elementu z wybranej tabeli na podstawie podanego identyfikatora (id).
d) Wyszukiwanie elementów:
Funkcja searchMedia(tableName, title) umożliwia wyszukiwanie elementów w wybranej tabeli na podstawie podanego tytułu.
e) Listowanie elementów:
Funkcja listMedia(tableName) zwraca listę wszystkich elementów w wybranej tabeli.
f) Zapisywanie danych do plików:
- funkcja saveTxt(data, fileName) zapisuje dane do pliku tekstowego (TXT) w formacie czytelnym dla człowieka
- funkcja saveJson(data, fileName) zapisuje dane do pliku JSON w formie sformatowanej
- funkcja saveCsv(data, fileName, header=None) zapisuje dane w formie tabelarycznej, gdzie pierwszy wiersz zawiera nagłówki.

2. Opis interfejsu:
Program rozpoczyna się od wyświetlenia menu głównego, gdzie użytkownik może wybrać różne opcje związane z zarządzaniem 
bazą danych.
a) Dodawanie nowych elementów:
Użytkownik może dodać nowy film, książkę lub płytę, podając odpowiednie informacje, takie jak tytuł, reżysera, autora, 
gatunek i rok wydania.
b) Usuwanie elementów:
Użytkownik może wybrać opcję usunięcia elementu, podając identyfikator (id) oraz wybierając tabelę (movies/books/records).
c) Wyszukiwanie elementów:
Użytkownik może wyszukać element w wybranej tabeli, podając tytuł.
d) Listowanie elementów:
Użytkownik ma możliwość wylistowania wszystkich elementów w wybranej tabeli.
e) Zapisywanie bazy danych do pliku:
Użytkownik może wybrać opcję zapisu bazy danych do pliku tekstowego (TXT), pliku JSON lub pliku CSV. Wybiera również, 
który format pliku chce użyć.
f) Wyjście z programu:
Użytkownik może zakończyć program, wpisując "0" i potwierdzając chęć wyjścia.
g) Potwierdzenie kontynuacji:
Po wykonaniu danej operacji program pyta użytkownika, czy chce kontynuować. Użytkownik może odpowiedzieć "y" lub "n" 
w zależności od swojej decyzji.

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
- Obsługa różnych formatów zapisu:
Implementacja umożliwia zapis bazy danych do plików w formatach TXT, JSON i CSV.
- Potwierdzenie kontynuacji:
Dodane potwierdzenie przed zakończeniem programu, może pomóc w uniknięciu przypadkowego wyjścia z programu.

5. Podsumowanie
Projekt to prosty system zarządzania informacjami o filmach, kiążkach i płytach. Skupia się na interakcji z użytkownikiem
poprzez tekstowe menu, pozwalając na dodawanie, usuwanie, wyszukiwanie, listowanie i zapisywanie danych w różnych formatach.

6. Uruchomienie: 
Aby uruchomić program należy wpisać: python dataBaseOperations.py
