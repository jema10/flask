import mysql.connector
from mysql.connector import Error


def db():
	print("진입1")
	try:
		print("진입2")
		conn = mysql.connector.connect(
			host='localhost',
			port='3306', 
			database='master',
			user='root',
			password='123456'
		)
		#return conn
		#print("진입3")
	except Error as e:
		print(f"에러:{e}")

	return conn
def main():
	print("start program")
	conn = db()
	print(conn)
	if(conn):
		print("연결성공")

if __name__ == "__main__":
	main()