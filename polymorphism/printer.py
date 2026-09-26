class Printer:
    def print(self):
        print("Printing a document.")


class PDFPrinter:
    def print(self):
        print("Printing a PDF.")


def do_print(obj):
    obj.print()


do_print(Printer())
do_print(PDFPrinter())