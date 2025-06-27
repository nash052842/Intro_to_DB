
def create_database():
    try:
        connection = mysql connector.connect(
            host='localhost',       
            user='root',          
            password='shem' 
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor=("CREATE DATABASE: alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
