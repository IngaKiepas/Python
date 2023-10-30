"""
Exercise 3.1:
Podany kod nie jest poprawny składniowo, ponieważ:
- w Pythonie nie używa się średników na koniec instrukcji:
powinno to więc wyglądać, np. tak:
x = 2; y = 3
if (x > y):
    result = x
else:
    result = y
- w pętli for, pętla if powinna być pod pętlą for, w innym bloku:
for i in "axby":
    if ord(i) < 100:
        print (i)
- w tej pętli for instrukcja print powinna być pod pętlą lub zawarta w nawiasach
for i in "axby":
    print(ord(i) if ord(i) < 100 else i)
"""
"""
Exercise 3.2:
W poniższym kodzie:
- L=L.sort() zwraca None, więc L=L.sort() nie ma sensu, powinno to wyglądać, np. tak:
L = [3, 5, 4]
L.sort()
- w linii poniżej występuje przypisanie trzech wartości do dwóch zmiennych, a to jest błędne:
x, y = 1, 2, 3
- w linii ponizej, aby zmienic zawartosc na indeksie 1 nalezy zrobic z X liste:
X = 1,2,3 X[1] = 4
- w linii poniżej wystepuje przypisanie wartosci do indeksu 3, ale lista ma tylko indeksy 0,1,2. 
Więc indeks 3 wykracza poza granice i jest to błąd.
X = [1, 2, 3] ; X[3] = 4
- poniżej błędem jest użycie funkcji append() dla stringów.
X = "abc" ; X.append("d")
- poniżej w funkcji pow nie ma zadnych argumentow:
L = list(map(pow, range(8)))
"""
# Exercise 3.3:
print("Exercise 3.3: ")
print("Here are numbers from 0 to 30, but without those that are divisible by 3: ")
for i in range(31): #Here I have all numbers that are not divisible by 3
    if (i % 3) != 0:
        print(i)

#Exercise 3.4:
print("\nExercise 3.4: ")
while True:
    number = input("Give me a number of the float type or 'stop' if you want to end:")
    if(number == 'stop'):
        print("You wrote stop, so this is the end of exercise!")
        break
    try:
        number = float(number)
        print("Your number is: ", number)
        cube = number ** 3
        print("This is the cube of your number: ", cube)
    except ValueError:
        print("Wrong value! Write down float number, not a string!")

#Exercise 3.5:
print("\nExercise 3.5: ")
def drawMeasure(length):
    measure = ""
    for x in range(length + 1):
        measure += "|..."
    measure += "\n"
    for x in range(length + 1):
        measure += str(x) + "  "
        measure += " "
    print(measure)

length = input("Give me the length of measure: ")
length = int(length)
print("This is our measure of given length: ", length)
drawMeasure(length)

#Exercise 3.6:
print("\nExercise 3.6: ")
def drawRectangle(height, width):
    rectangle = ""
    for h in range(height):
        rectangle += "+"
        for w in range(width):
            rectangle +="---+"
        rectangle +="\n"
        for w in range(width + 1):
            rectangle += "|   "
        rectangle += "\n"

    rectangle += "+"
    for w in range(width):
        rectangle += "---+"
    rectangle += "\n"

    print(rectangle)

height = input("Give me a height of our rectangle: ")
width = input("Give me a width of our rectangle: ")
height = int(height)
width = int(width)
print("This is our rectangle with given width and height: ", width, "x", height)

drawRectangle(height, width)
"""
Exercise 3.7:
Dla wykomentowania metody __str__:
program zwraca:
Time(12) Time(3456)
[Time(12), Time(3456)]
Dla wykomentowania metody __repr__:
program zwraca:
[<__main__.Time object at 0x1065ff050>, <__main__.Time object at 0x1065ff450>]
Na pewno można zauważyć, że przy wykomentowaniu metody __rep__ i zostawieniu metody __str__ mamy wynik
bardziej czytelny dla użytkownika 
"""

#Exercise 3.8:
print("\nExercise 3.8: ")
print("These are our number sequences: ")
sequence1 = [5, 7, 22, 21, 14]
sequence2 = [21, 22, 10, 9, 47]
print("Sequence 1: ", sequence1)
print("Sequence 2: ", sequence2)
S1 = set(sequence1)
S2 = set(sequence2)
sequencesSum = S1.union(S2)
sequencesIntersection = S1.intersection(S2)
print("Union of sequences: ", sequencesSum)
print("Intersection of sequences: ", sequencesIntersection)

#Exercise 3.9:
print("\nExercise 3.9: ")
sequenceList = ([5, 6, 2], [], [2], [9, 8], [2, 5, 8], [2, 2], [], [15], [6, 3, 1])
print("This is our sequence list: ", sequenceList)

sumList = [sum(i) for i in sequenceList]
print("This is a list with the sum of the numbers from the sequences: ", sumList)

#Exercise 3.10:
print("\nExercise 3.10: ")
print("Przykład zaprezentowany w kodzie bez wypisywania niczego na ekran!")
# 1 way to do this:
numbers = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

#2 way to do this:
numbers2 = {}
numbers2['I'] = 1
numbers2['V'] = 5
numbers2['X'] = 10
numbers2['L'] = 50
numbers2['C'] = 100
numbers2['D'] = 500
numbers2['M'] = 1000











