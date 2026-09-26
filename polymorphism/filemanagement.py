from abc import ABC, abstractmethod


class File(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


class PDF(File):
    def read(self):
        print("Reading PDF file.")

    def write(self, data):
        print("Writing to PDF:", data)


class Excel(File):
    def read(self):
        print("Reading Excel file.")

    def write(self, data):
        print("Writing to Excel:", data)


class Word(File):
    def read(self):
        print("Reading Word file.")

    def write(self, data):
        print("Writing to Word:", data)


class CSV(File):
    def read(self):
        print("Reading CSV file.")

    def write(self, data):
        print("Writing to CSV:", data)


files = [
    PDF(),
    Excel(),
    Word(),
    CSV()
]

for file in files:
    file.read()
    file.write("Hello Python")