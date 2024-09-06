# Wyświetl informację o programie
print("Kalkulator 4 prostych działań arytmetycznych na dwóch liczbach\n")

# Wyświetl dostępne opcje działania
print("Wybierz operacje jaką chcesz wykonać, poprzez wybranie numeru: ")
print("1 = Dodawanie")
print("2 = Odejmowanie")
print("3 = Mnozenie")
print("4 = Dzielenie")
print("5 = Zakoncz program \"Kalkulator\"")

# Poproś użytkownika o podanie numeru działania
choose = input("\npodaj numer działania które chcesz wykonać: ")

# Dopóki użytkownik nie wybierze 5, powtarzaj pętlę
while choose != '5':

    # Jeśli użytkownik wybrał 1, wykonaj dodawanie
    if choose == '1':
        # Poproś użytkownika o podanie dwóch liczb
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))

        # Oblicz sumę liczb
        sum = a+b
        # Wyświetl wynik
        print(f"\nWynik dodawania wynosi: {sum}")
    # Jeśli użytkownik wybrał 2, wykonaj odejmowanie
    elif choose == '2':
        # Poproś użytkownika o podanie dwóch liczb
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
    
        # Oblicz różnicę liczb
        diff = a - b
        # Wyświetl wynik
        print(f"\nWynik odejmowania wynosi: {diff}")
    # Jeśli użytkownik wybrał 3, wykonaj mnożenie
    elif choose == '3':
        # Poproś użytkownika o podanie dwóch liczb
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))

        # Oblicz iloczyn liczb
        prod = a * b
        # Wyświetl wynik
        print(f"\nWynik mnożenia wynosi: {prod}")
    # Jeśli użytkownik wybrał 4, wykonaj dzielenie
    elif choose == '4':
        # Poproś użytkownika o podanie dwóch liczb
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))

        # Sprawdź, czy druga liczba nie jest zerem
        if b != 0:
            # Oblicz iloraz liczb
            quot = a / b
            # Wyświetl wynik
            print(f"\nWynik dzielenia wynosi: {quot}")
        else:
            # Wyświetl komunikat o błędzie
            print("\nNie można dzielić przez zero")
    # Jeśli użytkownik wybrał inny numer, wyświetl komunikat o błędzie
    else:
        print("\nNieprawidłowy numer działania, podaj prawidłowy numer Działania")

    # Wyświetl ponownie dostępne opcje działania
    print("\nWybierz operacje jaką chcesz wykonać, poprzez wybranie numeru: ")
    print("1 = Dodawanie")
    print("2 = Odejmowanie")
    print("3 = Mnozenie")
    print("4 = Dzielenie")
    print("5 = Zakoncz program \"Kalkulator\"")
    # Poproś użytkownika o podanie numeru działania
    choose = input("\npodaj numer działania które chcesz wykonać: ")

# Jeśli użytkownik wybrał 5, zakończ program
print("\nZakończono działanie programu \"Kalkulator\"")