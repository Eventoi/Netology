import psycopg2

with psycopg2.connect(database="netology_db", user="postgres", password="") as conn:

# Создание таблицы клиентов
def create_clients_table():
    with conn.cursor() as cur:
        create_current_clients_table = """
            CREATE TABLE IF NOT EXISTS clients
            (id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            email VARCHAR(50) NOT NULL,
            phone BIGINT);"""
        cur.execute(create_current_clients_table)
    conn.commit()
create_clients_table()

# Создание таблицы с номерами телефонов
def create_phone_numbers_table():
    with conn.cursor() as cur:
        create_current_phone_numbers_table = """
            CREATE TABLE IF NOT EXISTS phone_numbers
            (id SERIAL PRIMARY KEY,
            client_id INT,
            phone BIGINT,
            FOREIGN KEY (client_id) REFERENCES clients(id));"""
        cur.execute(create_current_phone_numbers_table)
    conn.commit()
create_phone_numbers_table()



# Добавление нового клиента
def add_client(first_name, last_name, email, phone):
    with conn.cursor() as cur:
        add_current_client = """
            INSERT INTO clients (first_name, last_name, email, phone)
            VALUES (%s, %s, %s, %s)
            RETURNING id;"""
        cur.execute(add_current_client, (first_name, last_name, email, phone))
    # Получение id добавленного клиента
        client_id = cur.fetchone()[0]
    conn.commit()
# add_client("Новый", "Студент", "New_student@com.dot", 9874563210)

# Изменения данных о клиенте
def update_client_info(id, first_name=None, last_name=None, email=None, phone=None):
    with conn.cursor() as cur:

        update_query = 'UPDATE clients SET '
        params = []

        if first_name is not None:
            update_query += 'first_name = %s, '
            params.append(first_name)

        if last_name is not None:
            update_query += 'last_name = %s, '
            params.append(last_name)

        if email is not None:
            update_query += 'email = %s, '
            params.append(email)

        if phone is not None:
            update_query += 'phone = %s, '
            params.append(phone)

        # Удаление последней запятой и пробела из запроса
        update_query = update_query.rstrip(', ')

        # Добавление условия WHERE для конкретного id
        update_query += ' WHERE id = %s;'
        params.append(id)

        # Выполнение запроса с динамическими параметрами
        cur.execute(update_query, params)
    conn.commit()
# update_client_info(7, first_name="Капитан Джек", last_name="Воробей", email="Сapt.Jack_sparrow@comic.com", phone=None)

# Поиск клиента по имеющимся данным
def find_client(first_name=None, last_name=None, email=None, phone=None):
    with conn.cursor() as cur:
        # Формирование динамического SQL-запроса и параметров
        find_query = 'SELECT * FROM clients WHERE '
        params = []

        if first_name is not None:
            find_query += 'first_name = %s AND '
            params.append(first_name)

        if last_name is not None:
            find_query += 'last_name = %s AND '
            params.append(last_name)

        if email is not None:
            find_query += 'email = %s AND '
            params.append(email)

        if phone is not None:
            find_query += 'phone = %s AND '
            params.append(phone)

        # Удаление последнего "AND" из запроса
        find_query = find_query.rstrip(' AND ')

        # Выполнение запроса с динамическими параметрами
        cur.execute(find_query, params)
        return cur.fetchall()

# result = find_client(first_name="Ученик", last_name="Нетологии")
# if result:
#     print(f'Найден клиент: {result}')
# else:
#     print("Клиент не найден")

# Удаление клиента
def delete_client(id):
    with conn.cursor() as cur:
        delete_current_client = """
            DELETE FROM clients
            WHERE id = %s;"""
        cur.execute(delete_current_client, (id,))
    conn.commit()
# delete_client(8)



# Добавление номера телефона
def add_phone_number(client_id, phone):
    with conn.cursor() as cur:
        insert_phone_number = """
            INSERT INTO phone_numbers (client_id, phone)
            VALUES (%s, %s);"""
        cur.execute(insert_phone_number, (client_id, phone))
    # Обновление последнего добавленного номера в таблице clients
        update_client_phone = """
            UPDATE clients
            SET phone = %s
            WHERE id = %s;"""
        cur.execute(update_client_phone, (id, phone))
    conn.commit()
# add_phone_number(11, 9874563210123)

# Удаление номера телефона
def delete_phone_number(client_id, phone):
    with conn.cursor() as cur:
        delete_current_phone_number = """
            UPDATE clients
            SET phone = NULL
            WHERE id = %s;"""
        cur.execute(delete_current_phone_number, (id,))
    conn.commit()
# delete_phone_number(2)

# Автозаполнение таблицы phone_numbers из таблицы clients, если последняя была создана и заполнена раньше
# def export_clients_phone_numbers():
#     with conn.cursor() as cur:
#         phone_numbers_query = """
#             INSERT INTO phone_numbers (client_id, phone)
#             SELECT id, phone
#             FROM clients
#             WHERE phone IS NOT NULL;"""
#         cur.execute(phone_numbers_query)
#     conn.commit()
# export_clients_phone_numbers()


conn.close()