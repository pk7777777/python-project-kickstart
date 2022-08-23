import sqlite3
import csv

DB_NAME = "user.db"
FILE = "sample_users.csv"

INPUT_STRING = """
Enter the option:
    1. CREATE TABLE users
    2. Import data from CSV file
    3. Add new record to databse
    4. Delete a record from id of user.
    5. Delete all records from user table.
    6. Query all records from user table.
    7. Update a record using id of user.
    8. Press any key to quit.

"""

CREATE_USERS_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name CHAR(255) NOT NULL,
        last_name CHAR(255) NOT NULL,
        company_name CHAR(255) NOT NULL,
        address CHAR(255) NOT NULL,
        city CHAR(255) NOT NULL,
        county CHAR(255) NOT NULL,
        state CHAR(255) NOT NULL,
        zip REAL NOT NULL,
        phone1 CHAR(255) NOT NULL,
        phone2 CHAR(255),
        email CHAR(255) NOT NULL,
        web text
    );
"""


COLUMNS = (
    "first_name",
    "last_name",
    "company_name",
    "address",
    "city",
    "county",
    "state",
    "zip",
    "phone1",
    "phone2",
    "email",
    "web"

)

COLUMN_INPUT_STRING = f"""
Which column would you like to update?. Please make sure column is one of the following:
{COLUMNS}
"""

def update_user(conn, column_name, user_id, column_values):
    """update sings record to table

    Args:
        conn (sqlite3): _description_
        column_name (_type_): _description_
        user_id (_type_): _description_
        column_values (_type_): _description_
    """
    cur = conn.execute(
        f"UPDATE users set {column_name}=? where id=?",(column_name, user_id)

    )
    conn.commit()

def create_connection(db_name):
    """creating connection and return cursor object
    
    Returns:
        cur: sqlite3.Connection object
    """
    conn = sqlite3.connect(db_name)
    except Exception as e:
        print(str(e))
        
    return conn

def create_table(conn):
    """create a table

    Args:
        conn (sqlite3 connection): sqlite connection object
    """
    cur = conn.cursor()
    cur.execute(CREATE_USERS_TABLE_QUERY)
    conn.commit()
    print("User table was successfully created.")


def open_csv_file(FILE):
    """opens csv files and return all records in list of tuple

    Args:
        FILE (str): _description_

    Returns:
        _type_: _description_
    """
    db_data = []
    with open(FILE) as f:
        data = csv.reader(f, delimiter=",")
        for datum in data:
            db_data.append(tuple(datum))
        return db_data[1:]

        

def insert_users(conn, db_data):
    """Insert record to table

    Args:
        conn (sqlite3 connection): sqlite3 connection object
        db_data (list[tuple]): all records for table
    
    Returns:
        None: None
    """
    user_add_query = '''
    INSERT INTO users
    (first_name,last_name,company_name,address,city,county,state,zip,phone1,phone2,email,web)

    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    '''
    cur = conn.cursor()
    cur.executemany(user_add_query, db_data)
    conn.commit()
    print("Sucessfully iserted data into user table")


def delete_user_id(conn, user_id):
    """delete single record from table

    Args:
        conn (sqlite3 connection): sqlite3 connection object
        user_id (int): if of user

    Returns:
        None: None

    """
    cur = conn.execute("DELETE from users where id = ?", (user_id,))
    conn.commit()
    print("Sucessfully deleted record from user table")

def delete_all_records(conn):
    cur = conn.execute("DELETE from users")
    conn.commit()
    print("Sucessfully deleted all record from user table")

def select_all_records(conn):
    cur = conn.execute("Select * from users;")
    for row in cur:
        print(row)

def main():
    while true
    conn = create_connection(DB_NAME)
    user_input = input(INPUT_STRING)

    if user_input == "1":
        create_table(conn)
        
    elif user_input == "2":
        data = open_csv_file(FILE)
        insert_users(conn, data)

    elif user_input == "3":
        data = []
        for column in COLUMNS:
            user_input = input(f"Enter {column}: ")
            data.append(user_input)

        data = tuple(data)
        insert_users(conn, [data])

    elif user_input == "4":
        user_id = input("Enter id of user: ")
        if user_id.isnumeric():
            delete_user_id(conn, user_id)

    elif user_input == "5":
        confirmation = input(
            "Are you sure?? \
            Press y or Yes to continue. \
            Or, Press n or No to skip."
        )
        if confirmation.lower() in ["y", "yes"]:
            delete_all_records(conn)

    elif user_input == "6":
        select_all_records(conn)

    elif user_input == "7":
        user_id = input("Enter id of user: ")
        if user_id.isnumeric():
            column_name = input(COLUMN_INPUT_STRING)
            column_value = input(f"Enter value of {column_name}: ")
            update_user(conn, column_name, user_id, column_value)

    else:
        exit()



if __name__ == "__main__":
    main()
