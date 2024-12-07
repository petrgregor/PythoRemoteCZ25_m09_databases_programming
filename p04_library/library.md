# Správa knihovny
Vytvoř aplikaci v Pythonu s využitím SQLAlchemy,
která bude simulovat jednoduchý systém správy knihovny. 
Aplikace by měla mít následující funkce:

## Přidání dat:
- Přidej několik autorů a jejich knih.
- Přidej několik čtenářů (borrowers).

## Vypůjčení knihy:
- Vytvoř funkci, která umožní půjčit knihu konkrétnímu čtenáři 
(vytvořením záznamu v tabulce Loans).

## Vrácení knihy:
- Vytvoř funkci, která umožní označit knihu jako vrácenou 
(return_date se nastaví na aktuální datum).

## Dotazy:
- Vypiš všechny knihy konkrétního autora.
- Najdi všechny knihy, které aktuálně nejsou půjčené.
- Vypiš čtenáře, kteří mají aktuálně alespoň jednu půjčenou knihu. 

## Bonusové úkoly (nepovinné)
- Implementuj omezení, které zabrání půjčení knihy, 
pokud už je aktuálně půjčená.
- Vypiš statistiku: Počet půjček na každého čtenáře.
- Vytvoř funkci pro zobrazení přehledu všech aktuálních půjček.

## Ukázka kódu
```python
# Přidání dat
add_author(name="J.K. Rowling", birth_date="1965-07-31")
add_book(title="Harry Potter and the Philosopher's Stone", publication_date="1997-06-26", author_id=1)
add_borrower(name="John Doe", email="john.doe@example.com")

# Půjčení knihy
borrow_book(book_id=1, borrower_id=1)

# Vrácení knihy
return_book(book_id=1)

# Dotazy
print(get_books_by_author(author_id=1))
print(get_available_books())
print(get_active_borrowers())
```