# CIPHER
1. ROT13, ROT47 (SZYFR CEZARA) -> https://pl.wikipedia.org/wiki/Szyfr_Cezara
2. Funkcjonalności
   * FileHandlder odczyt, zapis do pliku, user podaje nazwe, wyjatki, Gdy chce zpiasca do tego samego pliku to append,
   * Szyfrowanie i Odszyfrowywanie.
   * Buffer czyli taka lista, która sobie istnieje podczas działania programu
   * Menu
   * Manager
   * IOReader io.print(), io.read()
   * Exit


### struktura obiekt
- {"ROT47": xyz}

3. Dodatkowe rzeczy:
    * FactoryMethod
    * Testy Jednostkowe

4. Stylistyka
   * PEP 8
   * GitFlow
   * Czeste commity
   * Conventioal commits
   * Typing
   * Docstrings
   * Cleancode itd.

TODO 02.08.22:
   * cipher.py ->  2. change prints to logger warning/print,
   * facade.py -> 1. refactor user_request_hanlder method while loop, so it has direct exit program?
   * 2. replace str menu with dict menu, write to file in form {ROT13: text}
      * filehandler.py -> method should create files dir for output files omodule os, os.getcwd(),
      * if not os.path.isdir(os.getcwd() + '/files'), os.mkdir
   * ioreader.py -> use logger warning/print instead of standard print


DONE:
1. rename method encode
2. add staticmethod
