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

def choose_operation_type():
    '''
    Function that checks if given input is equal to: 1 or 2 or 3 or 4.

    :return: input (string)
    '''

    while True:
        try:
            x = int(input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: '))
            if x < 1 or x > 4:
                print("Podane dane to nie liczba naturalna w przedziale 1 - 4!")
                continue
        except ValueError:
            print("Podane dane to nie liczba naturalna w przedziale 1 - 4!")
            continue
        else:
           break
    z = "{0}".format(x)
    return z

operation_number = choose_operation_type()

operation_type = {
    '1': ["Dodawanie", "dodać", "dodawania", "Dodaję do {0} liczby {1}"],
    '2': ["Odejmowanie", "odjąć", "odejmowania", "Odejmuję od {0} liczby {1}"],
    '3': ["Mnozenie", "mnożyć", "mnożenia", "Mnożę {0} przez {1}"],
    '4': ["Dzielenie", "dzielić", "dzielenia", "Dzielę {0} przez {1}"]
}
def check_numbers(x):
    """
    Function that checks if given input is number equal or greater than 2

    :param x: input to be checked.
    :return: input (string) which is equal or greater than 2
    """
    while True:
        try:
            z = int(input(f'Podaj ile liczb chcesz {operation_type[x][1]}: '))
            if int(z) < 2:
                print("Działanie {0} musi się składać z conajmniej 2 liczb!".format(operation_type[x][2]))
                continue
        except ValueError:
            print("Podane dane to nie liczba naturalna!")
            continue
        else:
           break
    return z


def calculate(how_many_numbers, calculation_type):
    """
    Calculator function. Have 4 different equasions: '+', '-', '*', "/"

    :param how_many_numbers: int attribute taken from input - it tells how many numbers will be in equasion.
    :param calculation_type: str attribute tells which operation will be in equasion.
    :return: result of equasion (float).
    """
    i = 1
    result = float()
    text = ''
    numbers = ['', '']
    for number in range(0, how_many_numbers):
        while True:
            try:
                if number == 0:
                    x = float(input(f'Podaj {i} liczbę: '))
                else:
                    x = float(input(f'Podaj {i} liczbę, którą chcesz {operation_type[calculation_type][1]}: '))
            except ValueError:
                print("Podane dane to nie liczba")
                continue
            else:
                if int(calculation_type) == 4:
                    result /= x
                    i += 1
                break
        if int(calculation_type) == 1:
            result += x
            i += 1
        elif int(calculation_type) == 2 and number == 0:
            result = x
            i += 1
        elif int(calculation_type) == 2 and number > 0:
            result -= x
            i += 1
        elif int(calculation_type) == 3 and number == 0:
            result = x
            i += 1
        elif int(calculation_type) == 3 and number > 0:
            result *= x
            i += 1
        elif int(calculation_type) == 4 and number == 0:
            result = x
        elif int(calculation_type) == 4 and number > 0 and x == 0:
            while True:
                if x == 0:
                    while True:
                        try:
                            x = float(input('Nie można dzielić przez 0, podaj liczbę większą od zera: '))
                        except ValueError:
                            continue
                        else:
                            if float(x) != 0:
                                break
                            continue
                    i += 1
                    break
            result /= x

        if number == 0:
            numbers[0] = x
        elif number == 1:
            numbers[1] = str(x)
        else:
            text += ' i ' + str(x)

    numbers[1] += text
    logging.debug(f'{operation_type[str(calculation_type)][3].format(numbers[0], numbers[1])}')
    return result


print(f'Wynik to: {calculate(check_numbers(operation_number), operation_number)}')





