class MySQL:
    def connect(self):
        print("Connected to MySQL.")


class PostgreSQL:
    def connect(self):
        print("Connected to PostgreSQL.")


class MongoDB:
    def connect(self):
        print("Connected to MongoDB.")


def connect_database(database):
    database.connect()


connect_database(MySQL())
connect_database(PostgreSQL())
connect_database(MongoDB())