=== PSQL INSTALL ===
sudo apt update
sudo apt install postgresql
sudo systemctl status postgresql

=== CLI ROOT ===
sudo -u postgres psql - вхід під суперюзер
sudo -i -u postgres - вхід з під рута OS якшо забув пароль
CREATE USER username WITH PASSWORD 'password';  -- Створення користувача
ALTER USER username CREATEDB, CREATEROLE;        -- Дозволяємо права
ALTER USER username NOCREATEDB;                  -- Забираємо право
CREATE DATABASE db_name OWNER username;          -- Створення БД з власником
DROP DATABASE db_name;                           -- Видалення БД
\du         -- Список користувачів (\du+)
\l          -- Список БД (\l+)
\c db_name  -- Заходимо/підключаємося до конкретної БД (лапки не потрібні)
\q          -- Вихід з CLI psql
ALTER DATABASE db_name RENAME TO new_db_name;     -- Перейменувати БД (потрібно відключити всіх)
ALTER ROLE old_user RENAME TO new_name;           -- Перейменувати користувача
ALTER ROLE username WITH PASSWORD 'new_password'; -- Зміна/встановлення пароля


=== CLI USER ===
psql -U admin -h localhost -d 'db_name' -p 5432 - логування користувача
-- ПРАВА ДОСТУПУ (GRANT / REVOKE):
GRANT CONNECT ON DATABASE db_name TO new_user;             -- Дозволити підключатися до БД
GRANT SELECT, INSERT ON TABLE my_table TO new_user;        -- Дозволити читати/писати в конкретну таблицю
GRANT ALL ON DATABASE db_name TO new_user;                 -- Дати всі права на БД
REVOKE SELECT, INSERT ON TABLE my_table FROM new_user;     -- Забираємо права

-- СХЕМИ:
SHOW search_path;                                  -- В які схеми зараз дивиться сесія
DROP SCHEMA public CASCADE;                -- Видалити схему public (CASCADE видалить і все, що всередині)
CREATE SCHEMA schema_name;                         -- Створення схеми
ALTER SCHEMA schema_name OWNER TO username;        -- Зміна власника схеми
GRANT ALL ON SCHEMA schema_name TO new_user;       -- Права на рівні схеми
GRANT CREATE ON SCHEMA schema_name TO new_user;    -- Дозвіл створювати таблиці всередині схеми
SET search_path TO schema_name;                    -- Тимчасово змінити схему для поточної сесії
ALTER ROLE username SET search_path TO new_schema; -- Назавжди закріпити схему за користувачем
CREATE TABLE schema_name.table_name (...);         -- Створення таблиці в конкретній схемі
SELECT * FROM schema_name.table_name;              -- Запит до таблиці в конкретній схемі




---
\dt # tables
\dt public.*  # all table in schemas
\du # all users (права)
\dn - schemas
\conninfo - користувач в поточний момент
\d rabota_ua -show table
\l # list database
\q - вихід

----
# PYTHON
pip install asyncpg # postgres
DB_URL = 'postgresql+asyncpg://admin:admin@localhost:5432/voron_crashed' # alchemy
DB_URL = 'postgresql://USERNAME:PASSWORD@localhost:5432/DB_NAME # sync
db_url= 'postgres://admin:admin@localhost:5432/DATABASE_NAME -  TORTOISE
DB_URL = 'postgres://admin:admin@localhost:5432/cine_tracker?schema=app' # конкретно в схему !
----
