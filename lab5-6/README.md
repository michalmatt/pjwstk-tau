## TAU lab5-6: Maven - lista poleceń
1. Instalacja Maven'a
2. Projekt z laboratoriów 1 dostosować do środowiska Mavenowego
3. Dopisanie nowej funkcjonalności w projekcie
4. Utworzenie minimum 7 nowych testów
5. Dodanie dwóch nowych dependencji
6. Utworzenie minimum 3 nowych testów do punktu 5.
### O aplikacji "Kalkulator kredytowy"
Aplikacja generuje harmonogram spłaty kredytu dla zadanych parametrów:
- Wnioskowana kwota kredytu
- Ilość rat
- Oprocentowanie
- Opłata stała
- Rodzaj rat (stała wysokość lub raty malejące)
### Folder "screenshots" (zawartość):
- Uruchomienie projektu z CLI komendą "mvn jetty:run"
- Uruchomienie testów z CLI komendą "mvn test"
- Widok formularza w aplikacji
- Widok harmonogramu spłaty w aplikacji
### Testy:
1. wnioskowanaKwotaKredytu = null
2. wnioskowanaKwotaKredytu "is empty"
3. iloscRat = null
4. iloscRat "is empty"
5. oprocentowanie = null
6. oprocentowanie "is empty"
7. oplataStala = null
8. oplataStala "is empty"
9. rodzajRat = null
10. rodzajRat "is empty"