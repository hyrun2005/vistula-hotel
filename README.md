﻿# vistula-hotel-restaurant

Dokumentacja dla strony internetowej "Vistula Hotel & Restaurant"
1. Strona główna
URL: http://13.60.235.95:8000/
Główna zawartość:
oBaner: Nagłówek "Enjoy your stay" z przyciskiem Rooms prowadzącym do strony z pokojami.
oHistoria hotelu: Opis komfortu i usług hotelu: 20 nowocześnie urządzonych pokoi, widok na rzekę, telewizor, Wi-Fi.
oCechy szczególne:
Great Location: Malownicza lokalizacja.
Meals On The House: Kuchnia polska i międzynarodowa.
Fitness Room: Nowoczesna siłownia dostępna dla gości.

2. O nas (About)
URL: /about/
Główna zawartość:
oOur Mission: Oferowanie najlepszych rozwiązań z gwarancją najwyższej jakości usług.
oHotel Highlights:
Nowoczesne udogodnienia: Szybki internet Wi-Fi, telewizor z płaskim ekranem, luksusowe łóżko.
Lokalizacja: W pobliżu Starego Miasta w Warszawie.
Atrakcje: Siłownia, spa, sale konferencyjne.
oRestaurant Experience:
Kuchnia: Tradycyjne polskie dania z nowoczesnym akcentem.
Atmosfera: Żywa muzyka i tematyczne wydarzenia.
oAdditional Features:
Inicjatywy kulturalne (współpraca z lokalnymi artystami).
Spersonalizowana obsługa dla każdego gościa.

3. Strona kontaktowa (Contact Us)
URL: /contactUs/
Zawartość:
oFormularz kontaktowy:
Pola: Name, Email, Message.
Przycisk Submit do wysyłania wiadomości.

4. Strona pokoi (Rooms)
URL: /rooms/
Główna zawartość:
oLista dostępnych pokoi z krótkim opisem, ceną i statusem dostępności:
SINGLE - Room 212 Standard: $400.00 za noc.
SINGLE - Room 312 Luxe: $800.00 za noc.
SINGLE - Room 412 President Luxe: $1200.00 za noc.
DOUBLE - Room 215 Standard: $600.00 za noc.
DOUBLE - Room 315 Luxe: $1000.00 za noc.
DOUBLE - Room 415President  Luxe: $1400.00 za noc.
MORE - Room 217 Standard: $900.00 za noc.
DOUBLE - Room 317 Luxe: $1300.00 za noc.
DOUBLE - Room 417 President  Luxe: $1800.00 za noc.
oPrzyciski: View Details do przeglądania szczegółów pokoju.
Strona szczegółów pokoju:
oURL: /rooms/{id}/
oZawartość:
Szczegółowy opis pokoju.
Cena za noc.
Status dostępności z opcją rezerwacji.
Przycisk Book Now do wyboru dat rezerwacji.
Rezerwacja:
oPo potwierdzeniu rezerwacji klient otrzymuje wiadomość e-mail z jej szczegółami.
oNa stronie rezerwacji status płatności automatycznie aktualizuje się na PAID.
oDodatkowa płatność przez platformę zewnętrzną nie jest wymagana dla rezerwacji hotelowych.

5. Rezerwacja i płatność
URL: /rooms/booking/{id}/
Strona rezerwacji:
oPola do wyboru dat Check-in i Check-out.
oPrzycisk Confirm Booking do potwierdzenia rezerwacji.
Strona szczegółów rezerwacji:
oBooking ID: Unikalny identyfikator rezerwacji.
oEmail użytkownika: Adres e-mail użytkownika.
oRoom: Nazwa pokoju.
oCheck-in Date / Check-out Date: Daty pobytu.
oTotal Price: Łączny koszt.
oPayment Status: PAID (automatyczna aktualizacja po potwierdzeniu rezerwacji).

6. Restauracja (Vistula Restaurant)
URL: /restaurant/
Główna zawartość:
oBaner: "Welcome to Vistula Restaurant" z przyciskiem View Our Menu.
oOur Story: Historia restauracji z naciskiem na jakość i atmosferę.
oCechy szczególne:
Exquisite Cuisine: Tradycyjne i nowoczesne dania.
Fine Beverages: Starannie dobrane napoje i koktajle.
Exceptional Service: Wykwalifikowany personel.
Menu restauracji:
oDania:
Desery, Burgery, Napoje, Dania główne, Zupy – każda kategoria zawiera zdjęcia, opisy i ceny.
oKoszyk:
Możliwość dodania potraw do koszyka.
Przycisk Proceed to Order do złożenia zamówienia.
oSkładanie zamówienia:
Lista wybranych potraw z podsumowaniem ceny.
Przycisk Confirm Order do zatwierdzenia.
Płatność: Poprzez platformę Fondy dla bezpiecznych płatności online.

7. Funkcjonalność i integracja
1.Rezerwacja pokoi:
oPrzeglądanie dostępnych pokoi i ich rezerwacja.
oAutomatyczne potwierdzenie rezerwacji z aktualizacją statusu płatności na PAID i wysyłką szczegółów e-mailem.
2.Restauracja:
oPrzegląd menu z różnymi kategoriami potraw.
oKoszyk zakupowy do wyboru potraw i finalizacji zamówienia.
3.Płatność:
oIntegracja z platformą Fondy dla bezpiecznych płatności online w restauracji.

8. Podsumowanie
Strona Vistula Hotel & Restaurant to w pełni funkcjonalna aplikacja internetowa do:
Rezerwacji pokoi: Wygodny interfejs z automatycznym potwierdzeniem i aktualizacją statusu płatności.
Składania zamówień w restauracji: Nowoczesne funkcje koszyka i płatności przez platformę Fondy.
Informacji o hotelu i usługach: Kompleksowe informacje o ofercie i udogodnieniach.
Formularz kontaktowy: Możliwość szybkiego kontaktu z administracją.

Techniczna Dokumentacja Interfejsu Strony Internetowej
1. Stosowane Technologie
Backend: Django (Python)
Frontend: HTML, CSS, JavaScript
Baza danych: SQLite (domyślnie w Django) 
Panel administracyjny: Django Admin

2. Struktura Danych
2.1 Konta (Accounts)
User profiles: Rozszerzony model użytkownika Django.
oPola: imię, nazwisko, email, zdjęcie profilowe, data utworzenia.????

2.2 Autoryzacja i Uwierzytelnianie
Groups: Standardowy model Django do zarządzania grupami.
Users: Standardowy model użytkowników z dodatkowymi polami dla potrzeb aplikacji.

2.3 Pokoje Hotelowe (Hotel Rooms)
Bookings:
oPola: identyfikator użytkownika, numer pokoju, data rezerwacji, status płatności.
Payments:
oPola: identyfikator rezerwacji, kwota, status płatności, data transakcji.
Room photos:
oPola: numer pokoju, zdjęcie (ImageField), opis zdjęcia.
Rooms:
oPola: numer pokoju, typ pokoju, opis, cena za noc.

2.4 Restauracja (Restaurant)
Categorys (poprawna nazwa: Categories):
oPola: nazwa kategorii (np. przystawki, dania główne), opis.
Dishs (poprawna nazwa: Dishes):
oPola: nazwa potrawy, cena, kategoria (ForeignKey), opis, zdjęcie potrawy.

