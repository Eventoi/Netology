import sqlalchemy as sq
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

engine = create_engine('postgresql://postgres:password@localhost:5432/netology_db')

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

class Publisher(Base):
    __tablename__ = "publisher"
    id = Column(Integer, primary_key=True)
    name = Column(String(length=100), nullable=False, unique=True)

    def __str__(self):
        return f'Издатель {self.id}: {self.name}'

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    title = Column(String(length=100), nullable=False)
    id_publisher = Column(Integer, ForeignKey("publisher.id"), nullable=False)
    publisher = relationship(Publisher, backref="books")

    def __str__(self):
        return f'Книга {self.id}: {self.title}, {self.id_publisher}'

class Shop(Base):
    __tablename__ = "shop"
    id = Column(Integer, primary_key=True)
    name = Column(String(length=100), nullable=False, unique=True)

    def __str__(self):
        return f'Магазин {self.id}: {self.name}'

class Stock(Base):
    __tablename__ = "stock"
    id = Column(Integer, primary_key=True)
    id_book = Column(Integer, ForeignKey("book.id"), nullable=False)
    id_shop = Column(Integer, ForeignKey("shop.id"), nullable=False)
    count = Column(Integer, nullable=False)

    def __str__(self):
        return f'Магазин {self.id}: {self.id_book}, {self.id_shop}, {self.count}'

class Sale(Base):
    __tablename__ = "sale"
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    date_sale = Column(Date, nullable=False)
    id_stock = Column(Integer, ForeignKey("stock.id"), nullable=False)
    count = Column(Integer, nullable=False)