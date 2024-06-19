from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Publisher, Book, Shop, Stock, Sale

# Создаем подключение к базе данных
engine = create_engine('postgresql://postgres:password@localhost:5432/netology_db')
Session = sessionmaker(bind=engine)
session = Session()

def query_publisher_info():
    # Получаем имя или идентификатор издателя от пользователя
    publisher_name = input("Введите имя или идентификатор издателя: ")

    # Ищем издателя в базе данных
    publisher = session.query(Publisher).filter_by(name=publisher_name).first()

    if publisher:
        # Запрос выборки фактов покупки книг этого издателя
        purchases = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale) \
            .join(Stock) \
            .join(Shop) \
            .join(Sale) \
            .filter(Book.id_publisher == publisher.id) \
            .all()

        # Выводим результаты
        for title, shop_name, price, date_sale in purchases:
            print(f"{title} | {shop_name} | {price} | {date_sale.strftime('%d-%m-%Y')}")
    else:
        print("Издатель не найден.")

    session.close()