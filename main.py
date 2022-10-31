"""
Zadanie: kalkulator
Czas na duże, poważne zadanie! Dojrzewasz jako programista, więc mamy coś odpowiedniego – stworzymy własny kalkulator,
oczywiście nieco uproszczony. Załóżmy, że będzie przyjmował zawsze dwie liczby do obliczeń.

Docelowo chcielibyśmy uzyskać taki efekt:

Po uruchomieniu programu jesteśmy pytani o typ obliczenia

>> Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:
Następnie pobieramy dwie wartości liczbowe.

Korzystając z biblioteki logging, informujemy użytkownika, jakie działanie wykonamy i jakie będą jego argumenty (np. Dodaję 1 i 3).

Następnie wykonujemy obliczenie i drukujemy rezultat z print.

Do pobierania wartości użyj input. Nie ma potrzeby sprawdzania, czy podane argumenty są liczbami, przewidujemy poprawne uzupełnienie.

Przykładowe wywołanie razem z wartościami wybranymi przez użytkownika może wyglądać tak:

>> Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: 1
Podaj składnik 1. 2.3
Podaj składnik 2. 5.4
Dodaję 2.30 i 5.40
Wynik to 7.70
Dla chętnych
Jeśli chcesz usprawnić swoje zadanie, możesz dodać dwa rozszerzenia:

Sprawdzaj, czy podana wartość na pewno jest liczbą.
W wypadku mnożenia i dodawania daj użytkownikowi możliwość wpisania większej ilości argumentów niż tylko dwa, np. możesz dodać do siebie trzy i więcej liczb.
Prześlij link do zdalnego repozytorium z zadaniem Mentorowi. Sprawisz mu frajdę!
"""

x = input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ')

def is_int(x):
    """
    Checks if number taken from input is integer (Input is string type).

    :param x: number to be checked
    :return: True / False
    """
    digit = bool
    for sign in x:
        if sign.isdigit() == False:
            return False
        if sign.isdigit():
            digit = True
    return digit

def is_float(x):
    """
    Checks if number taken from input is a float (Input is string type).

    :param x: number to be checked
    :return: True / False
    """
    digit = bool
    i = 0
    dot = False
    for sign in x:
        if sign == '-' and i == 0:
            i += 1
            continue
        elif sign == '.' and dot == False:
            dot = True
            continue
        elif sign.isdigit():
            digit = True
        else:
            digit = False
            return digit
    return digit

def is_1to(x, y):
    """
    Checks if number taken from input is within range (1 to y+1).

    :param x: number which will be checked
    :param y: end of range
    :return: True / False
    """
    expected = range(1, y+1)
    return x in expected

def calculate():
    '''
    Calculation function. It doesn't take any arguments.
    Arguments are received through input method.
    It outputs a value of one of 4 different operations: addition, subtraction, multiplication, division.
    You can choose how many numbers will be involved in equasion.

    :return: value of mathematical operation in dedicated text formula
    '''
    q = []
    result = float()

    if x == '1':
        y = input('Ile liczb chciałbyś dodać? (min.2 liczby): ')
        while is_int(y) != True:
            y = input('Podaj cyfrę - int (min. 2): ')
        while is_int(y) == True:
            if int(y) > 1:
                break
            y = input('Podaj cyfrę - int (min. 2): ')
        i = 0
        while i < int(y):
            z = input('Podaj liczbę {0}: '.format(i+1))
            while is_float(z) != True:
                z = input('Podaj liczbę - float / int: ')
            q.append(float(z))
            i += 1

        for number in q:
            result += number

        text = str()
        if len(q) > 2:
            for n in q[2:]:
                text += " i " + str(n)

        return print(f'Dodawanie do liczby: {q[0]}, liczb: {q[1]}{text}\n'
                     f'Wynik Twojego działania to: {result}')

    elif x == '2':
        y = input('Ile liczb chciałbyś odjąć? (min.2 liczby): ')
        while is_int(y) != True:
            y = input('Podaj cyfrę - int (min. 2): ')
        while is_int(y) == True:
            if int(y) > 1:
                break
            y = input('Podaj cyfrę - int (min. 2): ')
        i = 0
        while i < int(y):
            z = input('Podaj liczbę {0}: '.format(i+1))
            while is_float(z) != True:
                z = input('Podaj liczbę - float / int: ')
            q.append(float(z))
            i += 1

        result = q[0]
        for number in q[1:len(q)]:
            result -= number

        text = str()
        if len(q) > 2:
            for n in q[2:]:
                text += " i " + str(n)

        return print(f'Odejmowanie od liczby: {q[0]}, liczb: {q[1]}{text}\n'
                     f'Wynik Twojego działania to: {result}')
    elif x == '3':
        y = input('Ile liczb chciałbyś mnożyć? (min. 2 liczby): ')
        while is_int(y) != True:
            y = input('Podaj cyfrę - int (min. 2): ')
        while is_int(y) == True:
            if int(y) > 1:
                break
            y = input('Podaj cyfrę - int (min. 2): ')
        i = 0
        while i < int(y):
            z = input('Podaj liczbę {0}: '.format(i+1))
            while is_float(z) != True:
                z = input('Podaj liczbę - float / int: ')
            q.append(float(z))
            i += 1

        result = q[0]
        for number in q[1:len(q)]:
            result *= number

        text = str()
        if len(q) > 2:
            for n in q[2:]:
                text += " i " + str(n)

        return print(f'Mnożenie liczby: {q[0]} przez: {q[1]}{text}\n'
                     f'Wynik Twojego działania to: {result}')
    else:
        y = input('Ile liczb chciałbyś dzielić? (min. 2 liczby): ')
        while is_int(y) != True:
            y = input('Podaj cyfrę - int (min. 2): ')
        while is_int(y) == True:
            if int(y) > 1:
                break
            y = input('Podaj cyfrę - int (min. 2): ')
        i = 0
        while i < int(y):
            z = input('Podaj liczbę {0}: '.format(i+1))
            while is_float(z) != True:
                z = input('Podaj liczbę - float / int: ')
            q.append(float(z))
            i += 1
        j = 1
        for number in q[1:]:
            if number == 0:
                z = input(f'Liczba {j+1} musi być różna od 0!: ')
                while float(z) == 0:
                    z = input(f'Liczba {j+1} musi być różna od 0!: ')
                q[j] = float(z)
            j += 1

        result = q[0]
        for number in q[1:len(q)]:
            result /= number

        text = str()
        if len(q) > 2:
            for n in q[2:]:
                text += " i " + str(n)

        return print(f'Dzielenie liczby: {q[0]} przez: {q[1]}{text}\n'
                     f'Wynik Twojego działania to: {result}')


while is_int(x) != True or is_1to(int(x), 5) != True:
    x = input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ')


calculate()


