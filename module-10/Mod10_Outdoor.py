import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Erenlevi90M",
    database="outdoor"
)
cursor = conn.cursor()

# Function to display data from a table
def display_table_data(table_name):
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    rows = cursor.fetchall()
    print(f"Data from {table_name} table:")
    for row in rows:
        converted_row = []
        if table_name == "equipment":
            for index, col in enumerate(row):
                if index == 5:
                    if col == 1:
                        converted_row.append("Unusable")
                    elif col == 2:
                        converted_row.append("Damaged")
                    elif col == 3:
                        converted_row.append("Moderate Use")
                    elif col == 4:
                        converted_row.append("Like New")
                    elif col == 5:
                        converted_row.append("New")
                    else:
                        converted_row.append(col)
                else:
                    converted_row.append(col)
            print(converted_row)
        else:
            for col in row:
                converted_row.append(col)
            print(converted_row)
    print()

# Call the function for each table
tables = ["customer", "equipment", "guide", "destinations", "trip", "employee", "equipment_transactions", "booking", "inventory_audit"]
for table in tables:
    display_table_data(table)

# Close the connection
conn.close()
