setup Virtual Environment
-- cd vào project
-- python -m venv venv
-- venv\Scripts\activate
kiểm tra version python
--python --version

FastAPI:
--pip install fastapi uvicorn

Xuất thư viện sang txt
--pip freeze > requirements.txt
Run serve --backend:
--uvicorn main:app --reload

Hoc PostgreSQL và pgAdmin4 Basic

CREATE TABLE users (
id SERIAL PRIMARY KEY,
name VARCHAR(100),
email VARCHAR(100),
password VARCHAR(100)
);

INSERT INTO users(name,email,password)
VALUES(
'Duong',
'duong@gmail.com',
'123456'
);

.....

SQLAlchemy ORM
--pip install sqlalchemy psycopg2-binary

