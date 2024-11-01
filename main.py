import os
import subprocess
import shutil
from datetime import datetime

PWD = os.getcwd()
ssk = PWD + "/skrypty"

def clear_screen():
    subprocess.run("clear", shell=True)

def log_run(skrypt):
    with open("logs.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: Uruchomiono skrypt - {skrypt}\n")

def pokaz_pwd():
    global PWD
    print(f"Aktualny katalog: {PWD}")
    input("\nNaciśnij ENTER, aby kontynuować")                    

def main():
    try:
        while True:
            clear_screen()
            print(f"Witaj w Karmiz - {PWD}\n")
            print("Menu:\n")
            print("1.  Pomoc")
            print("2.  Informacje o projekcie")
            print("3.  Skrypty")
            print("4.  Pokaż aktualny katalog")
            print("5.  Wyświetl pliki w aktualnym katalogu")
            print("6.  Zmień katalog")
            print("7.  Utwórz plik")
            print("8.  Usuń plik")
            print("9.  Utwórz katalog")
            print("10. Usuń katalog")
            print("11. Wyjście\n")
            wybor = input("Wpisz numer wybranej opcji: ")

            clear_screen()

            if wybor == "1":
                pomoc()
            elif wybor == "2":
                info()
            elif wybor == "3":
                skrypty()
            elif wybor == "4":
                pokaz_pwd()
            elif wybor == "5":
                ls()
            elif wybor == "6":
                cd()
            elif wybor == "7":
                create_file()
            elif wybor == "8":
                delete_file()
            elif wybor == "9":
                create_directory()
            elif wybor == "10":
                delete_directory()
            elif wybor == "11":
                confirm_exit = input("Czy na pewno chcesz wyjść? (t/N): ")
                if confirm_exit.lower() == "t":
                    clear_screen()
                    break
                elif confirm_exit.lower() in ["", "n"]:
                    print()
                else:
                    input("Nieprawidłowy wybór. Naciśnij ENTER, aby kontynuować.")
            else:
                input("Nieprawidłowy wybór. Naciśnij ENTER, aby kontynuować.")
    except KeyboardInterrupt:
        print("\nProgram zakończony przez użytkownika.")

def pomoc():
    print("Sekcja Pomoc: Tutaj znajdziesz wskazówki dotyczące korzystania z programu.\n")
    input("Naciśnij ENTER, aby kontynuować")

def info():
    print("Karmiz został stworzony, aby ułatwić pracę w terminalu dla początkujących.")
    print("\nAutor: Kmarz_PL")
    input("Naciśnij ENTER, aby kontynuować")

def skrypty():
    if not os.path.exists(ssk):
        print(f"Folder '{ssk}' nie istnieje.")
        input("Naciśnij ENTER, aby kontynuować")
        return

    skrypty = [f for f in os.listdir(ssk) if f.endswith(".py") or f.endswith(".sh")]
    if not skrypty:
        print("Brak dostępnych skryptów w folderze 'skrypty'.")
        input("Naciśnij ENTER, aby kontynuować")
        return

    print("Dostępne skrypty:")
    for skrypt in skrypty:
        print(skrypt)

    skrypt = input("\nWybierz skrypt lub wpisz 'q', aby wrócić: ").strip()

    if skrypt.lower() == 'q':
        return

    skrypt_path = os.path.join(ssk, skrypt)

    if skrypt in skrypty:
        if skrypt.endswith(".sh"):
            subprocess.run(["chmod", "+x", skrypt_path])
            subprocess.run([f"./{skrypt_path}"], shell=True)
            log_run(skrypt)
        elif skrypt.endswith(".py"):
            subprocess.run(["python3", skrypt_path])
            log_run(skrypt)
    else:
        print("Nieprawidłowy wybór lub skrypt nie istnieje.")
    input("\nNaciśnij ENTER, aby kontynuować")

def ls():
    print("Lista plików:\n")
    os.system("ls")
    input("\nNaciśnij ENTER, aby kontynuować")

def cd():
    global PWD
    print(f"Aktualny katalog: {PWD}\n")
    kdz = input('Wpisz nazwę katalogu lub "..", aby wyjść: ').strip()
    
    if kdz == "..":
        PWD = os.path.abspath(os.path.join(PWD, os.pardir))
    else:
        new_path = os.path.join(PWD, kdz)
        if os.path.isdir(new_path):
            PWD = new_path
        else:
            print(f"Katalog '{kdz}' nie istnieje.")
    
    clear_screen()
    print(f"Zmieniono katalog. Aktualna ścieżka: {PWD}")
    input("\nNaciśnij ENTER, aby kontynuować")

def create_file():
    file_name = input("Podaj nazwę pliku do utworzenia: ").strip()
    if file_name:
        file_path = os.path.join(PWD, file_name)
        with open(file_path, 'w') as f:
            f.write("")
        print(f"Plik '{file_name}' został utworzony.")
    else:
        print("Nie podano nazwy pliku.")
    input("\nNaciśnij ENTER, aby kontynuować")

def delete_file():
    file_name = input("Podaj nazwę pliku do usunięcia: ").strip()
    if file_name:
        file_path = os.path.join(PWD, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Plik '{file_name}' został usunięty.")
        else:
            print(f"Plik '{file_name}' nie istnieje.")
    else:
        print("Nie podano nazwy pliku.")
    input("\nNaciśnij ENTER, aby kontynuować")

def create_directory():
    dir_name = input("Podaj nazwę katalogu do utworzenia: ").strip()
    if dir_name:
        dir_path = os.path.join(PWD, dir_name)
        try:
            os.makedirs(dir_path)
            print(f"Katalog '{dir_name}' został utworzony.")
        except FileExistsError:
            print(f"Katalog '{dir_name}' już istnieje.")
    else:
        print("Nie podano nazwy katalogu.")
    input("\nNaciśnij ENTER, aby kontynuować")

def delete_directory():
    dir_name = input("Podaj nazwę katalogu do usunięcia: ").strip()
    if dir_name:
        dir_path = os.path.join(PWD, dir_name)
        if os.path.exists(dir_path):
            try:
                shutil.rmtree(dir_path)
                print(f"Katalog '{dir_name}' został usunięty.")
            except OSError as e:
                print(f"Nie można usunąć katalogu '{dir_name}'. Błąd: {e}")
        else:
            print(f"Katalog '{dir_name}' nie istnieje.")
    else:
        print("Nie podano nazwy katalogu.")
    input("\nNaciśnij ENTER, aby kontynuować")

main()
