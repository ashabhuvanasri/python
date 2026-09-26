from abc import ABC, abstractmethod


class FileProcessor(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


class PDFProcessor(FileProcessor):
    def read(self):
        print("Reading PDF.")

    def write(self, data):
        print("Writing to PDF:", data)


class ExcelProcessor(FileProcessor):
    def read(self):
        print("Reading Excel.")

    def write(self, data):
        print("Writing to Excel:", data)


files = [PDFProcessor(), ExcelProcessor()]

for file in files:
    file.read()
    file.write("Hello")