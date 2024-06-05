-- Создание таблицы Сотрудник
CREATE TABLE Employee (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    department VARCHAR(255) NOT NULL,
    manager_id INT,
    note TEXT,
    FOREIGN KEY (manager_id) REFERENCES Employee(id)
);