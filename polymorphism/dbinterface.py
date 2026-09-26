from abc import ABC, abstractmethod


class Database(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def close(self):
        pass


class MySQL(Database):
    def connect(self):
        print("Connected to MySQL.")

    def insert(self, data):
        print("Inserted into MySQL:", data)

    def close(self):
        print("MySQL connection closed.")


class MongoDB(Database):
    def connect(self):
        print("Connected to MongoDB.")

    def insert(self, data):
        print("Inserted into MongoDB:", data)

    def close(self):
        print("MongoDB connection closed.")


databases = [MySQL(), MongoDB()]

for database in databases:
    database.connect()
    database.insert({"name": "John"})
    database.close()