class PDFFile:
    def read(self):
        print("Reading PDF file.")


class WordFile:
    def read(self):
        print("Reading Word file.")


class ExcelFile:
    def read(self):
        print("Reading Excel file.")


def read_file(file):
    file.read()


read_file(PDFFile())
read_file(WordFile())
read_file(ExcelFile())