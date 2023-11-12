#Exercise 4.2:
print("Exercise 4.2: ")
#Exercise 3.5:
print("\na) Exercise 3.5: ")
def drawMeasure(length):
    measure = ""
    for x in range(length + 1):
        measure += "...|"
    measure += "\n"
    for x in range(length + 1):
        measure += "  " + str(x)
        measure += " "
    print(measure)

print("This is our measure of 5: ")
print(drawMeasure(5))

print("\nb) Exercise 3.6: ")

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

print("This is our rectangle with given width = 5 and height = 7: ")
print(drawRectangle(7, 5))

#Exercise 4.3:
def factorial(n):
    iteraFactorial = 1
    if n == 0:
        iteraFactorial = 1
    for i in range(1, n+1):
        iteraFactorial *= i
    return iteraFactorial

print("\nExercise 4.3:")
print("This is the factorial of 7: ")
print(factorial(7))

#Exercise 4.4:
def fibonacci(n):
    if n < 0:
        print("Wrong value! Write number > 0: ")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        iteraFibonacci = [0, 1]
        for f in range(2, n + 1):
            iteraFibonacci.append(iteraFibonacci[f-1] + iteraFibonacci[f-2])
        return iteraFibonacci[-1]

print("\nExercise 4.4: ")
print("This is the Fibonacci function with n = 7: ")
print(fibonacci(7))

#Exercise 4.5:
def odwracanie1(L, left, right):
    if left >= right:
        return
    L[left], L[right] = L[right], L[left]
    odwracanie1(L, left + 1, right - 1)

def odwracanie2(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

#Exercise 4.6:
print("\nExercise 4.6: ")
def sum_seq(sequence):
    sumInSeq = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            sumInSeq += sum_seq(item)
        else:
            sumInSeq += item
    return sumInSeq

print("This is our sequence: ")
element1 = [1, (2, 3), [], 4, [5, (6, 7)], [(8, 9)]]
print(element1)
print("This is the sum of sequence: ")
print(sum_seq(element1))

#Exercise 4.7:
print("\nExercise 4.7: ")
def flatten(sequence):
    sumInFlatten = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            sumInFlatten.extend(flatten(item))
        else:
            sumInFlatten.append(item)
    return sumInFlatten

print("This is our sequence: ")
element2 = [1, (2, 3), [], 4, [5, (6, 7)], [(8, 9)]]
print(element2)
print("This is the flatten sequence: ")
print(flatten(element2))

