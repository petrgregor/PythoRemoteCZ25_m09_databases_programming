from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    books = relationship('Book', back_populates='author')


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    publication_date = Column(Date, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    author = relationship('Author', back_populates='books')
    loans = relationship('Loan', back_populates='book')


class Borrower(Base):
    __tablename__ = 'borrowers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    loans = relationship('Loan', back_populates='borrower')


class Loan(Base):
    __tablename__ = 'loans'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    borrower_id = Column(Integer, ForeignKey('borrowers.id'), nullable=False)
    loan_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=True)
    book = relationship('Book', back_populates='loans')
    borrower = relationship('Borrower', back_populates='loans')
