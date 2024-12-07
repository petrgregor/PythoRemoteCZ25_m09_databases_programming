from datetime import date

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from p04_library.models import Base, Author, Book, Borrower, Loan

engine = create_engine('sqlite:///library.db', echo=False)
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)


def add_author(name, birth_date):
    with Session() as session:
        author = Author(name=name, birth_date=birth_date)
        session.add(author)
        session.commit()


def add_book(title, publication_date, author_id):
    with Session() as session:
        book = Book(title=title, publication_date=publication_date, author_id=author_id)
        session.add(book)
        session.commit()


def add_borrower(name, email):
    with Session() as session:
        borrower = Borrower(name=name, email=email)
        session.add(borrower)
        session.commit()


def borrow_book(book_id, borrower_id):
    with Session() as session:
        # Kontrola, zda kniha není již půjčena
        active_loan = session.query(Loan).filter_by(book_id=book_id, return_date=None).first()
        if active_loan:
            raise Exception(f"Kniha s ID {book_id} je již půjčena.")
        loan = Loan(book_id=book_id, borrower_id=borrower_id, loan_date=date.today())
        session.add(loan)
        session.commit()


def return_book(book_id):
    with Session() as session:
        loan = session.query(Loan).filter_by(book_id=book_id, return_date=None).first()
        if not loan:
            raise Exception(f"Kniha s ID {book_id} není aktuálně půjčena.")
        loan.return_date = date.today()
        session.commit()


def get_books_by_author(author_id):
    with Session() as session:
        books = session.query(Book).filter_by(author_id=author_id).all()
        return [book.title for book in books]


def get_available_books():
    with Session() as session:
        subquery = session.query(Loan.book_id).filter(Loan.return_date == None).subquery()
        books = session.query(Book).filter(~Book.id.in_(select(subquery))).all()
        return [book.title for book in books]


def get_active_borrowers():
    with Session() as session:
        borrowers = session.query(Borrower).join(Loan).filter(Loan.return_date == None).distinct().all()
        return [borrower.name for borrower in borrowers]


# Příklad použití
if __name__ == '__main__':
    """
    # Přidání dat
    add_author(name="J.K. Rowling", birth_date=date(1965, 7, 31))
    add_book(title="Harry Potter and the Philosopher's Stone", publication_date=date(1997, 6, 26), author_id=1)
    add_book(title="Harry Potter and the Chamber of Secrets", publication_date=date(1998, 7, 2), author_id=1)
    add_borrower(name="John Doe", email="john.doe@example.com")
    """

    """
    # Půjčení knihy
    try:
        borrow_book(book_id=1, borrower_id=1)
    except Exception as e:
        print(e)
    """
    """
    # Vrácení knihy
    try:
        return_book(book_id=1)
    except Exception as e:
        print(e)
    """

    # Dotazy
    print("Knihy autora J.K. Rowling:", get_books_by_author(author_id=1))
    print("Dostupné knihy:", get_available_books())
    print("Čtenáři s aktuálními půjčkami:", get_active_borrowers())
