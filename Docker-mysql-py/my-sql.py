# db_interactive.py

import psycopg2

# Replace with your actual DB container credentials
DB_HOST = "localhost"
DB_NAME = "userinfo"
DB_USER = "root"
DB_PASSWORD = "root"

def connect_db():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

def setup_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)

def add_name_to_db(cursor, conn, name):
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()
    print(f"✅ '{name}' added to the database.")

def display_names(cursor):
    cursor.execute("SELECT id, name FROM users")
    rows = cursor.fetchall()
    print("\n📋 Names in the database:")
    for row in rows:
        print(f"{row[0]}. {row[1]}")
    print()

def main():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        setup_table(cursor)

        while True:
            print("\nChoose an option:")
            print("1. Add a name")
            print("2. Display all names")
            print("3. Quit")
            choice = input("Enter choice [1/2/3]: ").strip()

            if choice == "1":
                name = input("Enter the name to add: ").strip()
                if name:
                    add_name_to_db(cursor, conn, name)
                else:
                    print("⚠️ Name cannot be empty.")
            elif choice == "2":
                display_names(cursor)
            elif choice == "3":
                print("👋 Exiting.")
                break
            else:
                print("❌ Invalid choice. Please enter 1, 2, or 3.")

    except Exception as e:
        print(f"🚫 Database error: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    main()
