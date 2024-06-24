import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Shop, Book, Stock, Sale

DSN = 'postgresql://postgres:password@localhost:5432/netology_db'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open('fixtures/tests_data.json', 'r') as fd:
    data = json.load(fd)

for record in data:
    model_name = record.get('model')
    model_class = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }.get(model_name, None)

    if model_class is not None:
        obj = model_class(**record.get('fields'))
        session.add(obj)
        session.commit()
    else:
        print(f"Класс не найден: {model_name}")

def get_shops(search_term):
    query = session.query(
        Book.title,
        Shop.name,
        Sale.price,
        Sale.date_sale
    ).select_from(Sale).join(Stock, Sale.id_stock == Stock.id).join(Book, Stock.id_book == Book.id).join(Publisher, Book.id_publisher == Publisher.id)

    if search_term.isdigit():
        query = query.filter(Publisher.id == search_term)
    else:
        query = query.filter(Publisher.name == search_term)

    for book_title, shop_name, price, date_sale in query.all():
        print(f"{book_title: <40} | {shop_name: <10} | {price: <8} | {date_sale.strftime('%d-%m-%Y')}")

if __name__ == '__main__':
    search_term = input("Введите название издателя или его ID: ")
    get_shops(search_term)