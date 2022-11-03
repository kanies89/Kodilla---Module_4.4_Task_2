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
import logging
logging.basicConfig(level=logging.DEBUG)

OPERATION_TYPE = {
    1: ["Dodawanie", "dodać", "dodawania", "Dodaję do {0} liczby {1}"],
    2: ["Odejmowanie", "odjąć", "odejmowania", "Odejmuję od {0} liczby {1}"],
    3: ["Mnozenie", "mnożyć", "mnożenia", "Mnożę {0} przez {1}"],
    4: ["Dzielenie", "dzielić", "dzielenia", "Dzielę {0} przez {1}"]
}
def choose_operation_type(z):
    '''
    Function that checks if given input is equal to: 1 or 2 or 3 or 4.

    :return: input (string)
    '''
    t = check_int_float(z)
    while True:
        if  t < 1 or t > 4:
            t = input("Podane dane to nie liczba naturalna w przedziale 1 - 4!: ")
            continue
        else:
            break
    return int(t)

def check_int_float(x, y = True):
    """
    Checks if user input x is an: int or float. If parameter y is True than method will check if number x is int.
    If False than it will check if it's a float.

    :param x: input to be checked.
    :param y: True for int check / False for float check.
    :return: int / float of input.
    """
    z = x
    while True:
        try:
            if y == True:
                t = 'powinieneś wpisać liczbę całkowitą'
                int(z)
            else:
                t = 'powinieneś wpisać liczbę rzeczywistą'
                float(z)
        except ValueError:
            z = input("Wprowadź poprawne dane - {0}: ".format(t))
            continue
        else:
            break

    if y == True:
        return int(z)
    else:
        return float(z)

def check_numbers(x):
    """
    Function that checks if given input is number equal or greater than 2

    :param x: input to be checked.
    :return: input (int) which is equal or greater than 2
    """

    if x == 1 or x == 3:
        z = input(f'Podaj ile liczb chcesz {OPERATION_TYPE[int(x)][1]}: ')
        while True:
            t = check_int_float(z)
            if t >= 2:
                return t
            elif t < 2:
                print("Działanie {0} musi się składać z conajmniej 2 liczb!".format(OPERATION_TYPE[x][2]))
                continue
    else:
        return 2

def calculate(how_many_numbers, calculation_type):
    """
    Calculator function. Have 4 different equasions: '+', '-', '*', "/"

    :param how_many_numbers: int attribute taken from input - it tells how many numbers will be in equasion.
    :param calculation_type: str attribute tells which operation will be in equasion.
    :return: result of equasion (float).
    """
    i = 1
    text = ''
    numbers = ['', '']
    for number in range(0, how_many_numbers):
        if number == 0:
            x = float(input(f'Podaj {i} liczbę: '))
            check_int_float(x, False)
            result = x
            i += 1
        else:
            x = float(input(f'Podaj {i} liczbę, którą chcesz {OPERATION_TYPE[calculation_type][1]}: '))
            if calculation_type == 4:
                result /= x
            elif calculation_type == 1:
                result += x
            elif calculation_type == 2:
                result -= x
            elif calculation_type == 3:
                result *= x
            elif calculation_type == 4 and x == 0:
                x = float(input('Nie można dzielić przez 0, podaj liczbę większą od zera: '))
                while True:
                    if check_int_float(x) > 0:
                        return z
                    elif check_int_float(z) < 0:
                        print("Nie można dzielić przez 0!")
                        continue
                result /= x
            i+=1
        if number == 0:
            numbers[0] = x
        elif number == 1:
            numbers[1] = str(x)
        else:
            text += ' i ' + str(x)
    numbers[1] += text
    if __name__ == "__main__":
        logging.debug(f'{OPERATION_TYPE[calculation_type][3].format(numbers[0], numbers[1])}')
    return result

x = input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ')
operation_number = choose_operation_type(x)

print(f'Wynik to: {calculate(check_numbers(operation_number), operation_number)}')





