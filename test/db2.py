import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        # MySQL 데이터베이스에 연결
        connection = mysql.connector.connect(
            host='localhost',      # MySQL 서버 주소
            user='your_username',  # 사용자 이름
            password='your_password',  # 비밀번호
            database='your_database'   # 사용할 데이터베이스 이름
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INT NOT NULL
            )
        ''')
        connection.commit()
        print("Table 'users' created or already exists.")
    except Error as e:
        print(f"Error creating table: {e}")

def insert_data(connection, name, age):
    try:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO users (name, age) VALUES (%s, %s)', (name, age))
        connection.commit()
        print(f"Inserted {name}, {age} into 'users'.")
    except Error as e:
        print(f"Error inserting data: {e}")

def fetch_data(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        print("User data:")
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error fetching data: {e}")

def main():
    # 데이터베이스 연결
    connection = connect_to_database()
    if connection is None:
        print("Failed to connect to the database. Exiting.")
        return

    try:
        # 테이블 생성
        create_table(connection)

        # 데이터 삽입
        insert_data(connection, 'Alice', 25)
        insert_data(connection, 'Bob', 30)

        # 데이터 조회
        fetch_data(connection)

    finally:
        # 연결 닫기
        if connection.is_connected():
            connection.close()
            print("Database connection closed.")

if __name__ == '__main__':
    main()
