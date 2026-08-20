connection = None

try:
    print("Connecting to database...")
    connection = "Database Connection"
    print("Database connected")

except Exception:
    print("Database connection failed")

finally:
    if connection:
        print("Database connection closed")