#pip install mysql-connector-python
import mysql.connector

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
    # 테이블 생성
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

def insert_data(connection, username, password,email):
    # 데이터 삽입
    print("입력시작")
    cursor = connection.cursor()
    cursor.execute('INSERT INTO user (username, password,email) VALUES (%s, %s,%s)', (username, password,email))
    connection.commit()
    print(f"Inserted {username}, {password} into 'users'.")
    print("입력종료")
def fetch_data(connection):
    # 데이터 조회
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    print("User data:")
    for row in rows:
        print(row)

def main():
    print("start program")
    # 데이터베이스 연결
    connection = connect_to_database()

    # 테이블 생성
    #create_table(connection)

    # 데이터 삽입
    insert_data(connection, 'admin', '123456')
    insert_data(connection, 'test1', '123456')

    # 데이터 조회
    fetch_data(connection)

    # 연결 닫기
    connection.close()

if __name__ == '__main__':
    main()
