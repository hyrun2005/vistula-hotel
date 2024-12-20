# vistula-hotel-restaurant

Dokumentacja dla strony internetowej "Vistula Hotel & Restaurant"
1. Strona główna
URL: http://13.60.235.95:8000/
Główna zawartość:
Baner: Nagłówek "Enjoy your stay" z przyciskiem Rooms prowadzącym do strony z pokojami.
Historia hotelu: Opis komfortu i usług hotelu: 20 nowocześnie urządzonych pokoi, widok na rzekę, telewizor, Wi-Fi.
Cechy szczególne:
Great Location: Malownicza lokalizacja.
Meals On The House: Kuchnia polska i międzynarodowa.
Fitness Room: Nowoczesna siłownia dostępna dla gości.
2. O nas (About)
URL: /about/
Główna zawartość:
Our Mission: Oferowanie najlepszych rozwiązań z gwarancją najwyższej jakości usług.
Hotel Highlights:
Nowoczesne udogodnienia: Szybki internet Wi-Fi, telewizor z płaskim ekranem, luksusowe łóżko.
Lokalizacja: W pobliżu Starego Miasta w Warszawie.
Atrakcje: Siłownia, spa, sale konferencyjne.
Restaurant Experience:
Kuchnia: Tradycyjne polskie dania z nowoczesnym akcentem.
Atmosfera: Żywa muzyka i tematyczne wydarzenia.
Additional Features:
Inicjatywy kulturalne (współpraca z lokalnymi artystami).
Spersonalizowana obsługa dla każdego gościa.
3. Strona kontaktowa (Contact Us)
URL: /contactUs/
Zawartość:
Formularz kontaktowy:
Pola: Name, Email, Message.
Przycisk Submit do wysyłania wiadomości.
4. Strona pokoi (Rooms)
URL: /rooms/
Główna zawartość:
Lista dostępnych pokoi z krótkim opisem, ceną i statusem dostępności:
SINGLE - Room 212 Standard: $400.00 za noc.
SINGLE - Room 312 Luxe: $800.00 za noc.
SINGLE - Room 412 President Luxe: $1200.00 za noc.
DOUBLE - Room 215 Standard: $600.00 za noc.
DOUBLE - Room 315 Luxe: $1000.00 za noc.
DOUBLE - Room 415President  Luxe: $1400.00 za noc.
MORE - Room 217 Standard: $900.00 za noc.
DOUBLE - Room 317 Luxe: $1300.00 za noc.
DOUBLE - Room 417 President  Luxe: $1800.00 za noc.
Przyciski: View Details do przeglądania szczegółów pokoju.
Strona szczegółów pokoju:
URL: /rooms/{id}/
Zawartość:
Szczegółowy opis pokoju.
Cena za noc.
Status dostępności z opcją rezerwacji.
Przycisk Book Now do wyboru dat rezerwacji.
Rezerwacja:
Po potwierdzeniu rezerwacji klient otrzymuje wiadomość e-mail z jej szczegółami.
Na stronie rezerwacji status płatności automatycznie aktualizuje się na PAID.
Dodatkowa płatność przez platformę zewnętrzną nie jest wymagana dla rezerwacji hotelowych.
5. Rezerwacja i płatność
URL: /rooms/booking/{id}/
Strona rezerwacji:
Pola do wyboru dat Check-in i Check-out.
Przycisk Confirm Booking do potwierdzenia rezerwacji.
Strona szczegółów rezerwacji:
Booking ID: Unikalny identyfikator rezerwacji.
Email użytkownika: Adres e-mail użytkownika.
oom: Nazwa pokoju.
Check-in Date / Check-out Date: Daty pobytu.
Total Price: Łączny koszt.
Payment Status: PAID (automatyczna aktualizacja po potwierdzeniu rezerwacji).
6. Restauracja (Vistula Restaurant)
URL: /restaurant/
Główna zawartość:
Baner: "Welcome to Vistula Restaurant" z przyciskiem View Our Menu.
Our Story: Historia restauracji z naciskiem na jakość i atmosferę.
Cechy szczególne:
Exquisite Cuisine: Tradycyjne i nowoczesne dania.
Fine Beverages: Starannie dobrane napoje i koktajle.
Exceptional Service: Wykwalifikowany personel.
Menu restauracji:
Dania:
Desery, Burgery, Napoje, Dania główne, Zupy – każda kategoria zawiera zdjęcia, opisy i ceny.
Koszyk:
Możliwość dodania potraw do koszyka.
Przycisk Proceed to Order do złożenia zamówienia.
Składanie zamówienia:
Lista wybranych potraw z podsumowaniem ceny.
Przycisk Confirm Order do zatwierdzenia.
Płatność: Poprzez platformę Fondy dla bezpiecznych płatności online.
7. Funkcjonalność i integracja
1.Rezerwacja pokoi:
Przeglądanie dostępnych pokoi i ich rezerwacja.
Automatyczne potwierdzenie rezerwacji z aktualizacją statusu płatności na PAID i wysyłką szczegółów e-mailem.
2.Restauracja:
Przegląd menu z różnymi kategoriami potraw.
Koszyk zakupowy do wyboru potraw i finalizacji zamówienia.
3.Płatność:
Integracja z platformą Fondy dla bezpiecznych płatności online w restauracji.

8. Podsumowanie
Strona Vistula Hotel & Restaurant to w pełni funkcjonalna aplikacja internetowa do:
Rezerwacji pokoi: Wygodny interfejs z automatycznym potwierdzeniem i aktualizacją statusu płatności.
Składania zamówień w restauracji: Nowoczesne funkcje koszyka i płatności przez platformę Fondy.
Informacji o hotelu i usługach: Kompleksowe informacje o ofercie i udogodnieniach.
Formularz kontaktowy: Możliwość szybkiego kontaktu z administracją.
Techniczna Dokumentacja Interfejsu Strony Internetowej
1. Stosowane Technologie
Backend: Django (Python)
Frontend: HTML, CSS, JavaScript
Baza danych: SQLite (domyślnie w Django) 
Panel administracyjny: Django Admin
2. Struktura Danych
2.1 Konta (Accounts)
User profiles: Rozszerzony model użytkownika Django.
Pola: imię, nazwisko, email, zdjęcie profilowe, data utworzenia.????

2.2 Autoryzacja i Uwierzytelnianie
Groups: Standardowy model Django do zarządzania grupami.
Users: Standardowy model użytkowników z dodatkowymi polami dla potrzeb aplikacji.

2.3 Pokoje Hotelowe (Hotel Rooms)
Bookings:
Pola: identyfikator użytkownika, numer pokoju, data rezerwacji, status płatności.
Payments:
Pola: identyfikator rezerwacji, kwota, status płatności, data transakcji.
Room photos:
Pola: numer pokoju, zdjęcie (ImageField), opis zdjęcia.
Rooms:
Pola: numer pokoju, typ pokoju, opis, cena za noc.
2.4 Restauracja (Restaurant)
Categorys (poprawna nazwa: Categories):
Pola: nazwa kategorii (np. przystawki, dania główne), opis.
Dishs (poprawna nazwa: Dishes):
Pola: nazwa potrawy, cena, kategoria (ForeignKey), opis, zdjęcie potrawy.
